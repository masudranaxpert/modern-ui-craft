"""Audit + repair all category READMEs: dedupe rows, sync counts with jpgs on disk."""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
GAL = os.path.join(BASE, "gallery")
ALSO = os.path.join(BASE, "_rejected_inbox")

def slug_of(row):
    m = re.search(r"`([^`]+\.jpg)`", row)
    return m.group(1) if m else None

def repair(cat_dir):
    rd = os.path.join(cat_dir, "README.md")
    if not os.path.exists(rd):
        return f"{cat_dir}: NO README"
    jpgs = sorted(f for f in os.listdir(cat_dir) if f.endswith(".jpg"))
    lines = open(rd).read().splitlines()
    table_idx = next(i for i, l in enumerate(lines) if l.startswith("| #"))
    head, rows = lines[:table_idx + 2], []  # +2 keeps header + separator
    for l in lines[table_idx + 2:]:
        if l.startswith("|"):
            rows.append(l)
    seen, uniq, missing = set(), [], []
    for r in rows:
        s = slug_of(r)
        if s in seen:
            continue
        seen.add(s)
        uniq.append(r)
    row_slugs = {slug_of(r) for r in uniq}
    missing = [j for j in jpgs if j not in row_slugs]
    extra = [s for s in row_slugs if s not in jpgs]
    count_line = f"**Screens:** {len(jpgs)}  "
    new_head = [count_line if re.match(r"\*\*Screens:\*\*", h) else h for h in head]
    out = "\n".join(new_head + uniq + missing_grace(missing)) + "\n"
    open(rd, "w").write(out)
    status = f"{len(rows)} rows -> {len(uniq)} uniq, jpgs {len(jpgs)}, count fixed"
    if missing:
        status += f", MISSING ROWS: {missing}"
    if extra:
        status += f", STALE ROWS: {extra}"
    return f"{os.path.relpath(cat_dir, BASE)}: {status}"

def missing_grace(missing):
    return [f"| ? | `{m}` | (row missing — add manually) | | |" for m in missing]

folders = []
for root, dirs, _ in os.walk(GAL):
    for d in dirs:
        p = os.path.join(root, d)
        if os.path.exists(os.path.join(p, "README.md")):
            folders.append(p)
folders.append(ALSO)
folders.sort()
for f in folders:
    print(repair(f))
