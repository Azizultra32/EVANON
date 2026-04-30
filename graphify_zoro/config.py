from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    project_root: Path
    source_corpus: Path
    raw_dir: Path
    raw_ocr_dir: Path
    graphify_out_dir: Path
    datalab_api_key: str
    datalab_mode: str

    def ensure_directories(self) -> None:
        for path in (
            self.project_root,
            self.raw_dir,
            self.raw_ocr_dir,
            self.graphify_out_dir,
        ):
            path.mkdir(parents=True, exist_ok=True)


def get_settings() -> Settings:
    load_dotenv()
    project_root = Path(
        os.environ.get("GRAPHIFY_PROJECT_ROOT", "/Users/ali/GRAPHIFY-zoroastrianism")
    ).expanduser()
    raw_dir = project_root / "raw"
    settings = Settings(
        project_root=project_root,
        source_corpus=Path(os.environ["SOURCE_CORPUS"]).expanduser(),
        raw_dir=raw_dir,
        raw_ocr_dir=raw_dir / "ocr",
        graphify_out_dir=project_root / "graphify-out",
        datalab_api_key=os.environ["DATALAB_API_KEY"],
        datalab_mode=os.environ.get("DATALAB_MODE", "accurate"),
    )
    settings.ensure_directories()
    return settings
