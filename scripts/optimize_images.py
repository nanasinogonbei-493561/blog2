#!/usr/bin/env python3
"""公開記事で使用しているローカル画像を長辺1200px・200KB以下目標でJPEG圧縮する。"""
from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SIPS_BIN = "/usr/bin/sips"
QUALITY_STEPS = (80, 72, 64, 56)


def parse_used_images(article_path: Path) -> list[Path]:
    """記事のFront Matterから実使用中の画像ファイルパス一覧を抽出する。"""
    text = article_path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return []
    fm = match.group(1)

    featured_match = re.search(r"^featured_image:\s*(.+)$", fm, re.M)
    featured_raw = (
        featured_match.group(1).strip().strip('"').strip("'")
        if featured_match
        else ""
    )
    img_dir = (ROOT / featured_raw).parent if featured_raw else None

    used: list[Path] = []
    seen: set[Path] = set()

    def add_path(candidate: Path) -> None:
        resolved = candidate.resolve()
        if resolved.is_file() and resolved not in seen:
            seen.add(resolved)
            used.append(resolved)

    if featured_raw:
        add_path(ROOT / featured_raw)

    inline_block = re.search(
        r"^wordpress_inline_media:\n((?:  .*\n)+)", fm, re.M
    )
    if inline_block and img_dir is not None:
        for line in inline_block.group(1).splitlines():
            key_match = re.match(r"^  ([^:\s][^:]+):\s*$", line)
            if key_match:
                add_path(img_dir / key_match.group(1).strip().strip('"').strip("'"))

    return used


def get_max_dimension(image_path: Path) -> int:
    """sipsで画像の長辺ピクセル数を取得する。"""
    res = subprocess.run(
        [SIPS_BIN, "-g", "pixelWidth", "-g", "pixelHeight", str(image_path)],
        check=True,
        capture_output=True,
        text=True,
    )
    dims = [
        int(m.group(1))
        for m in re.finditer(r"pixel(?:Width|Height):\s*(\d+)", res.stdout)
    ]
    return max(dims) if dims else 0


def optimize_one(
    src_path: Path,
    dest_path: Path,
    *,
    max_edge: int,
    target_kb: int,
) -> tuple[int, int, int]:
    """1枚の画像を長辺制限＋段階JPEG圧縮し、(元bytes, 圧縮後bytes, 採用品質)を返す。"""
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    src_bytes = src_path.stat().st_size
    max_dim = get_max_dimension(src_path)
    target_bytes = target_kb * 1024

    best_quality = QUALITY_STEPS[-1]
    for quality in QUALITY_STEPS:
        cmd = [
            SIPS_BIN,
            "-s",
            "format",
            "jpeg",
            "-s",
            "formatOptions",
            str(quality),
        ]
        if max_dim > max_edge:
            cmd.extend(["-Z", str(max_edge)])
        cmd.extend([str(src_path), "--out", str(dest_path)])
        subprocess.run(cmd, check=True, capture_output=True, text=True)

        best_quality = quality
        if dest_path.stat().st_size <= target_bytes:
            break

    return src_bytes, dest_path.stat().st_size, best_quality


def main() -> None:
    parser = argparse.ArgumentParser(description="公開記事の使用画像をJPEG圧縮・リサイズ")
    parser.add_argument(
        "--articles-dir",
        default="articles/published",
        help="対象Markdownディレクトリ",
    )
    parser.add_argument("--max-edge", type=int, default=1200, help="長辺の最大ピクセル")
    parser.add_argument("--target-kb", type=int, default=200, help="1枚あたりの目標上限KB")
    args = parser.parse_args()

    articles = sorted((ROOT / args.articles_dir).glob("*.md"))
    total_before = 0
    total_after = 0
    image_count = 0

    for article in articles:
        images = parse_used_images(article)
        art_before = 0
        art_after = 0
        details: list[str] = []

        for src in images:
            dest = src.parent / "optimized" / f"{src.stem}.jpg"
            before_b, after_b, q = optimize_one(
                src, dest, max_edge=args.max_edge, target_kb=args.target_kb
            )
            art_before += before_b
            art_after += after_b
            image_count += 1
            details.append(
                f"    {src.name} -> optimized/{dest.name}: "
                f"{before_b/1024:.1f}KB -> {after_b/1024:.1f}KB (q={q})"
            )

        total_before += art_before
        total_after += art_after
        pct = (1 - art_after / art_before) * 100 if art_before else 0.0
        print(
            f"{article.name}: {art_before/1024:.1f}KB -> {art_after/1024:.1f}KB "
            f"(-{pct:.1f}%, {len(images)}枚)"
        )
        for line in details:
            print(line)

    overall_pct = (1 - total_after / total_before) * 100 if total_before else 0.0
    print(
        f"\nTOTAL ({image_count}枚): {total_before/1024:.1f}KB -> {total_after/1024:.1f}KB "
        f"(-{overall_pct:.1f}%)"
    )


if __name__ == "__main__":
    main()
