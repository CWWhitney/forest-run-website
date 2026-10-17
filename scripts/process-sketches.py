#!/usr/bin/env python3 -I
"""Turn photos/screenshots of pencil sketches into clean black-and-white line drawings.

Usage: python3 -I scripts/process-sketches.py <source_dir> <collection>
Uses the red channel (blue graph-paper grid vanishes), divides out uneven paper
lighting, then stretches levels so pencil is dark on white. No EXIF is kept.
"""
import re, sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter, ImageOps

MAX_PX = 1400
HI = 0.92             # ratio to local paper brightness: >=HI white; LO is auto-picked per image
SKIP = {"Screen-Shot-2022-10-17-at-22-23-04"}  # output stems to leave out (the desk photo is a regular color photo)
CROP = {"Screen-Shot-2022-10-17-at-22-14-05": 0.07, "Screen-Shot-2022-10-17-at-22-19-21": 0.07}             # output stem -> fraction of each edge to trim (dark photo borders)
ROTATE = {"b320ac28-9866-4ebf-96c2-1c587c03f576": 90, "17ae1b35-0eaf-4e17-8ffa-5a7b774cdcab": 90, "80eceb3d-733d-451d-9319-35c655c8c540": 90, "3c52777f-15c6-4938-962d-3c85320456d7": 180}

src, collection = Path(sys.argv[1]), sys.argv[2]
out = Path(__file__).resolve().parent.parent / "static" / "images" / collection
out.mkdir(parents=True, exist_ok=True)
for f in sorted(src.iterdir()):
    if f.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
        continue
    stem = re.sub(r"[^A-Za-z0-9_-]+", "-", f.stem).strip("-")
    if stem in SKIP:
        continue
    im = ImageOps.exif_transpose(Image.open(f)).convert("RGB")
    im.thumbnail((MAX_PX, MAX_PX))
    r = im.getchannel("R")
    bg = r.filter(ImageFilter.MaxFilter(15)).filter(ImageFilter.GaussianBlur(im.width / 40))
    ratio = np.asarray(r, dtype=np.float32) / np.maximum(np.asarray(bg, dtype=np.float32), 1)
    lo = float(np.clip(np.percentile(ratio, 1), 0.35, 0.8))
    g = np.clip((ratio - lo) / (HI - lo), 0, 1) ** 1.5
    res = Image.fromarray((g * 255).astype(np.uint8), "L")
    if stem in CROP:
        m = int(min(res.size) * CROP[stem])
        res = res.crop((m, m, res.width - m, res.height - m))
    if stem in ROTATE:
        res = res.rotate(ROTATE[stem], expand=True)
    res.save(out / f"{stem}.png", optimize=True)
    print("ok", stem)
