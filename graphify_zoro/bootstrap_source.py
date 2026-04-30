from __future__ import annotations

from pathlib import Path

from graphify_zoro.config import get_settings


def main() -> None:
    settings = get_settings()
    link_path = settings.raw_dir / "source"
    if link_path.exists() or link_path.is_symlink():
        if link_path.resolve() == settings.source_corpus.resolve():
            print(f"Source link already points at {settings.source_corpus}")
            return
        raise SystemExit(f"{link_path} already exists and points elsewhere.")

    link_path.symlink_to(settings.source_corpus, target_is_directory=True)
    print(f"Created source link: {link_path} -> {settings.source_corpus}")


if __name__ == "__main__":
    main()
