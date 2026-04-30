from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path

from graphify_zoro.config import get_settings
from graphify_zoro.ocr_corpus import _output_base, _output_markdown_path


def _iter_pdfs(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() == ".pdf"
    )


def main() -> None:
    parser = argparse.ArgumentParser(prog="graphify-zoro-ocr-status")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Directory to write status logs into.",
    )
    args = parser.parse_args()

    settings = get_settings()
    pdfs = _iter_pdfs(settings.source_corpus)
    converted: list[Path] = []
    pending: list[Path] = []

    for source_path in pdfs:
        output_base = _output_base(settings.raw_ocr_dir, settings.source_corpus, source_path)
        if _output_markdown_path(output_base).exists():
            converted.append(source_path)
        else:
            pending.append(source_path)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir = args.out_dir or settings.project_root / "docs" / "ocr-status"
    out_dir.mkdir(parents=True, exist_ok=True)

    converted_path = out_dir / f"{timestamp}-converted-pdfs.txt"
    pending_path = out_dir / f"{timestamp}-pending-pdfs.txt"
    summary_path = out_dir / f"{timestamp}-summary.txt"

    converted_path.write_text("\n".join(str(path) for path in converted) + "\n", encoding="utf-8")
    pending_path.write_text("\n".join(str(path) for path in pending) + "\n", encoding="utf-8")
    summary_path.write_text(
        "\n".join(
            [
                f"source_corpus={settings.source_corpus}",
                f"raw_ocr_dir={settings.raw_ocr_dir}",
                f"total_pdfs={len(pdfs)}",
                f"converted_pdfs={len(converted)}",
                f"pending_pdfs={len(pending)}",
                f"converted_list={converted_path}",
                f"pending_list={pending_path}",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print(summary_path)


if __name__ == "__main__":
    main()
