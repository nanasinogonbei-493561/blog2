#!/usr/bin/env python3
from __future__ import annotations

import argparse
import mimetypes
import os
from pathlib import Path
from typing import Any

import requests
import yaml
from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parent.parent


def load_config() -> dict[str, Any]:
    with (ROOT / "config" / "blog.yaml").open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def build_session() -> tuple[requests.Session, str, dict[str, Any]]:
    load_dotenv(ROOT / ".env")
    config = load_config()

    url = os.getenv("WP_URL", "").rstrip("/")
    username = os.getenv("WP_USERNAME", "")
    password = os.getenv("WP_APP_PASSWORD", "")
    if not url or not username or not password:
        raise RuntimeError("WP_URL / WP_USERNAME / WP_APP_PASSWORD を .env に設定してください。")

    wp_cfg = config.get("wordpress", {})
    session = requests.Session()
    session.auth = (username, password)
    session.headers.update({"User-Agent": wp_cfg.get("user_agent", "codex-wordpress-blog/1.0")})
    return session, f'{url}{wp_cfg.get("api_base", "/wp-json/wp/v2")}', config


def upload_media(
    session: requests.Session,
    base_url: str,
    config: dict[str, Any],
    file_path: str | Path,
    *,
    alt_text: str = "",
    caption: str = "",
    title: str = "",
) -> dict[str, Any]:
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"画像ファイルが見つかりません: {path}")

    mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    wp_cfg = config.get("wordpress", {})
    timeout = wp_cfg.get("timeout_seconds", 30)
    verify = bool(wp_cfg.get("verify_ssl", True))

    headers = {
        "Content-Disposition": f'attachment; filename="{path.name}"',
        "Content-Type": mime_type,
    }
    with path.open("rb") as f:
        response = session.post(
            f"{base_url}/media",
            headers=headers,
            data=f,
            timeout=timeout,
            verify=verify,
        )

    if not response.ok:
        try:
            detail = response.json()
        except Exception:
            detail = response.text[:1000]
        raise RuntimeError(f"メディアアップロード失敗 {response.status_code}: {detail}")

    media = response.json()
    updates: dict[str, str] = {}
    if alt_text:
        updates["alt_text"] = alt_text
    if caption:
        updates["caption"] = caption
    if title:
        updates["title"] = title

    if updates:
        update_response = session.post(
            f'{base_url}/media/{media["id"]}',
            json=updates,
            timeout=timeout,
            verify=verify,
        )
        if not update_response.ok:
            try:
                detail = update_response.json()
            except Exception:
                detail = update_response.text[:1000]
            raise RuntimeError(f"メディア情報更新失敗 {update_response.status_code}: {detail}")
        media = update_response.json()

    return media


def main() -> None:
    parser = argparse.ArgumentParser(description="WordPressメディアアップロード")
    parser.add_argument("file")
    parser.add_argument("--alt", default="")
    parser.add_argument("--caption", default="")
    parser.add_argument("--title", default="")
    args = parser.parse_args()

    session, base_url, config = build_session()
    media = upload_media(
        session,
        base_url,
        config,
        args.file,
        alt_text=args.alt,
        caption=args.caption,
        title=args.title,
    )
    print(f'uploaded: ID={media["id"]}')
    print(media.get("source_url", ""))


if __name__ == "__main__":
    main()
