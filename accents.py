"""Analyze saturated accent colors and calculate saturated pixel share."""
import sys
import os
import colorsys
from collections import Counter
from PIL import Image

def analyze_accents(image_path, min_sat=0.35, min_val=0.20):
    if not os.path.exists(image_path):
        print(f"Error: {image_path} not found")
        sys.exit(1)

    img = Image.open(image_path).convert("RGB")
    w, h = img.size
    # Sample down slightly for rapid analysis on huge screenshots
    if w * h > 500000:
        scale = (500000 / (w * h)) ** 0.5
        img = img.resize((int(w * scale), int(h * scale)))

    if hasattr(img, "get_flattened_data"):
        pixels = list(img.get_flattened_data())
    else:
        pixels = list(img.getdata())
    total_pixels = len(pixels)

    saturated = []
    for r, g, b in pixels:
        h_val, s_val, v_val = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
        if s_val >= min_sat and v_val >= min_val:
            # Quantize color slightly to group nearby shades
            qr = (r // 8) * 8
            qg = (g // 8) * 8
            qb = (b // 8) * 8
            hue_deg = int(h_val * 360)
            saturated.append((qr, qg, qb, hue_deg, round(s_val, 2), round(v_val, 2)))

    sat_share = (len(saturated) / total_pixels) * 100
    print(f"=== Accents for {os.path.basename(image_path)} ===")
    print(f"  Dimensions: {w}x{h}")
    print(f"  Saturated pixel share: {sat_share:.2f}%")

    if saturated:
        counts = Counter(saturated).most_common(8)
        sat_total = len(saturated)
        print("  Top saturated color clusters:")
        for (r, g, b, h_deg, s, v), count in counts:
            hex_code = f"#{r:02X}{g:02X}{b:02X}"
            pct = (count / sat_total) * 100
            print(f"    {hex_code}  {pct:5.1f}%  hue={h_deg:3d}°  sat={s:.2f}  val={v:.2f}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python accents.py <image_path>")
        sys.exit(1)
    analyze_accents(sys.argv[1])
