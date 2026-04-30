# Git Workflow

This repository tracks the Zoroastrian/Mithras corpus, OCR output, and Graphify graph artifacts.

## What Is Tracked

- `raw/source/` contains the original PDF/TIFF/image/source corpus. Heavy files are stored with Git LFS.
- `raw/ocr/` contains Datalab OCR output, including Markdown, metadata, and OCR image assets.
- `graphify-input/ocr-markdown/` contains symlinks to OCR Markdown files used as Graphify input.
- `graphify-out/` contains the queryable graph, report, visualizations, pass artifacts, Obsidian export, and LLM cache.
- `.githooks/` contains versioned Git hooks.

## What Is Ignored

- `.env` is ignored because it contains API keys.
- `.venv/`, `__pycache__/`, and build metadata are ignored.
- Machine-local Graphify files such as `graphify-out/.graphify_python`, `manifest.json`, and `cost.json` are ignored.

## Hooks

The repo uses `core.hooksPath=.githooks`.

- Git LFS hooks keep large PDFs/TIFFs/images/media stored through LFS.
- Graphify hook markers are installed, so `graphify hook status` reports installed.
- The hooks are corpus-safe: they do not run the stock code-only rebuild because that would overwrite the Zoroastrian corpus graph with a graph of helper scripts.
- When files under `raw/source/`, `raw/ocr/`, or `graphify-input/` change, the hook writes `graphify-out/needs_update`.

## Resume A Semantic Update

```bash
cd /Users/ali/GRAPHIFY-zoroastrianism
source .venv/bin/activate
graphify-zoro-ocr --suffix .pdf
graphify-zoro-ocr-status
find graphify-input/ocr-markdown -type l -delete
find raw/ocr -maxdepth 1 -type f -name '*.md' -exec ln -sf "$PWD/{}" graphify-input/ocr-markdown/ \;
graphify-zoro-llm --input graphify-input/ocr-markdown --workers 2 --timeout 1200
```

The LLM cache in `graphify-out/llm-cache/` prevents reprocessing chunks already completed for the same model, reasoning setting, prompt version, and source text.

## Push To GitHub

The GitHub repository should be created empty: no README, no `.gitignore`, no license, no template.

```bash
git remote add origin https://github.com/Azizultra32/EVANON.git
git branch -M main
git push -u origin main
```
