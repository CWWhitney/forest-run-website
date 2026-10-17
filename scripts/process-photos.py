#!/usr/bin/env python3 -I
"""Turn originals (HEIC/JPG/PNG) into small, metadata-free web JPEGs.

Usage: python3 -I scripts/process-photos.py <source_dir> <collection>
Writes to static/images/<collection>/ and skips pixel-identical duplicates.
Originals stay outside the repo (Dropbox / object storage).
"""
import hashlib, re, subprocess, sys, tempfile
from pathlib import Path
from PIL import Image, ImageOps

MAX_PX, QUALITY = 1400, 75
src, collection = Path(sys.argv[1]), sys.argv[2]
out = Path(__file__).resolve().parent.parent / "static" / "images" / collection
out.mkdir(parents=True, exist_ok=True)
seen = {}
with tempfile.TemporaryDirectory() as tmp:
    for f in sorted(src.iterdir()):
        ext = f.suffix.lower()
        if ext not in {".heic", ".jpg", ".jpeg", ".png"}:
            print("skip", f.name); continue
        path = f
        if ext == ".heic":
            path = Path(tmp) / (f.stem + ".jpg")
            subprocess.run(["sips", "-s", "format", "jpeg", str(f), "--out", str(path)],
                           check=True, capture_output=True)
        im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
        im.thumbnail((MAX_PX, MAX_PX))
        digest = hashlib.md5(im.tobytes()).hexdigest()
        if digest in seen:
            print("duplicate", f.name, "==", seen[digest]); continue
        seen[digest] = f.name
        im.save(out / (re.sub(r"[^A-Za-z0-9_-]+", "-", f.stem).strip("-") + ".jpg"), "JPEG", quality=QUALITY, optimize=True)  # no EXIF
        print("ok", f.name)
