# Color combination systems

Derived from measured palettes (see `measured-palettes.md`) + `_grids/manifest_1..8.txt`
estimates for the 48 reference images. Measured values come from ~14 representative
images spanning light/dark, web/mobile.

---

## 1. White canvas + status-hue system (enterprise dashboards)

**Seen in:** Crestway, HubSpot-like marketing analytics, CRM analytics (#1, #2, #8)
**Measured:** #FFFFFF 54% / #E0E0E0 20% chrome; accents green #4EC430, orange #FB9801,
purple #AF80FA, blue #3B98FB. Saturated share 1.6%.

```yaml
canvas: "#FFFFFF"
surface: "#F5F7F8"
border: "#E0E0E0"
ink: "#1A1D21"
status-green: "#4EC430"
status-orange: "#FB9801"
status-purple: "#AF80FA"
status-blue: "#3B98FB"
```

**Rule:** color is metadata, not decoration — ≤2% of pixels saturated, each hue maps
to a state (on-track / at-risk / review / info). Chrome stays pure gray.

## 2. Tinted-neutral + single corporate hue

**Seen in:** SecureVault (#32), MailVista (#27)
**Measured:** off-whites #EDF4FD / #F4F8FE / #F8FAFE, border #C6D4E5, accent blue
#3079FB→#599AFA (hue 215–220). Saturated share 0.8%.

```yaml
canvas: "#F4F8FE"
surface: "#FFFFFF"
border: "#C6D4E5"
ink: "#12233F"
primary: "#2F6FED"
primary-hover: "#2670FB"
success: "#1F9D55"
```

**Rule:** neutrals carry a whisper of the brand hue (blue-tinted grays); one accent
does all the work. Calmest enterprise pattern in the set.

## 3. Cream + forest green + lime (organic ops)

**Seen in:** Careflow (#5), Databrain (#18), SakanBeasa (#38)
**Measured:** cream #F0ECEA, lime wash #F3F9CD (17%), sidebar forest #304226/#3A4C2F
(hue 86–112, sat 0.4), lime accent #C7CF7C / #A7DB25, deep floor #042215.

```yaml
canvas: "#F4F4EF"
surface: "#FFFFFF"
sidebar: "#2F452C"        # low-sat forest, not black
hero-wash: "#F3F9CD"
accent-lime: "#A7DB25"
accent-soft-lime: "#C7CF7C"
ink: "#1C2418"
```

**Rule:** dark green sidebar replaces the usual near-black rail; lime is the only
loud color and marks "needs attention" hero cards. Warm neutrals throughout.

## 4. Sage canvas + single-hue green ramp

**Seen in:** Spend analytics card (#13), Wiseproedit (#39)
**Measured:** sage #DEE2D4 49%, chart green ramp #005A39 → #146C4B → #65B498
(hue 156–160).

```yaml
canvas: "#DEE2D4"
surface: "#F9FBF6"
chart-1: "#005A39"
chart-2: "#146C4B"
chart-3: "#457D67"
chart-4: "#65B498"
ink: "#22291F"
```

**Rule:** a 4-step lightness ramp of ONE hue encodes series order — no legend colors
needed. The sage canvas itself is a desaturated step of the same hue.

## 5. Near-black + single glow hue (dark mobile)

**Seen in:** body readiness (#7), fitness week metrics (#22), Waley Pro paywall (#19),
Vantage traces/tables (#33, #35–37)
**Measured:** bg stack #060707/#0E191A/#0F0F10/#101418; teal ramp #02454F→#034F5A
(hue 187, sat 0.97) + muted #2F6367 + glow edge #6D8A8C. Saturated share 3.4%.
Vantage variant: near-black #0E1210 + mint green signal.

```yaml
bg-0: "#060707"
bg-1: "#0E191A"
bg-2: "#203B3D"        # raised card / glass
ink: "#F1F3F2"
glow-deep: "#02454F"
glow-core: "#035965"
glow-edge: "#6D8A8C"
```

**Rule:** never #000 — layered near-blacks with a hue cast (teal or green). The
accent exists as a *glow*: deep saturated fill + desaturated rim, not flat paint.
Text/structure stays monochrome.

## 6. Full-bleed brand hue + black pill CTA (consumer mobile)

**Seen in:** Floriva (#3), Breet (#6), crypto wallets (#12, #16)
**Measured:** Floriva magenta #C64073 (hue 336, sat 0.68, val 0.8) at 26% pixel share,
tints #EFD6E5/#EEE4EB; Breet cyan #05A0BB (hue 188, sat 0.97, val 0.73) at 26%,
gradient stop #037B90.

```yaml
brand: "#C64073"       # or #05A0BB
brand-deep: "#A53C5C"  # or #037B90
brand-tint: "#FDF0F4"  # or #E0F5F8
canvas: "#FFFFFF"
cta: "#000000"         # black pill — deliberately not brand color
ink: "#111111"
```

**Rule:** one loud hue owns hero/screens (25%+ pixel share), a darker stop makes the
gradient, pale tints replace gray surfaces, and the primary CTA is a *black* pill so
it never fights the brand color.

## 7. White + multi-hue data ink (finance/crypto apps)

**Seen in:** crypto analytics (#29), invoicing (#45), crypto wallet 4-screen (#28)
**Measured:** neutrals #F6F7F9/#FFFFFF; series hues #646DE6, #02ADFD, #19BB83,
#FE7703, #FB4D62; finance green #01CF7C vs red accents.

```yaml
canvas: "#F6F7F9"
surface: "#FFFFFF"
series-1: "#646DE6"
series-2: "#02ADFD"
series-3: "#19BB83"
series-4: "#FE7703"
negative: "#FB4D62"
positive: "#01CF7C"
ink: "#17181C"
```

**Rule:** chrome is colorless; every saturated pixel belongs to a data series. Hues
are spread around the wheel (235°, 199°, 159°, 27°, 351°) for separability, and
green/red are reserved for semantic up/down.

## 8. Gray + single warm accent (support/media brands)

**Seen in:** support analytics yellow (#34), Sephia courses (#43), revenue sidebar (#44)
**Measured:** #F7F7F7/#E2E2E2 neutrals, yellow ramp #FDCB00→#F3CE13→#F7E791 (hue 48–54),
warm tint zone #F3EBCD; Sephia cream #FAF6EF + amber accents.

```yaml
canvas: "#F7F7F7"
surface: "#FFFFFF"
border: "#E2E2E2"
accent: "#F3CE13"
accent-soft: "#F7E791"
accent-wash: "#F3EBCD"
ink: "#191919"
```

**Rule:** pure gray UI + one warm hue (yellow/amber) for highlights, chart series and
chip fills; a warm-tinted wash zone (not gray) marks the hero area.

## 9. Pastel wash + black structure (soft consumer)

**Seen in:** task manager aurora (#40), Sapick landing (#11), medspa profile (#15),
habit tracker (#31)
**Measured:** pastel washes #DFE7DF/#A9CDBA/#C2D2D1, muted olive-gold accents
#85A63B/#C4AD4F (sat ~0.6), black active tabs/FAB, white cards.

```yaml
canvas: "#FDFDFD"
wash-a: "#DFE7DF"   # mint
wash-b: "#F7E8DC"   # peach
card: "#FFFFFF"
active: "#000000"
fab: "#B5E048"
muted-accent: "#85A63B"
gold: "#C4AD4F"
```

**Rule:** color lives in background gradients and illustration strokes at sat ≤0.6;
structure (active tab, CTA) is pure black for contrast against the softness.

## 10. Zero-color monochrome (control case)

**Seen in:** Torin settings (#46), plus black-CTA elements in #11, #16, #17, #20, #31
**Measured:** #D4D4D4 65% / #EDEDEB / #FFFFFF / #8D8D8C; **no saturated pixels**.

```yaml
bg: "#EDEDEB"
group: "#FFFFFF"
border: "#D4D4D4"
ink: "#111111"
secondary-ink: "#8D8D8C"
```

**Rule:** hierarchy via gray steps and weight only. Appears standalone for utility
screens and as the "structure layer" of every black-pill pattern above.

---

## How to choose (from the corpus)

| Context | Pattern | Example |
|---|---|---|
| Enterprise dashboard, status-heavy | 1 or 2 | Crestway, SecureVault |
| Ops dashboard, brand personality | 3 | Careflow, Databrain |
| Single-chart card / calm finance | 4 | Spend card |
| Dark consumer or dev-tool UI | 5 | Body readiness, Vantage |
| Consumer mobile, brand-led | 6 | Floriva, Breet |
| Portfolio/multi-series data | 7 | Crypto analytics |
| Support/media, one warm brand hue | 8 | Support analytics |
| Soft consumer, task/lifestyle | 9 | Aurora tasks |
| Utility/settings | 10 | Torin |

Universal invariants across all 48 refs:
1. Saturated pixels ≤4% in dashboards, ≥25% only in brand-led mobile heroes.
2. Dark backgrounds are never #000 (measured #060707–#101418, hue-cast).
3. Accent usage is single-hue ramps; multi-hue appears only as data-series ink.
4. Neutral surfaces are often hue-tinted (blue #F4F8FE, sage #DEE2D4, cream #F4F4EF),
   rarely pure #EEE gray except in the gray+accent pattern (#8).
5. Primary CTAs: black pill (consumer), brand blue (#2F6FED-class, corporate),
   or gradient of the brand hue (fintech) — never a second unrelated hue.
