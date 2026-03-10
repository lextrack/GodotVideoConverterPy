from __future__ import annotations

import re
import subprocess
import sys
from threading import Event
from typing import Callable

TIME_RE = re.compile(r"time=(\d+):(\d+):(\d+(?:\.\d+)?)")


class FFmpegRunError(RuntimeError):
    pass


ProgressCallback = Callable[[int], None]


def _hidden_subprocess_kwargs() -> dict[str, object]:
    if sys.platform != "win32":
        return {}
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    return {
        "creationflags": subprocess.CREATE_NO_WINDOW,
        "startupinfo": startupinfo,
    }


def run_ffmpeg(
    ffmpeg_path: str,
    args: list[str],
    total_seconds: float | None = None,
    on_progress: ProgressCallback | None = None,
    cancel_event: Event | None = None,
) -> None:
    cmd = [ffmpeg_path, *args]
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        bufsize=1,
        **_hidden_subprocess_kwargs(),
    )

    if process.stderr is None:
        raise FFmpegRunError("Failed to capture FFmpeg stderr")

    last_progress = 0
    errors: list[str] = []

    for line in process.stderr:
        if cancel_event and cancel_event.is_set():
            process.terminate()
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                process.kill()
            raise FFmpegRunError("FFmpeg run cancelled by user")

        if "Error" in line or "Invalid" in line or "No such" in line or "Permission denied" in line:
            errors.append(line.strip())

        match = TIME_RE.search(line)
        if match and total_seconds and total_seconds > 0:
            h = float(match.group(1))
            m = float(match.group(2))
            s = float(match.group(3))
            current = h * 3600 + m * 60 + s
            percent = int(min((current / total_seconds) * 100, 100))
            if percent > last_progress:
                last_progress = percent
                if on_progress:
                    on_progress(percent)

    if cancel_event and cancel_event.is_set():
        process.terminate()
        try:
            process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            process.kill()
        raise FFmpegRunError("FFmpeg run cancelled by user")

    process.wait()
    if process.returncode != 0:
        detail = "; ".join(errors[:5]) if errors else f"Exit code {process.returncode}"
        raise FFmpegRunError(f"FFmpeg failed: {detail}")

    if on_progress:
        on_progress(100)
