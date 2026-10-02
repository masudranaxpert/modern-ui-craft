"""Build contact-sheet grids from inbox/ inbox images for AI classification."""
import os
from PIL import Image, ImageDraw

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "inbox")
OUT = os.path.join(BASE, "_grids")
os.makedirs(OUT, exist_ok=True)

files = [
    os.path.join(SRC, f) for f in sorted(os.listdir(SRC))
    if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
]

# numeric sort: photo_2 before photo_10
import re
def numkey(p):
    m = re.search(r"photo_(\d+)_", os.path.basename(p))
    return int(m.group(1)) if m else 0
files.sort(key=numkey)

TW, TH = 560, 420
COLS, ROWS = 2, 3
batch_size = COLS * ROWS
num_grids = (len(files) + batch_size - 1) // batch_size

manifest_all = []
for g in range(num_grids):
    batch = files[g * batch_size:(g + 1) * batch_size]
    sheet = Image.new("RGB", (COLS * TW, ROWS * (TH + 30)), "#dddddd")
    d = ImageDraw.Draw(sheet)
    manifest = []
    for i, path in enumerate(batch):
        name = os.path.basename(path)
        idx = numkey(path)
        img = Image.open(path).convert("RGB")
        img.thumbnail((TW - 8, TH - 8))
        x = (i % COLS) * TW
        y = (i // COLS) * (TH + 30)
        sheet.paste(img, (x + 4, y + 4))
        d.text((x + 8, y + TH + 6), f"[{idx}] {name[:44]}", fill="black")
        manifest.append(f"[{idx}] {name} -> {path}")
    out_path = os.path.join(OUT, f"inbox_grid_{g+1}.png")
    sheet.save(out_path)
    with open(os.path.join(OUT, f"inbox_manifest_{g+1}.txt"), "w") as fh:
        fh.write("\n".join(manifest))
    manifest_all.extend(manifest)
    print(f"inbox_grid_{g+1}.png saved ({len(batch)} images)")

with open(os.path.join(OUT, "inbox_manifest_ALL.txt"), "w") as fh:
    fh.write("\n".join(manifest_all))
print(f"TOTAL: {len(files)} images, {num_grids} grids")
