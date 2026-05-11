#!/usr/bin/env python3
from pathlib import Path
import subprocess
MOVIES_DIR = Path("../movies")
OUTPUT_DIR = MOVIES_DIR / "compressed"
OUTPUT_DIR.mkdir(exist_ok=True)
VIDEO_EXTENSIONS = {".mp4", ".m4v"}
for input_path in MOVIES_DIR.iterdir():
    if input_path.suffix.lower() not in VIDEO_EXTENSIONS:
        continue
    output_path = OUTPUT_DIR / f"{input_path.stem}.mp4"
    print(f"Compressing: {input_path.name}")
    command = [
        "ffmpeg",
        "-y",
        "-i", str(input_path),
        # ===== VIDEO =====
        "-vf",
        "scale='min(1280,iw)':-2",
        "-c:v", "libx264",
        "-preset", "fast",
        "-profile:v", "high",
        "-level", "4.0",
        "-crf", "22",
        "-pix_fmt", "yuv420p",
        # ===== WEB OPTIMIZATION =====
        "-movflags", "+faststart",
        # ===== REMOVE AUDIO =====
        "-an",
        # ===== OUTPUT =====
        str(output_path)
    ]
    subprocess.run(command, check=True)
    print(f"Saved: {output_path}\n")
print("Done.")