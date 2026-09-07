#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import shutil
import sys
from pathlib import Path
from typing import Any

import frontmatter
import markdown
import requests
import yaml
from dotenv import load_dotenv

from wp_categories import resolve_term_ids
from wp_media import upload_media


ROOT = Path(__file__).resolve().parent.parent


def load_config() -> dict[str, Any]:
    with (ROOT / "config" / "blog.yaml").open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def build_session(config: dict[str, Any]) -> tuple[requests.Session, str]:
    load_dotenv(ROOT / ".env")

    url = os.getenv("WP_URL", "").rstrip("/")
    username = os.getenv("WP_USERNAME", "")
    password = os.getenv("WP_APP_PASSWORD", "")
    if not url or not username or not password:
        raise RuntimeError("WP_URL / WP_USERNAME / WP_APP_PASSWORD を .env に設定してください。")

    wp_cfg = config.get("wordpress", {})
    session = requests.Session()
    session.auth = (username, password)
    session.headers.update({"User-Agent": wp_cfg.get("user_agent", "codex-wordpress-blog/1.0")})
    return session, f'{url}{wp_cfg.get("api_base", "/wp-json/wp/v2")}'


def api_request(
    session: requests.Session,
    config: dict[str, Any],
    method: str,
    url: str,
    **kwargs: Any,
) -> requests.Response:
    wp_cfg = config.get("wordpress", {})
    response = session.request(
        method,
        url,
        timeout=wp_cfg.get("timeout_seconds", 30),
        verify=bool(wp_cfg.get("verify_ssl", True)),
        **kwargs,
    )
    if not response.ok:
        try:
            detail = response.json()
        except Exception:
            detail = response.text[:1200]
        raise RuntimeError(f"WordPress API error {response.status_code}: {detail}")
    return response


def check_connection(session: requests.Session, base_url: str, config: dict[str, Any]) -> None:
    # context=edit requires authentication and is a useful credential/capability check.
    response = api_request(
        session,
        config,
        "GET",
        f"{base_url}/users/me",
        params={"context": "edit"},
    )
    user = response.json()
    print(f'接続成功: user={user.get("name", "")} (ID={user.get("id", "")})')


def as_string_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value] if value.strip() else []
    if isinstance(value, (list, tuple)):
        return [str(x).strip() for x in value if str(x).strip()]
    return [str(value).strip()]


def resolve_featured_image(article_path: Path, value: str) -> Path | None:
    if not value.strip():
        return None
    p = Path(value)
    candidates = []
    if p.is_absolute():
        candidates.append(p)
    else:
        candidates.append(article_path.parent / p)
        candidates.append(ROOT / p)
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
    raise FileNotFoundError(f"featured_image が見つかりません: {value}")


def article_to_payload(
    article_path: Path,
    config: dict[str, Any],
    session: requests.Session,
    base_url: str,
    *,
    force_status: str | None = None,
    dry_run: bool = False,
) -> tuple[frontmatter.Post, dict[str, Any]]:
    post = frontmatter.load(article_path)
    meta = post.metadata

    title = str(meta.get("title", "")).strip()
    if not title:
        raise ValueError("Front Matterの title は必須です。")

    article_cfg = config.get("article", {})
    publishing_cfg = config.get("publishing", {})
    md_cfg = config.get("markdown", {})

    categories = as_string_list(meta.get("categories")) or as_string_list(article_cfg.get("default_categories"))
    tags = as_string_list(meta.get("tags")) or as_string_list(article_cfg.get("default_tags"))

    if dry_run:
        category_ids: list[int] = []
        tag_ids: list[int] = []
    else:
        category_ids = resolve_term_ids(
            session,
            base_url,
            config,
            "categories",
            categories,
            create_missing=bool(publishing_cfg.get("create_missing_categories", True)),
        )
        tag_ids = resolve_term_ids(
            session,
            base_url,
            config,
            "tags",
            tags,
            create_missing=bool(publishing_cfg.get("create_missing_tags", True)),
        )

    html = markdown.markdown(
        post.content,
        extensions=md_cfg.get("extensions", ["extra", "sane_lists"]),
        output_format=md_cfg.get("output_format", "html5"),
    )

    status = force_status or str(meta.get("status") or config.get("blog", {}).get("default_status", "draft"))
    if status not in {"draft", "pending", "private", "publish", "future"}:
        raise ValueError(f"未対応の status です: {status}")

    payload: dict[str, Any] = {
        "title": title,
        "content": html,
        "status": status,
    }

    slug = str(meta.get("slug", "")).strip()
    excerpt = str(meta.get("excerpt", "")).strip()
    if slug:
        payload["slug"] = slug
    if excerpt:
        payload["excerpt"] = excerpt
    if category_ids:
        payload["categories"] = category_ids
    if tag_ids:
        payload["tags"] = tag_ids

    comment_status = publishing_cfg.get("comment_status")
    ping_status = publishing_cfg.get("ping_status")
    if comment_status in {"open", "closed"}:
        payload["comment_status"] = comment_status
    if ping_status in {"open", "closed"}:
        payload["ping_status"] = ping_status

    featured = resolve_featured_image(article_path, str(meta.get("featured_image", "")))
    stored_media_id = meta.get("wordpress_featured_media_id")

    if featured is not None:
        if dry_run:
            pass
        elif stored_media_id:
            payload["featured_media"] = int(stored_media_id)
        else:
            media = upload_media(
                session,
                base_url,
                config,
                featured,
                alt_text=str(meta.get("featured_image_alt", "")),
                title=title,
            )
            payload["featured_media"] = int(media["id"])
            post.metadata["wordpress_featured_media_id"] = int(media["id"])

    return post, payload


def write_wp_metadata(article_path: Path, post: frontmatter.Post, result: dict[str, Any], status: str) -> None:
    post.metadata["wordpress_post_id"] = int(result["id"])
    post.metadata["wordpress_url"] = result.get("link", "")
    post.metadata["status"] = status
    article_path.write_text(frontmatter.dumps(post), encoding="utf-8")


def move_if_published(article_path: Path, config: dict[str, Any], status: str) -> Path:
    publishing_cfg = config.get("publishing", {})
    if status != "publish" or not publishing_cfg.get("move_file_after_publish", True):
        return article_path

    published_dir = ROOT / publishing_cfg.get("published_dir", "articles/published")
    published_dir.mkdir(parents=True, exist_ok=True)
    destination = published_dir / article_path.name

    if article_path.resolve() == destination.resolve():
        return article_path

    if destination.exists():
        raise FileExistsError(f"公開済み移動先が既に存在します: {destination}")

    shutil.move(str(article_path), str(destination))
    return destination


def publish_article(
    article_path: Path,
    *,
    force_status: str | None,
    dry_run: bool,
) -> None:
    if not article_path.is_file():
        raise FileNotFoundError(f"記事ファイルが見つかりません: {article_path}")

    config = load_config()
    if dry_run:
        # dry-runは認証情報やネットワーク接続なしで実行できる。
        session = requests.Session()
        base_url = ""
    else:
        session, base_url = build_session(config)

    post, payload = article_to_payload(
        article_path,
        config,
        session,
        base_url,
        force_status=force_status,
        dry_run=dry_run,
    )

    existing_id = post.metadata.get("wordpress_post_id")

    if dry_run:
        preview = dict(payload)
        preview["categories"] = as_string_list(post.metadata.get("categories"))
        preview["tags"] = as_string_list(post.metadata.get("tags"))
        preview["content"] = preview["content"][:1000] + (
            "..." if len(preview["content"]) > 1000 else ""
        )
        print("DRY RUN: WordPressへの変更は行いません。")
        print("操作:", "UPDATE" if existing_id else "CREATE")
        if existing_id:
            print("投稿ID:", existing_id)
        print(json.dumps(preview, ensure_ascii=False, indent=2))
        return

    if existing_id:
        endpoint = f"{base_url}/posts/{int(existing_id)}"
        action = "更新"
    else:
        endpoint = f"{base_url}/posts"
        action = "新規作成"

    response = api_request(session, config, "POST", endpoint, json=payload)
    result = response.json()

    write_wp_metadata(article_path, post, result, payload["status"])
    final_path = move_if_published(article_path, config, payload["status"])

    print(f"WordPress {action}成功")
    print(f'ID: {result["id"]}')
    print(f'Status: {result.get("status", payload["status"])}')
    print(f'URL: {result.get("link", "")}')
    print(f'File: {final_path}')


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Markdown記事をWordPressへ投稿・更新")
    parser.add_argument("article", nargs="?", help="articles/drafts/*.md")
    parser.add_argument("--dry-run", action="store_true", help="API変更をせず投稿内容を確認")
    parser.add_argument("--publish", action="store_true", help="明示的にpublishへ変更")
    parser.add_argument("--draft", action="store_true", help="明示的にdraftへ変更")
    parser.add_argument("--check", action="store_true", help="WordPress接続・認証を確認")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.publish and args.draft:
        raise ValueError("--publish と --draft は同時に指定できません。")

    config = load_config()
    if args.check:
        session, base_url = build_session(config)
        check_connection(session, base_url, config)
        return

    if not args.article:
        raise ValueError("記事ファイルを指定してください。例: articles/drafts/example.md")

    force_status = "publish" if args.publish else "draft" if args.draft else None
    publish_article(
        Path(args.article).resolve(),
        force_status=force_status,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("中断しました。", file=sys.stderr)
        raise SystemExit(130)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
