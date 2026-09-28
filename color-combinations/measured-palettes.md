# Measured palettes (real pixel data)

Source: `palette.py` (12-color quantized palette, % coverage) and `accents.py`
(hue/sat/val clusters over saturated pixels) run on a representative subset of 14
of the 48 reference images. Paths relative to repo root.

## Light web dashboards

### crm-pm-crestway-timeline.jpg — white + status-color system
- Neutrals: #FFFFFF 54%, #E0E0E0 20%, #F5F7F8, #EDF0F3 (cool grays)
- Accents (clusters): green #4EC430 / #51C238 (hue≈108), orange #FB9801 (hue 36,
  sat 1.0), purple #AF80FA (hue 264), blue #3B98FB (hue 210)
- Pattern: white canvas, muted gray chrome, 4 saturated status hues used as thin
  bars/tags — saturated pixel share only 1.6%.

### securevault-security-settings.jpg — corporate blue monochrome-accent
- Neutrals: blue-tinted off-whites #EDF4FD, #F4F8FE, #F8FAFE, border #C6D4E5
- Accent: single blue family, clusters #3079FB/#458EFA/#2670FB (hue 215–220,
  sat 0.6–0.85, val ~0.98). Green status words per manifest.
- Pattern: tinted (not gray) neutrals + ONE accent hue = calm enterprise look.

### support-analytics-yellow.jpg — yellow as brand accent on gray
- Neutrals: #F7F7F7 32%, #E2E2E2 32%, warm tint zones #F3EBCD
- Accents: yellow ramp #FDCB00 / #F3CE13 / #F1D339, tints #F7E791 (hue 48–54)
- Pattern: neutral gray UI, yellow reserved for chart series + highlight pills.

### revenuesidebar-tilted.jpg — white + red/amber data ink
- Neutrals: #FFFFFF 40%, #ECECEC 25%
- Accents: red #FB1711/#EE0000 (hue≈0), amber #EFBB50 (hue 40)
- Pattern: decorative mockup tilt; red used for chart emphasis only.

### invoicing-finance-overview.jpg — white + green/red finance duality
- Neutrals: #FFFFFF 38%, #DCDBDB 15%, muted sage chrome #C9D8D2, #537066
- Accents: green #01CF7C/#01AF64 (hue 154–159), blue #01A9FD + #0157BC, lime
  #98CC56; red for negative/Create CTA (manifest).
- Pattern: white + sage-tinted panels, semantic green/red for money in/out.

### crypto-analytics-bars-3scr.jpg — light multi-hue data app
- Neutrals: #F8F7F7, #F0F3F5, white cards, gray #5E5E5E bg frame
- Accents: periwinkle #646DE6 (hue 235), cyan #02ADFD, emerald #19BB83, orange
  #FE7703, red-pink #FB4D62 — one hue per data series.
- Pattern: near-white UI where ALL color is chart/data ink, none in chrome.

### careflow-healthcare-ops.jpg — cream + forest green
- Neutrals: cream #F0ECEA, white 32%, warm gray #C9C9C9, sage #C6CBB3,
  lime tint #F3F9CD (17% — the hero card wash)
- Accents: dark forest sidebar #3A4C2F/#304226/#2F452C (hue 86–112, sat ~0.4,
  val 0.26–0.31), lime #C7CF7C/#C6CD81 (hue 65)
- Pattern: dark-green sidebar + lime hero + cream body. Low-sat dark green, not
  pure black; lime carries the "attention" role.

### spend-against-plan-card.jpg — sage + forest line
- Neutrals: sage #DEE2D4 49%, near-white #F9FBF6
- Accents: single green ramp #005A39 → #146C4B → #65B498 (hue 156–160)
- Pattern: monochrome green ramp for the chart, sage canvas — one-hue harmony.

### databrain-realestate-analytics.jpg — dark green sidebar + lime accents
- Neutrals: white 45%+, gray #ECECEB, near-black green #042215 (12% sidebar)
- Accents: lime #A7DB25 ramp (hue 76–78, sat ~0.85, val ~0.86), navy #0C1C43
- Pattern: #042215 sidebar / white body / #A7DB22-ish lime highlights.

### aurora-task-manager (mobile/productivity) — pastel wash + olive-lime
- Neutrals: #C2C2C2 frame, #FAFAFA/#F7F6F5 screens, pastel mint/peach washes
  #DFE7DF, #A9CDBA, #C2D2D1
- Accents: olive-lime #85A63B, gold #C4AD4F, mustard #B0AC46 (hues 44–78,
  sat ~0.6) — muted pastel saturation, plus black active tabs + lime FAB.

## Dark mobile

### body-readiness-dark-2scr.jpg — near-black + teal glow
- Neutrals: #0E191A, #060707, #0F0F10 (stack of near-blacks), light #F1F3F2
- Accents: teal ramp #02454F → #034F5A → #035965 (hue 182–188, sat 0.54–0.97),
  muted mid-teal #2F6367, glow #6D8A8C
- Pattern: layered near-black greens, single teal family at two saturation
  levels (deep fill + glow edge). Saturated share only 3.4% — glow, not paint.

## Mobile brand-color apps

### floriva-flower-shop-3scr.jpg — magenta brand
- Neutrals: #EEE4EB, #FBF0F3, white, blush tints
- Accent: magenta ramp #C64073 → #D85185 → #D37097 (hue 336–337, sat 0.47–0.68,
  val ~0.8), deep #A53C5C for depth. Saturated share 26.2% — highest of the set;
  brand color used full-bleed.
- Black pill CTAs per manifest.

### breet-wallet-teal-3scr.jpg — teal gradient wallet
- Neutrals: white 32%, photo grays #BACACD, dark photo greens
- Accent: cyan-teal #05A0BB dominant (hue 188, sat 0.97, val 0.73), deep
  #037B90 for gradient stops. Saturated share 25.7%.
- Pattern: one loud brand hue at high saturation, gradient to a darker stop.

## Monochrome control

### torin-settings-monochrome.jpg — zero-color
- #D4D4D4 65%, #EDEDEB, #FFFFFF, #8D8D8C; accents.py: **no saturated pixels**.
- Pure grayscale + black toggles. Baseline for "how far every other app deviates".

---

## Cross-cutting measurements

- Light UIs sit on 4 neutral tiers: canvas white/near-white, panel tint (warm or
  hue-tinted, e.g. #EDF4FD, #DEE2D4, #F0ECEA), border gray #C6C9CF–#E0E0E0, and
  ink/near-black.
- Saturated pixel share is tiny in dashboards (0.5–4%) and large only in
  brand-forward mobile apps (25%+).
- Dark UIs never use #000: measured floors are #060707–#101418, usually with a
  hue cast (teal #0E191A, green #042215).
- Accent ramps are single-hue (5–8 lightness steps of one hue: teal, magenta,
  forest, lime) rather than many hues; multi-hue appears only as data-series ink.
