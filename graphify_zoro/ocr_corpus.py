from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

from datalab_sdk import ConvertOptions, DatalabClient

from graphify_zoro.config import get_settings


SUPPORTED_SUFFIXES = {
    ".pdf",
    ".tif",
    ".tiff",
    ".png",
    ".jpg",
    ".jpeg",
    ".doc",
    ".docx",
    ".md",
}


def _iter_supported_files(root: Path, suffixes: set[str]) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in suffixes
    )


def _output_base(raw_ocr_dir: Path, source_root: Path, source_path: Path) -> Path:
    relative_name = source_path.relative_to(source_root)
    stem = relative_name.name[: -len(source_path.suffix)]
    safe_stem = stem.replace(".", "_")
    if safe_stem != stem:
        digest = hashlib.sha1(str(relative_name).encode("utf-8")).hexdigest()[:8]
        safe_stem = f"{safe_stem}--{digest}"
    return raw_ocr_dir / relative_name.parent / safe_stem


def _output_markdown_path(output_base: Path) -> Path:
    return output_base.parent / f"{output_base.name}.md"


def main() -> None:
    parser = argparse.ArgumentParser(prog="graphify-zoro-ocr")
    parser.add_argument("--limit", type=int, default=None, help="Only OCR the first N files.")
    parser.add_argument(
        "--suffix",
        action="append",
        default=None,
        help="Only OCR files with this suffix. Can be repeated, e.g. --suffix .pdf.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-run OCR even when the Markdown output already exists.",
    )
    args = parser.parse_args()

    settings = get_settings()
    suffixes = SUPPORTED_SUFFIXES
    if args.suffix:
        suffixes = {suffix.lower() if suffix.startswith(".") else f".{suffix.lower()}" for suffix in args.suffix}
        unsupported = suffixes - SUPPORTED_SUFFIXES
        if unsupported:
            raise SystemExit(f"Unsupported suffixes: {', '.join(sorted(unsupported))}")

    files = _iter_supported_files(settings.source_corpus, suffixes)
    if args.limit is not None:
        files = files[: args.limit]

    if not files:
        raise SystemExit("No supported source files found for OCR.")

    client = DatalabClient(api_key=settings.datalab_api_key)
    options = ConvertOptions(
        output_format="markdown",
        mode=settings.datalab_mode,
        paginate=True,
    )

    for index, source_path in enumerate(files, start=1):
        output_base = _output_base(settings.raw_ocr_dir, settings.source_corpus, source_path)
        output_base.parent.mkdir(parents=True, exist_ok=True)
        output_markdown = _output_markdown_path(output_base)
        if output_markdown.exists() and not args.force:
            print(f"[{index}/{len(files)}] skipping existing {output_markdown}")
            continue

        print(f"[{index}/{len(files)}] converting {source_path}")
        client.convert(
            file_path=source_path,
            options=options,
            save_output=output_base,
        )
    print(f"OCR / conversion output written to {settings.raw_ocr_dir}")


if __name__ == "__main__":
    main()
