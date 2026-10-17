#!/usr/bin/env python3 -I
"""Turn photos/scans of pencil sketches into clean black-and-white line drawings.

Usage: python3 -I scripts/process-sketches.py <source> <collection>
<source> is a folder of images/PDFs or a single PDF (PDF pages are rendered with
pdftoppm and named <pdfname>-<page>). Output: static/images/<collection>/.
Divides out uneven paper lighting, then stretches levels so pencil is dark on
white. No EXIF is kept. Per-file settings are in the dicts below.
"""
import re, subprocess, sys, tempfile
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter, ImageOps

MAX_PX = 1400
HI = 0.92  # default: ratio to local paper brightness >= HI is white (low cut is auto per image)
SKIP = {   # output stems left out
    "Screen-Shot-2022-10-17-at-22-23-04",  # desk photo, kept as a regular color photo
    "17ae1b35-0eaf-4e17-8ffa-5a7b774cdcab", "80eceb3d-733d-451d-9319-35c655c8c540",  # too faint
    "Screen-Shot-2022-10-17-at-22-14-05", "Screen-Shot-2022-10-17-at-22-19-21",      # rough photos of plans
    "Screenshot-2022-11-22-at-17-17-26", "Screenshot-2022-11-22-at-17-18-05",  # same plan twice, ruler edge in frame
    "3c52777f-15c6-4938-962d-3c85320456d7",  # faint wall section; see blueprint-6
    "blueprint-7",  # septic application form: someone else's paperwork, not a drawing
}
CROP = {}  # stem -> fraction of each edge to trim (dark photo borders)
LEVELS = {f"blueprint-{n}": (0.40, 0.62) for n in range(1, 7)}  # stem -> fixed (lo, hi) for clean scans
ROTATE = {  # stem -> degrees counter-clockwise
    "b320ac28-9866-4ebf-96c2-1c587c03f576": 90, "3c52777f-15c6-4938-962d-3c85320456d7": 180,
    "blueprint-1": 90, "blueprint-2": 90, "blueprint-3": 90, "blueprint-4": 90,
}

src, collection = Path(sys.argv[1]), sys.argv[2]
out = Path(__file__).resolve().parent.parent / "static" / "images" / collection
out.mkdir(parents=True, exist_ok=True)

def clean(im, stem):
    if stem in LEVELS:  # clean scan: work at full resolution, grayscale
        gray = im.convert("L")
        bg = gray.filter(ImageFilter.MaxFilter(21)).filter(ImageFilter.GaussianBlur(gray.width / 40))
        lo, hi, gamma = *LEVELS[stem], 1.0
        ratio = np.asarray(gray, dtype=np.float32) / np.maximum(np.asarray(bg, dtype=np.float32), 1)
    else:  # photo: red channel makes blue graph-paper grid vanish
        im.thumbnail((MAX_PX, MAX_PX))
        r = im.getchannel("R")
        bg = r.filter(ImageFilter.MaxFilter(15)).filter(ImageFilter.GaussianBlur(im.width / 40))
        ratio = np.asarray(r, dtype=np.float32) / np.maximum(np.asarray(bg, dtype=np.float32), 1)
        lo, hi, gamma = float(np.clip(np.percentile(ratio, 1), 0.35, 0.8)), HI, 1.5
    g = np.clip((ratio - lo) / (hi - lo), 0, 1) ** gamma
    return Image.fromarray((g * 255).astype(np.uint8), "L")

def save(im, stem):
    if stem in SKIP:
        return
    res = clean(im.convert("RGB"), stem)
    if stem in CROP:
        m = int(min(res.size) * CROP[stem])
        res = res.crop((m, m, res.width - m, res.height - m))
    if stem in ROTATE:
        res = res.rotate(ROTATE[stem], expand=True)
    res.thumbnail((MAX_PX, MAX_PX), Image.LANCZOS)
    name = f"00-{stem}" if stem.startswith("blueprint") else stem  # sorts the blueprints first in galleries
    res.save(out / f"{name}.png", optimize=True)
    print("ok", stem)

with tempfile.TemporaryDirectory() as tmp:
    for f in sorted([src] if src.is_file() else src.iterdir()):
        stem = re.sub(r"[^A-Za-z0-9_-]+", "-", f.stem).strip("-")
        if f.suffix.lower() == ".pdf":
            subprocess.run(["pdftoppm", "-r", "170", "-png", str(f), f"{tmp}/{stem}"], check=True)
            for page in sorted(Path(tmp).glob(f"{stem}-*.png")):
                save(Image.open(page), re.sub(r"-0+(\d)", r"-\1", page.stem))  # pdftoppm may zero-pad
        elif f.suffix.lower() in {".jpg", ".jpeg", ".png"}:
            save(ImageOps.exif_transpose(Image.open(f)), stem)
