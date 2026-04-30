#!/usr/bin/env python3
"""Create a deduped Markdown input folder for Graphify and Cognee.

Raw OCR output is kept intact for provenance. This script builds a clean input
folder containing one symlink per unique Markdown content hash, plus a manifest
documenting which duplicates were excluded.
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import UTC, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "raw" / "ocr"
CLEAN_DIR = ROOT / "graphify-input" / "ocr-markdown-clean"
MANIFEST = ROOT / "docs" / "deduped-ocr-markdown-manifest.json"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def canonical_score(path: Path) -> tuple[int, int, int, str]:
    """Lower is better.

    Prefer original-looking names over Finder/copy duplicates while keeping the
    choice deterministic.
    """
    stem = path.stem.lower()
    copy_penalty = 1 if "copy" in stem else 0
    numeric_suffix_penalty = 1 if re.search(r"(?:^| )\d+(?:$|--)", stem) else 0
    hash_suffix_penalty = 1 if re.search(r"--[0-9a-f]{8}$", stem) else 0
    return (copy_penalty, numeric_suffix_penalty, hash_suffix_penalty, path.name.lower())


def build() -> dict:
    if not SOURCE_DIR.exists():
        raise SystemExit(f"Source OCR directory not found: {SOURCE_DIR}")

    groups: dict[str, list[Path]] = {}
    for path in sorted(SOURCE_DIR.glob("*.md")):
        groups.setdefault(sha256(path), []).append(path)

    CLEAN_DIR.mkdir(parents=True, exist_ok=True)
    for existing in CLEAN_DIR.iterdir():
        if existing.is_symlink() or existing.is_file():
            existing.unlink()

    included = []
    duplicate_groups = []
    for content_hash, paths in sorted(groups.items(), key=lambda item: sorted(p.name for p in item[1])[0].lower()):
        selected = sorted(paths, key=canonical_score)[0]
        link_path = CLEAN_DIR / selected.name
        link_path.symlink_to(Path("..") / ".." / selected.relative_to(ROOT))
        included.append(
            {
                "path": str(selected.relative_to(ROOT)),
                "link": str(link_path.relative_to(ROOT)),
                "content_hash": content_hash,
                "bytes": selected.stat().st_size,
            }
        )
        if len(paths) > 1:
            duplicate_groups.append(
                {
                    "content_hash": content_hash,
                    "selected": str(selected.relative_to(ROOT)),
                    "excluded": [str(path.relative_to(ROOT)) for path in sorted(paths) if path != selected],
                }
            )

    manifest = {
        "generated_at": datetime.now(UTC).isoformat(),
        "source_dir": str(SOURCE_DIR.relative_to(ROOT)),
        "clean_dir": str(CLEAN_DIR.relative_to(ROOT)),
        "source_markdown_count": sum(len(paths) for paths in groups.values()),
        "unique_markdown_count": len(groups),
        "duplicate_group_count": len(duplicate_groups),
        "duplicate_files_excluded": sum(len(group["excluded"]) for group in duplicate_groups),
        "included": included,
        "duplicate_groups": duplicate_groups,
    }
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> None:
    manifest = build()
    print(json.dumps({k: manifest[k] for k in (
        "source_markdown_count",
        "unique_markdown_count",
        "duplicate_group_count",
        "duplicate_files_excluded",
        "clean_dir",
        "source_dir",
    )}, indent=2))


if __name__ == "__main__":
    main()
