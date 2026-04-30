#!/bin/sh
set -eu

changed="${1:-}"
if [ -z "$changed" ]; then
  exit 0
fi

if printf '%s\n' "$changed" | grep -E '^(raw/source/|raw/ocr/|graphify-input/)' >/dev/null 2>&1; then
  mkdir -p graphify-out
  {
    echo "Semantic graph update required."
    echo "Changed corpus/OCR/input files:"
    printf '%s\n' "$changed" | grep -E '^(raw/source/|raw/ocr/|graphify-input/)' || true
    echo
    echo "Resume with:"
    echo "  cd /Users/ali/GRAPHIFY-zoroastrianism"
    echo "  source .venv/bin/activate"
    echo "  graphify-zoro-ocr --suffix .pdf"
    echo "  graphify-zoro-ocr-status"
    echo "  find graphify-input/ocr-markdown -type l -delete"
    echo "  find raw/ocr -maxdepth 1 -type f -name '*.md' -exec ln -sf \"\$PWD/{}\" graphify-input/ocr-markdown/ \\;"
    echo "  graphify-zoro-llm --input graphify-input/ocr-markdown --workers 2 --timeout 1200"
  } > graphify-out/needs_update
  echo "[graphify-zoro hook] Corpus/OCR files changed. Wrote graphify-out/needs_update."
fi
