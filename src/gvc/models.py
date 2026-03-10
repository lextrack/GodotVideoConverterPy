from dataclasses import dataclass


@dataclass(slots=True)
class VideoInfo:
    is_valid: bool = False
    duration: float = 0.0
    width: int = 0
    height: int = 0
    frame_rate: float = 0.0
    video_codec: str = ""
    audio_codec: str = ""
    bit_rate: int = 0
    has_audio: bool = False

    @property
    def aspect_ratio(self) -> str:
        return f"{self.width}:{self.height}" if self.width > 0 and self.height > 0 else "Unknown"

    @property
    def resolution(self) -> str:
        return f"{self.width}x{self.height}" if self.width > 0 and self.height > 0 else "Unknown"
