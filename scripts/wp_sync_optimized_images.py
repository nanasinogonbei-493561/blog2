#!/usr/bin/env python3
"""軽量化済み画像（optimized/*.jpg）をWordPressへ差し替えアップロードする補助スクリプト。"""
from __future__ import annotations

import argparse
import html
import re
from pathlib import Path
from typing import Any

import frontmatter

import wp_publish
from wp_media import upload_media

ROOT = Path(__file__).resolve().parent.parent


def extract_alt_from_content(content: str, img_url: str) -> str:
    """本文HTML内の対象画像タグから alt 属性を抽出する。"""
    m_tag = re.search(rf"<img\b[^>]*?{re.escape(img_url)}[^>]*>", content)
    if not m_tag:
        return ""
    m_alt = re.search(r'alt="([^"]+)"', m_tag.group(0))
    return html.unescape(m_alt.group(1)).strip() if m_alt else ""


def resolve_optimized_path(img_dir: Path, filename: str) -> Path:
    """元ファイル名に対応する optimized/<stem>.jpg パスを返す。"""
    candidate = img_dir / "optimized" / f"{Path(filename).stem}.jpg"
    if not candidate.is_file():
        raise FileNotFoundError(f"軽量化画像が見つかりません: {candidate}")
    return candidate


def replace_image_references(
    content: str,
    old_id: int,
    old_url: str,
    new_id: int,
    new_url: str,
) -> str:
    """本文（日英両タブ）内の wp:image メディアID・クラス・URLを差し替える。"""
    updated = content.replace(old_url, new_url)
    updated = updated.replace(f"wp-image-{old_id}", f"wp-image-{new_id}")
    updated = re.sub(
        rf'("id"\s*:\s*){old_id}\b',
        rf"\g<1>{new_id}",
        updated,
    )
    return updated


def sync_article_images(article_path: Path, *, apply: bool) -> None:
    """記事の使用画像を optimized/*.jpg へ差し替える（--apply 指定時のみアップロード・更新）。"""
    post = frontmatter.load(article_path)
    meta: dict[str, Any] = post.metadata
    featured_raw = str(meta.get("featured_image", "")).strip()
    if not featured_raw:
        raise ValueError(f"featured_image が未設定です: {article_path}")

    featured_src = ROOT / featured_raw
    img_dir = (
        featured_src.parent.parent
        if featured_src.parent.name == "optimized"
        else featured_src.parent
    )
    inline_media: dict[str, Any] = meta.get("wordpress_inline_media") or {}
    if not inline_media:
        raise ValueError(f"wordpress_inline_media が未設定です: {article_path}")

    title = str(meta.get("title", "")).strip()
    featured_alt = str(meta.get("featured_image_alt", "")).strip()

    plan_items: list[tuple[str, Path, int, str, str]] = []
    for orig_name, info in inline_media.items():
        opt_path = resolve_optimized_path(img_dir, orig_name)
        old_id = int(info["id"])
        old_url = str(info["url"])
        alt = str(
            info.get("alt")
            or extract_alt_from_content(post.content, old_url)
            or (featured_alt if orig_name == featured_src.name else "")
        ).strip()
        plan_items.append((orig_name, opt_path, old_id, old_url, alt))

    if not apply:
        print(f"DRY RUN: {article_path.name} ({len(plan_items)}枚)")
        for orig_name, opt_path, old_id, old_url, alt in plan_items:
            size_kb = opt_path.stat().st_size / 1024
            print(f"  - {orig_name} (ID={old_id}) -> {opt_path.name} ({size_kb:.1f}KB) alt={bool(alt)}")
        return

    config = wp_publish.load_config()
    session, base_url = wp_publish.build_session(config)

    new_inline: dict[str, Any] = {}
    new_content = post.content
    featured_new_id: int | None = None
    featured_opt_rel = str(
        resolve_optimized_path(img_dir, featured_src.name).relative_to(ROOT)
    )

    for orig_name, opt_path, old_id, old_url, alt in plan_items:
        media = upload_media(
            session,
            base_url,
            config,
            opt_path,
            alt_text=alt,
            title=f"{title} ({opt_path.stem})",
        )
        new_id = int(media["id"])
        new_url = str(media["source_url"])
        entry: dict[str, Any] = {"id": new_id, "url": new_url}
        if alt:
            entry["alt"] = alt
        new_inline[opt_path.name] = entry
        new_content = replace_image_references(
            new_content, old_id, old_url, new_id, new_url
        )
        if orig_name == featured_src.name:
            featured_new_id = new_id

    meta["featured_image"] = featured_opt_rel
    if featured_new_id is not None:
        meta["wordpress_featured_media_id"] = featured_new_id
    meta["wordpress_inline_media"] = new_inline
    post.content = new_content

    article_path.write_text(frontmatter.dumps(post), encoding="utf-8")
    wp_publish.publish_article(
        article_path,
        force_status=str(meta.get("status", "draft")),
        dry_run=False,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="軽量化済み画像をWordPressへ差し替え反映")
    parser.add_argument("article", help="対象Markdownファイル")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="実際にWordPressへアップロードし記事を更新する（未指定時はdry-run）",
    )
    args = parser.parse_args()
    sync_article_images(Path(args.article).resolve(), apply=args.apply)


if __name__ == "__main__":
    main()
