"""Build contact-sheet grids from gallery images."""
import os
from PIL import Image, ImageDraw

BASE = os.path.dirname(os.path.abspath(__file__))
GALLERY = os.path.join(BASE, "gallery")
OUT = os.path.join(BASE, "_grids")
os.makedirs(OUT, exist_ok=True)

# Collect all images from gallery/
files = []
for root, _, filenames in os.walk(GALLERY):
    for f in filenames:
        if f.lower().endswith((".jpg", ".jpeg", ".png")):
            files.append(os.path.join(root, f))

files.sort()
TW, TH = 560, 420
COLS, ROWS = 2, 3

batch_size = COLS * ROWS
num_grids = (len(files) + batch_size - 1) // batch_size

for g in range(num_grids):
    batch = files[g * batch_size:(g + 1) * batch_size]
    if not batch:
        break
    sheet = Image.new("RGB", (COLS * TW, ROWS * (TH + 26)), "#dddddd")
    d = ImageDraw.Draw(sheet)
    for i, path in enumerate(batch):
        name = os.path.splitext(os.path.basename(path))[0]
        img = Image.open(path).convert("RGB")
        img.thumbnail((TW - 8, TH - 8))
        x = (i % COLS) * TW
        y = (i // COLS) * (TH + 26)
        sheet.paste(img, (x + 4, y + 4))
        d.text((x + 8, y + TH + 4), name[:35], fill="black")
    out_path = os.path.join(OUT, f"grid_{g+1}.png")
    sheet.save(out_path)
    print(f"grid_{g+1}.png saved ({len(batch)} images)")
