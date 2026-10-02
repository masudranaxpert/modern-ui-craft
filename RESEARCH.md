# Cross-cutting research — what 48 modern UIs share

Analysis across the initial 48 gallery references (27 web dashboards, 3
landing/marketing, 18 mobile app screens) collected 2026-09-28. Gallery
expanded to 105 references on 2026-09-30 (14 new dashboards, 11 mobile
health, plus components/techniques folders) — every claim below held on
spot-check of the new set; full re-analysis pending. Every claim below is
backed by the majority of references, not vibes.

## 1. The shell → cards anatomy dominates (43/48)

The single most consistent structure: a tinted page background (gray, cream,
or sage — almost never pure white) with white rounded cards floating on it.
Separation comes from elevation (soft double shadows) in 80%+ of references;
hard 1px borders appear only in dense data tables.

Shell colors observed: `#F6F7F9`, `#F0F2F6`, `#FAF7F0`, `#F2F4EE`, `#ECECEC`.
Card radius: 16-20px everywhere; pills 999px.

## 2. Accent color is rationed like money (all 48)

Measured saturated-pixel share across references: **0.0%–4.9%**, with the
majority under 2%. The rejected anti-model (multi-hue noise at 4.9%) is the
outlier that proves the rule. Premium feel correlates with restraint:
- Interactive elements (links, active tabs, CTAs) own ONE hue family
- Data ink (chart series) may add 1-2 semantic hues (green=positive,
  red=negative) within a fixed sat/val band
- Red/orange is universally rationed to alerts/destructive — never decoration
- Settings screens hit 0.0% — zero accent, hierarchy purely typographic

## 3. The dark-anchor trick (light themes)

Light UIs carry weight through near-black elements: the primary CTA pill, the
active nav pill, avatar tiles, sometimes a whole hero card. Black IS the
accent. This lets the hue accent stay tiny and loud. Appears in 18+ light
references (black "Book appointment", "Export Data", "Get Started" pills).

## 4. Dark themes band by value, not hue (7 references)

Disciplined dark UIs (agent-observability family, fitness trackers) don't add
hues for hierarchy — they tier ONE accent by value: full-sat signal color →
mid-tone → deep desaturated surface tint. Extended data (sparklines,
hatched bars) goes gray. Chrome sits at #0C0C0C–#111418, never #000.

## 5. Pills are the 2026 signature (39/48)

Navigation, filters, chips, CTAs, time-range selectors — pills everywhere.
Active states are SOLID pills (black, dark-green, or accent); inactive are
ghost/outline. Sharp rectangles survive only inside dense tables. Floating
pill tab bars (detached from screen edge, soft shadow, blur backdrop) are
the mobile signature.

## 6. One hero per screen (all 48)

Every reference has exactly one dominant element: a gradient balance card
(fintech), a pastel at-risk panel (healthcare), a big metric (fitness), a
display headline (landing). Everything else is visibly quieter. Screens that
break this read as noisy dashboards.

## 7. KPI stat trio / quartet as dashboard opener (18/18 dashboards)

Web dashboards open with 3-4 stat cards (value + label + delta + sparkline),
then one hero chart, then detail tables/lists. This rhythm is so consistent
it can be treated as a law: **stats → hero chart → details**.

## 8. Mobile reflow, not redesign (5 responsive pairs)

The same product on mobile: sidebar → floating pill tab bar (3-5 labeled
icons), KPI 4-up → 2×2, filter rows → stacked sheets, tables → cards.
Components, accent, and chart language stay identical.

## 9. Typography: big tabular numbers, sentence case (all 48)

Metrics: 32-56px, weight 700-800, letter-spacing ≈ -0.02em, tabular
numerals (mono fonts for IDs/durations in technical UIs). Labels: sentence
case 12.5-14px; ALL-CAPS only for tiny eyebrows. Body ≥16px, ≥1.5
line-height.

## 10. Motion discipline

Press feedback scale(0.95-0.97) @160ms, transitions 150-300ms with strong
custom curves (`cubic-bezier(0.23,1,0.32,1)` ease-out), hover-guards for
touch, reduced-motion variants ship with the animation. Nothing bounces
except momentum gestures. The premium feel comes from restraint — no
entrance animation circus. Frequency gate: screens used 100+ times/day get
NO animation at all (keyboard, palette toggles). Full discipline lives in
`MOTION.md` (Emil Kowalski corpus + Apple fluid interfaces, adopted
2026-10-02).

## Trend signals (late 2026)

- Purple-gradient-everything era is over; pastel washes (purple, sky, mint,
  sage) as atmosphere below full saturation are in
- Serif/display headlines entering fintech landings; geometric sans bodies
- Dark-glass fitness/social UIs + light soft-shell productivity UIs are the
  two dominant mobile moods
- Command-K palettes with natural-language → filter-chip parsing appearing
  in pro tools
- AI-era tells to avoid: gradient-on-everything, stacked glassmorphism,
  emoji icons, rounded-everything

## What this means for generation

Copy anatomy first (shell → cards → nav → hero rhythm), ration color like a
budget, keep one hero, use pills, band dark themes by value, and screenshot-
compare against a reference before calling it done. Full rules: `SKILL.md`.
