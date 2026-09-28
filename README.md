# Modern UI Craft 🎨

**A curated reference gallery + design skill for building 2026-grade interfaces — dashboards, landing pages, and mobile apps that look premium on the first try.**

Born from a real failure: an AI agent shipped a "correct but backdated" dashboard despite following all the abstract rules. This repo is the fix — **48 hand-curated reference screenshots** from real products, deconstructed into reusable anatomy patterns, measured color systems, and a deterministic skill any AI agent (or human) can follow.

## What's inside

```
├── SKILL.md                  ← the skill: workflow + hard rules (C/S/T/I codes)
├── Galary/                   ← inbox: drop new raw screenshots here for AI to organize
├── gallery/
│   ├── web/
│   │   ├── dashboard/        ← 27 dashboard references + README.md
│   │   ├── landing/          ← landing pages + README.md
│   │   └── settings/         ← settings screens + README.md
│   └── mobile/
│       ├── finance/          ← wallets, exchanges, payouts + README.md
│       ├── fitness/          ← dark glass trackers + README.md
│       ├── social/           ← leaderboards, group sheets + README.md
│       ├── productivity/     ← task managers + README.md
│       ├── education/        ← e-learning + README.md
│       ├── ecommerce/        ← shop apps + README.md
│       ├── settings/         ← monochrome settings + README.md
│       ├── onboarding/       ← illustrated flows + README.md
│       └── utility/          ← widget packs + README.md
├── color-combinations/       ← measured hex pairings with usage notes
└── RESEARCH.md               ← cross-cutting analysis of all 48 references
```

## The core idea

> You are never the first person to design this screen. Find the closest
> reference, name it, and imitate its **anatomy** before writing CSS.

Every image in the gallery was selected because it passes the "premium feel" bar — soft-shell cards, pill navigation, rationed accent color, one hero per screen. The skill turns that taste into checklists: **C**olor, **S**tructure, **T**ypography, **I**nteraction rules, plus an anti-slop checklist.

## Quick start (for AI agents)

1. Read `SKILL.md`
2. Classify your job (what + where + who judges)
3. Open the closest `gallery/` folder, read its `README.md`
4. Write a 3-line design contract naming your reference
5. Build → screenshot at 1280px + 390px → critique like a designer
6. Ship only when your screenshot wouldn't look out of place in the gallery

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
