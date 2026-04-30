#!/usr/bin/env bash
set -euo pipefail

cd /Users/ali/GRAPHIFY-zoroastrianism
exec .venv/bin/python -m graphify.serve graphify-out/graph.json
