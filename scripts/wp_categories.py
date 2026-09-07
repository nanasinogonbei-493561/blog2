#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
from typing import Any

import requests
import yaml
from dotenv import load_dotenv


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def load_config() -> dict[str, Any]:
    path = os.path.join(ROOT, "config", "blog.yaml")
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def build_session() -> tuple[requests.Session, str, dict[str, Any]]:
    load_dotenv(os.path.join(ROOT, ".env"))
    config = load_config()

    url = os.getenv("WP_URL", "").rstrip("/")
    username = os.getenv("WP_USERNAME", "")
    password = os.getenv("WP_APP_PASSWORD", "")

    if not url or not username or not password:
        raise RuntimeError("WP_URL / WP_USERNAME / WP_APP_PASSWORD を .env に設定してください。")

    wp_cfg = config.get("wordpress", {})
    api_base = wp_cfg.get("api_base", "/wp-json/wp/v2")
    base_url = f"{url}{api_base}"

    session = requests.Session()
    session.auth = (username, password)
    session.headers.update({"User-Agent": wp_cfg.get("user_agent", "codex-wordpress-blog/1.0")})

    return session, base_url, config


def request_json(
    session: requests.Session,
    method: str,
    url: str,
    *,
    config: dict[str, Any],
    **kwargs: Any,
) -> Any:
    wp_cfg = config.get("wordpress", {})
    timeout = wp_cfg.get("timeout_seconds", 30)
    verify = bool(wp_cfg.get("verify_ssl", True))

    response = session.request(method, url, timeout=timeout, verify=verify, **kwargs)
    if not response.ok:
        try:
            detail = response.json()
        except Exception:
            detail = response.text[:1000]
        raise RuntimeError(f"WordPress API error {response.status_code}: {detail}")
    return response.json()


def list_terms(kind: str, *, per_page: int = 100) -> list[dict[str, Any]]:
    if kind not in {"categories", "tags"}:
        raise ValueError("kind は categories または tags")

    session, base_url, config = build_session()
    return request_json(
        session,
        "GET",
        f"{base_url}/{kind}",
        config=config,
        params={"per_page": per_page, "orderby": "name", "order": "asc"},
    )


def find_term_id(
    session: requests.Session,
    base_url: str,
    config: dict[str, Any],
    kind: str,
    name: str,
) -> int | None:
    results = request_json(
        session,
        "GET",
        f"{base_url}/{kind}",
        config=config,
        params={"search": name, "per_page": 100},
    )
    target = name.casefold().strip()
    for term in results:
        if str(term.get("name", "")).casefold().strip() == target:
            return int(term["id"])
    return None


def get_or_create_term(
    session: requests.Session,
    base_url: str,
    config: dict[str, Any],
    kind: str,
    name: str,
    *,
    create_missing: bool = True,
) -> int:
    if kind not in {"categories", "tags"}:
        raise ValueError("kind は categories または tags")

    existing = find_term_id(session, base_url, config, kind, name)
    if existing is not None:
        return existing

    if not create_missing:
        raise RuntimeError(f"{kind} '{name}' が見つかりません。自動作成は無効です。")

    created = request_json(
        session,
        "POST",
        f"{base_url}/{kind}",
        config=config,
        json={"name": name},
    )
    return int(created["id"])


def resolve_term_ids(
    session: requests.Session,
    base_url: str,
    config: dict[str, Any],
    kind: str,
    names: list[str],
    *,
    create_missing: bool,
) -> list[int]:
    ids: list[int] = []
    seen: set[str] = set()
    for raw in names:
        name = str(raw).strip()
        if not name or name.casefold() in seen:
            continue
        seen.add(name.casefold())
        ids.append(
            get_or_create_term(
                session,
                base_url,
                config,
                kind,
                name,
                create_missing=create_missing,
            )
        )
    return ids


def main() -> None:
    parser = argparse.ArgumentParser(description="WordPressカテゴリ/タグ管理")
    sub = parser.add_subparsers(dest="command", required=True)

    p_list = sub.add_parser("list", help="一覧表示")
    p_list.add_argument("kind", choices=["categories", "tags"])

    p_create = sub.add_parser("create", help="カテゴリ/タグを作成")
    p_create.add_argument("kind", choices=["category", "tag"])
    p_create.add_argument("name")

    args = parser.parse_args()

    if args.command == "list":
        for term in list_terms(args.kind):
            print(f'{term["id"]:>5}  {term["name"]}')
        return

    session, base_url, config = build_session()
    kind = "categories" if args.kind == "category" else "tags"
    term_id = get_or_create_term(session, base_url, config, kind, args.name, create_missing=True)
    print(f"{args.kind}: {args.name} -> ID {term_id}")


if __name__ == "__main__":
    main()
