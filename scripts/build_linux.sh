#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if ! command -v ffmpeg >/dev/null 2>&1 || ! command -v ffprobe >/dev/null 2>&1; then
  echo "Missing ffmpeg/ffprobe in PATH. Install them with your distro package manager."
  exit 1
fi

python -m pip install -r requirements-dev.txt
python -m pip install -e .

pyinstaller \
  --noconfirm \
  --clean \
  --name gvc \
  --onedir \
  --windowed \
  --icon Assets/icon.png \
  --copy-metadata godot-video-converter-py \
  --add-data "Assets/icon.png:Assets" \
  --add-data "Assets/icon.ico:Assets" \
  --paths src \
  src/gvc/__main__.py

echo "Build ready at dist/gvc/"
