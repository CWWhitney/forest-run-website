#!/usr/bin/env python3 -I
"""Make small, metadata-free web JPEGs from photo originals.

Usage:
  python3 -I scripts/process-photos.py <source_dir> <collection> [selection.csv]

Without a selection file, process all supported images in source_dir. A selection
CSV has columns `source` and `output` and processes only those named files. The
output collection is static/images/<collection>/. Originals stay outside the repo.
"""
import csv, hashlib, re, subprocess, sys, tempfile
from pathlib import Path
from PIL import Image, ImageOps

MAX_PX, QUALITY = 1400, 75
if len(sys.argv) not in {3, 4}:
    raise SystemExit(__doc__)
src, collection = Path(sys.argv[1]), sys.argv[2]
out = Path(__file__).resolve().parent.parent / "static" / "images" / collection
out.mkdir(parents=True, exist_ok=True)
if len(sys.argv) == 4:
    with Path(sys.argv[3]).open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    if not rows or not {"source", "output"}.issubset(rows[0]):
        raise SystemExit("selection CSV needs `source` and `output` columns")
    files = []
    for row in rows:
        source_name, output_name = row["source"], row["output"]
        if Path(source_name).name != source_name or Path(output_name).name != output_name:
            raise SystemExit("selection file names must not contain directories")
        if Path(output_name).suffix.lower() != ".jpg":
            raise SystemExit("output names must end in .jpg")
        files.append((src / source_name, output_name))
else:
    files = [(f, re.sub(r"[^A-Za-z0-9_-]+", "-", f.stem).strip("-") + ".jpg")
             for f in sorted(src.iterdir())]

seen = {}
with tempfile.TemporaryDirectory() as tmp:
    for f, output_name in files:
        ext = f.suffix.lower()
        if ext not in {".heic", ".jpg", ".jpeg", ".png"}:
            print("skip", f.name); continue
        if not f.is_file():
            raise SystemExit(f"missing source photo: {f}")
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
        im.save(out / output_name, "JPEG", quality=QUALITY, optimize=True)  # no EXIF
        print("ok", f.name, "->", output_name)
