# Godot Video Converter

Desktop utility for converting videos into game-ready formats, with a strong focus on OGV workflows for Godot and atlas generation for 2D pipelines.

This project is a Python rewrite of the original [.NET tool](https://github.com/lextrack/GodotVideoConverter).

## What does this app mainly do?

- Convert videos to `ogv`, `mp4`, `webm`, and `gif`
- Switch between `Godot` and `Love2D` engine profiles for OGV-specific presets
- Apply engine-oriented OGV presets for practical playback workflows
- Generate PNG sprite atlases from video clips
- Batch process multiple files from a simple GUI
- Analyze the selected video before converting
- Show a simple summary of what the video has and what to do next

## Current Positioning

The app is still centered on Godot, but it now includes a dedicated Love2D OGV profile and engine-specific guidance. Love2D has its own OGV preset family and playback recommendations, while the rest of the output formats remain shared between engine profiles.

## Main Workflows

### 1. Convert Video for Godot

Use this when you want a video file ready for in-engine playback.

- `ogv` is the main target for Godot-oriented workflows
- The engine profile changes only the `ogv` preset family; `mp4`, `webm`, and `gif` stay the same
- The `Quality` selector changes the overall image/audio quality; the engine preset changes how the video behaves during playback
- The app analyzes the selected video and shows two blocks: what the video has, and the recommended next step
- Those suggestions can change based on duration, resolution, FPS, audio, source codec, aspect ratio, selected engine, and selected output format
- Godot OGV modes:
  - `Official Godot`: recommended starting point for most Godot videos
  - `Seek Friendly`: better if the video needs to start from different points
  - `Ideal Loop`: better for videos that need to repeat smoothly
  - `Mobile Optimized`: safer choice for weaker devices
  - `High Compression`: smaller file, but less agile when jumping through the video
- Love2D OGV modes:
  - `Love2D Compatibility`: safest starting point for Love2D
  - `Seek Friendly`: better if the video needs to start from different points
  - `Ideal Loop`: better for videos that need to repeat smoothly
  - `Lightweight`: smaller file for simple or decorative playback
- You can also export to `mp4`, `webm`, or `gif`
- Resolution, FPS, and audio handling can be adjusted from the GUI

### 2. Generate Atlas from a Video

Use this when the video is really an animation source and you want frames packed into a texture.

- Export atlas as PNG
- Layout modes:
  - `grid`
  - `horizontal`
  - `vertical`
- Resolution presets:
  - `Low`
  - `Medium`
  - `High`
- Backends:
  - `ffmpeg`
  - `opencv`

This workflow is especially useful for 2D engines, prototyping, UI animation sources, and effects pipelines.

## Why Use This Instead of Raw FFmpeg

FFmpeg already does the heavy lifting. This app is useful because it reduces repeated setup work:

- Presets instead of remembering long command lines
- Safer defaults for common Godot OGV cases
- Batch conversion from a GUI
- Video analysis before export
- Atlas generation in the same tool
- Lightweight recommendations for format and playback decisions

## License

This project is licensed under the MIT License. See `LICENSE`.

## Requirements

- Python 3.11+
- FFmpeg and FFprobe

In this project, `bin/` is mainly used for Windows builds.

### Linux

- Install `ffmpeg` with your distro package manager
- Make sure `ffmpeg` and `ffprobe` are available in `PATH`

Verify:

```bash
ffmpeg -version
ffprobe -version
```

### Windows

Use one of these options:

- `bin/ffmpeg.exe` and `bin/ffprobe.exe`
- `GVC_FFMPEG_DIR=/path/to/binaries`
- FFmpeg binaries available in `PATH`

## Installation (Linux)

Install dependencies for your distro:

```bash
# Arch / CachyOS
sudo pacman -S ffmpeg python

# Debian / Ubuntu
sudo apt update
sudo apt install ffmpeg python3 python3-venv python3-pip

# Fedora
sudo dnf install ffmpeg python3 python3-pip

# openSUSE
sudo zypper install ffmpeg python3 python3-pip
```

Then install the project:

```bash
cd python_converter
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Run the GUI

```bash
gvc-gui
```

## Portable Build

### Linux

1. Install FFmpeg on the system.
2. Verify `ffmpeg` and `ffprobe` are available.
3. Run:

```bash
./scripts/build_linux.sh
```

Output is generated in `dist/gvc/`.

Linux distribution notes:

- Ship the full `dist/gvc/` directory
- End users still need `ffmpeg` and `ffprobe` available in `PATH`

### Windows

1. Copy binaries to `bin/ffmpeg.exe` and `bin/ffprobe.exe`
2. Run:

```powershell
./scripts/build_windows.ps1
```

Output is generated in `dist/gvc/`.

Windows distribution notes:

- Ship the full `dist/gvc/` directory
- FFmpeg binaries are bundled only if they were present in `bin/` during the build

## Project Structure

- `src/gvc/gui.py`: PySide6 desktop interface
- `src/gvc/convert.py`: conversion presets and FFmpeg argument building
- `src/gvc/atlas.py`: atlas generation with FFmpeg or OpenCV
- `src/gvc/probe.py`: metadata probing through FFprobe
- `src/gvc/recommendations.py`: Godot-oriented playback recommendations
- `src/gvc/ffmpeg_paths.py`: FFmpeg and FFprobe path resolution
- `src/gvc/settings.py`: persisted UI settings
- `src/gvc/i18n.py`: UI text and localization helpers
