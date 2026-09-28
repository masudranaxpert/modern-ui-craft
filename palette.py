"""Extract 12-color quantized palette with percentage coverage from an image."""
import sys
import os
from PIL import Image

def analyze_palette(image_path, num_colors=12):
    if not os.path.exists(image_path):
        print(f"Error: {image_path} not found")
        sys.exit(1)

    img = Image.open(image_path).convert("RGB")
    # Small resize to accelerate quantization while preserving ratio
    img_small = img.resize((320, int(320 * img.height / img.width)))
    q = img_small.quantize(colors=num_colors, method=Image.Quantize.MEDIANCUT)
    palette = q.getpalette()[:num_colors * 3]
    counts = sorted(q.getcolors(), reverse=True)
    total = sum(c[0] for c in counts)

    print(f"=== Palette for {os.path.basename(image_path)} ===")
    for count, idx in counts:
        r, g, b = palette[idx * 3:idx * 3 + 3]
        hex_code = f"#{r:02X}{g:02X}{b:02X}"
        pct = (count / total) * 100
        print(f"  {hex_code}  {pct:5.1f}%")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python palette.py <image_path>")
        sys.exit(1)
    analyze_palette(sys.argv[1])
