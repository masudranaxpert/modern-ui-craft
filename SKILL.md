---
name: modern-ui-craft
version: 1.1.0
description: Use when building any modern web or mobile UI — copy proven 2026
  design anatomy (soft-shell cards, pill nav, pastel heroes) from a curated
  reference gallery instead of inventing a look. Turns "make it modern and
  beautiful" into a deterministic checklist with measured color systems,
  per-app-type patterns, and hard anti-slop rules distilled from 105 real
  product screenshots.
metadata:
  tags: [ui, ux, design, dashboard, mobile, color, 2026]
---

# Modern UI Craft — build 2026-grade interfaces on the first try

The failure this skill prevents: an agent reads abstract rules (contrast,
spacing), ships a "correct" but dated-looking UI, and the user says
*"why does it look backdated?"*. Fix: **anatomy-first** — pick a proven
reference layout from `gallery/`, copy its structure, then fill with content.

## The one rule

> You are never the first person to design this screen. Find the closest
> reference in `gallery/`, name it in your design contract, and imitate its
> anatomy before writing a single line of CSS.

## Workflow

### 0. Classify the job
Answer before designing:
- **What** is it? dashboard / landing / settings / mobile app (finance,
  fitness, social, productivity, e-commerce, education) / utility
- **Where**? web-desktop / mobile / both (responsive)
- **Who** judges it? end users (delight matters) vs internal ops (clarity)

### 1. Pick your anatomy from the gallery
`gallery/` is organized by platform + app type. Each folder has a
`README.md` describing every reference image's layout skeleton and the
patterns that make it feel premium. Read the one closest to your job.
Non-negotiable starting points per type (full details in the folder):

| You're building | Start from | Core anatomy |
|---|---|---|
| Web dashboard | `gallery/web/dashboard/` | light-gray shell → floating white cards, dark icon sidebar OR none, KPI stat trio, one hero chart |
| Landing page | `gallery/web/landing/` | pastel gradient hero, huge display headline, floating product cards, black pill CTA, logo strip |
| Mobile finance | `gallery/mobile/finance/` | gradient balance hero → white body, icon quick-action grid, tx list, black pill CTA |
| Mobile fitness/social | `gallery/mobile/fitness/`, `gallery/mobile/social/` | dark glass or pastel aurora, big metric hero, bottom tab bar |
| Settings | `gallery/web/settings/`, `gallery/mobile/settings/` | monochrome, grouped rows, toggles carry all interaction, ZERO accent color |

### 2. Write a 3-line design contract (in your reply, not a file)
```
Build: [screen] — anatomy from [reference filename]
Theme: [light/dark] shell [hex] + accent [hex] (+ state hues)
Patterns: [pattern 1] + [pattern 2] + [pattern 3]
```
If you cannot name a reference, you have not looked hard enough.

### 3. Apply the hard rules (they override taste)

**Color**
- C1 — ONE accent hue family owns interactive elements. All accents within
  ~Δ5° hue unless a hue is semantically OWNED (success green, error red,
  per-category pastels).
- C2 — Accent coverage ≤2% of pixels; charts may push total to ~4%.
  Whitespace and neutrals carry the layout.
- C3 — Neutral temperature matches accent temperature: warm accent → cream
  shell (#FAF7F0), cool accent → cool gray shell (#F0F2F6). Sage/green →
  warm-neutral (#F2F4EE).
- C4 — State colors pair with a WORD, never color alone (8% of men are
  colorblind). Status = pastel pill + dark text of same hue.
- C5 — Semantic hues stay in one sat/val band per role. Red/orange rationed
  to alerts/destructive only.
- C6 — Settings/utility screens: zero accent. The calmer the job, the less
  color.
- Use `color-combinations/` for measured, proven pairings.

**Structure**
- S1 — Soft-shell: light gray page → white cards (radius 16-20px) floating
  on soft diffuse shadows (`0 2px 6px + 0 12px 32px`), no hard borders.
  Structure reads through elevation.
- S2 — Pill everything: nav tabs, filters, chips, CTAs = pills. Active tab =
  solid pill (dark or accent). Primary CTA = full-width black pill on light,
  white pill on dark. Sharp rectangles read dated.
- S3 — One hero per screen: the biggest loudest element (pastel wash card,
  gradient balance, metric) is THE hero; everything else quieter.
- S4 — Responsive = reflow, not redesign: mobile re-stacks (KPIs 2×2,
  sidebar → bottom pill tab bar, 3-5 labeled icons), same components.
- S5 — Labels are verbs ("Export CSV", "Review the 12"). One primary button
  per view.

**Typography**
- T1 — Body ≥16px, secondary ≥12.5px, 12px absolute floor. Tabular numerals
  (mono or font-variant-numeric) for every metric/id/timestamp.
- T2 — Big numbers: 32-56px, weight 700-800, letter-spacing -0.02em.
  Sentence case labels, ALL-CAPS only for tiny eyebrows (12px, 0.07em max).
- T3 — Line-height ≥1.5 body (1.6 for Bangla), 50-75 chars/line.

**Interaction**
- I1 — Touch targets ≥44px (mobile), ≥40px desktop buttons; 8px spacing.
- I2 — Motion (full discipline: Hermes `uiux-engineer` skill →
  `references/motion-animation.md`): run the Gate first — frequency
  (keyboard/100+-per-day = NO animation; occasional = standard; rare =
  delight budget) → purpose (feedback / spatial consistency / state
  indication / jarring-change bridge; "looks cool" is not a purpose).
  150-300ms, canonical curves `--ease-out: cubic-bezier(0.23,1,0.32,1)`,
  `--ease-in-out: cubic-bezier(0.77,0,0.175,1)`; never `ease-in` on UI.
  Press feedback scale(0.97), transition transform 160ms. Entrances from
  scale(0.95)+opacity(0), never scale(0). Only transform/opacity/clip-path
  animate. `prefers-reduced-motion` = gentler variant (opacity/color stay,
  movement drops) ships WITH every animation. Hover styles guarded by
  `@media(hover:hover) and (pointer:fine)`.
- I3 — Toasts: ONE at a time, non-blocking, replace alert(); actionable
  toasts never auto-dismiss. Toast personality exception: ~400ms `ease`
  (not ease-out) reads elegant on occasional surfaces (Sonner).
- I4 — Loading: skeleton screens for layout stability (CLS), spinners only
  for sub-second waits.
- I5 — Every entity shows its state inline (pill+word, meter, delta) without
  clicks.

**Anti-slop checklist (run before shipping)**
- [ ] No gradients on everything (gradient budget: ONE hero element max)
- [ ] No glassmorphism cards stacked on glassmorphism cards
- [ ] No emoji as icons (use a consistent stroke SVG set)
- [ ] Not everything is rounded 24px+ (radius system: 20/14/999)
- [ ] ≤2 typefaces, ≤3 weights, no letter-spaced body text
- [ ] Charts: max 2 accent series + gray for extended data
- [ ] No dev jargon visible (IDs, source enums, "Not Installed" plumbing)
- [ ] Screenshot test: would this sit unnoticed inside the gallery folder?

### 4. Verify like a designer, not an engineer
Technical checks (contrast, overflow, tests passing) are necessary but NOT
design verification. After building:
1. Screenshot at desktop (1280) + mobile (390) widths.
2. Compare side-by-side against the gallery reference you named.
3. Critique: hierarchy (one hero?), breathing (spacing ≥16px between cards),
   color discipline (≤2% accent), and honesty (any dev/debug text visible?).
4. Iterate until the screenshot would not look out of place in `gallery/`.

## Folder guide
- `gallery/web/` + `gallery/mobile/` — 105 curated reference screenshots,
  semantic filenames, grouped by app type (plus `components/` for
  component-level refs and `techniques/` for concrete how-to cards)
- `gallery/**/README.md` — per-folder breakdown of every image
- `color-combinations/` — measured hex pairings from the references with
  usage notes
- `RESEARCH.md` — cross-cutting analysis: what all modern UIs share,
  where trends are heading

## Honest limits
- Gallery reflects late-2026 taste; palettes decay ~18 months. Re-verify
  against fresh references after mid-2028.
- Rules are floors and defaults from real products, not guarantees — a
  specific brand can justify breaking them, but break deliberately and
  note why.
- The gallery is curated (user-verified "looks premium"); new additions
  should be measured with the same bar.
