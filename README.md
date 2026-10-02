# Modern UI Craft 🎨

**A curated reference gallery + design skill for building 2026-grade interfaces — dashboards, landing pages, and mobile apps that look premium on the first try.**

Born from a real failure: an AI agent shipped a "correct but backdated" dashboard despite following all the abstract rules. This repo is the fix — **105 hand-curated reference screenshots** (48 curated 2026-09-28 + 57 organized from the 2026-09-30 inbox drop) from real products, deconstructed into reusable anatomy patterns, measured color systems, and a deterministic skill any AI agent (or human) can follow.

## What's inside

```
├── SKILL.md                  ← the skill: workflow + hard rules (C/S/T/I codes)
├── MOTION.md                 ← animation discipline (Emil Kowalski): the Gate,
│                                curves, durations, never-ship list, recipes
├── inbox/                    ← staging: drop new raw screenshots here for AI to organize
├── gallery/
│   ├── web/
│   │   ├── dashboard/        ← 41 dashboard references + README.md
│   │   ├── landing/          ← landing pages + README.md
│   │   └── settings/         ← settings screens + README.md
│   ├── mobile/
│   │   ├── finance/          ← wallets, exchanges, payouts + README.md
│   │   ├── fitness/          ← dark glass + gamified trackers + README.md
│   │   ├── health/           ← telehealth, wellness, medication + README.md
│   │   ├── social/           ← leaderboards, group sheets + README.md
│   │   ├── productivity/     ← task managers, calendars, AI assistants + README.md
│   │   ├── education/        ← e-learning + README.md
│   │   ├── ecommerce/        ← shop apps + README.md
│   │   ├── settings/         ← monochrome settings + README.md
│   │   ├── onboarding/       ← illustrated flows + README.md
│   │   └── utility/          ← prayer times, widgets + README.md
│   ├── components/           ← component-level refs: cards, pills, gauges, feeds
│   └── techniques/           ← concrete how-to rules (radius, specs, wireframes)
├── color-combinations/       ← measured hex pairings with usage notes
└── RESEARCH.md               ← cross-cutting analysis of the curated references

Local-only (gitignored): `inbox/` staging drops, `_grids/` contact sheets,
`_rejected_inbox/` provenance, one-off organize scripts.
```

## The core idea

> You are never the first person to design this screen. Find the closest
> reference, name it, and imitate its **anatomy** before writing CSS.

Every image in the gallery was selected because it passes the "premium feel" bar — soft-shell cards, pill navigation, rationed accent color, one hero per screen. The skill turns that taste into checklists: **C**olor, **S**tructure, **T**ypography, **I**nteraction rules, plus an anti-slop checklist.

## Quick start (for AI agents)

1. Read `SKILL.md` (anatomy) — and `MOTION.md` (motion) if the build has
   any animation, transition, hover, or micro-interaction (real UIs always do)
2. Classify your job (what + where + who judges)
3. Open the closest `gallery/` folder, read its `README.md`
4. Write a 3-line design contract naming your reference
5. Build → screenshot at 1280px + 390px → critique like a designer
6. Run the `MOTION.md` Never-Ship list on every animation you wrote
7. Ship only when your screenshot wouldn't look out of place in the gallery

## Highlights from the rules

- **C2**: accent color ≤2% of pixels — whitespace carries the layout
- **S1**: soft-shell anatomy — structure reads through elevation, not borders
- **S2**: pill everything; sharp rectangles read dated
- **C4**: state colors always paired with a word (8% of men are colorblind)
- **T1**: tabular numerals for every metric; body ≥16px

See `SKILL.md` for all 20+ rules with rationale.

## Why a gallery instead of abstract rules?

Abstract rules produce correct-but-dated UIs. Real references carry **tacit** knowledge — exactly how much shadow, exactly where the hero sits, exactly how loud the accent is — that rules can't encode. Pairing both (references for anatomy, rules for discipline) is what makes outputs feel designed rather than generated.

## License & credits

Reference screenshots are collected for educational/research purposes and belong to their respective products. Everything else (skill, analysis, docs): MIT.
