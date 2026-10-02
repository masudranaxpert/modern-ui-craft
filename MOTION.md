# MOTION.md — animation & micro-interaction discipline

Source: Emil Kowalski's design-engineering corpus (github.com/emilkowalski/skills,
adapted 2026-10-02) + Apple fluid-interface talks. Emil builds Sonner (13M+
weekly downloads), Vaul, Animata — this is production-proven, not taste.

Read this BEFORE writing any animation, transition, hover effect, or
micro-interaction in this project's UI builds. Pair with `SKILL.md` (anatomy)
— anatomy decides WHAT it looks like, this file decides HOW it moves.

## The Gate — run IN ORDER, before any motion code

### 1. Should this animate at all? (frequency)

| Frequency | Decision |
| --- | --- |
| 100+ times/day (keyboard shortcuts, ⌘K palette, tab switches) | **No animation. Ever.** Keyboard-initiated is a disqualifier, not a judgment call. |
| Tens of times/day (hover, list nav, row select) | Near-imperceptible only (<150ms) or nothing |
| Occasional (modals, drawers, toasts, settings) | Standard animation |
| Rare / first-time (onboarding, empty state, success) | The delight budget lives here — bounce/stagger allowed ONLY here |

### 2. Purpose — name it in one word, or don't build it

feedback / spatial consistency / state indication / preventing a jarring
change / explanation (marketing only) / delight (rare tier only).
"It looks cool" on a frequently-seen element = STOP. Function check: data
the user is READING or ACTING on must not move for style.

## Canonical curves — use these exact tokens, never hand-roll

```css
--ease-out: cubic-bezier(0.23, 1, 0.32, 1);     /* entrances, exits, UI */
--ease-in-out: cubic-bezier(0.77, 0, 0.175, 1); /* on-screen movement */
--ease-drawer: cubic-bezier(0.32, 0.72, 0, 1);  /* iOS drawer/sheet */
```

Decision order: entering/exiting → ease-out · moving on screen →
ease-in-out · hover/color → ease · constant motion (progress, marquee) →
linear. **Never `ease-in` on UI** — it starts slow, delaying the exact
moment the user watches most.

## Duration

| Element | Duration |
| --- | --- |
| Button press feedback | 100–160ms |
| Tooltips, small popovers | 125–200ms |
| Dropdowns, selects | 150–250ms |
| Modals, drawers | 200–500ms |

**UI stays under 300ms.** A 180ms dropdown feels more responsive than a
400ms one. ONE deliberate exception: a toast on an occasional surface can
run ~400ms `ease` (not ease-out) — Sonner reads as elegant partly because
its motion fits the component's personality.

## Never-Ship list (each is an automatic fix in review)

| Before | After | Why |
| --- | --- | --- |
| `transition: all 300ms` | `transition: transform 200ms var(--ease-out)` | `all` animates unintended props off-GPU |
| `scale(0)` entrance | `scale(0.95); opacity: 0` | Nothing in the real world appears from nothing |
| `ease-in` on a dropdown | `var(--ease-out)` | Delays the watched moment; sluggish |
| `transform-origin: center` on popover | origin at the TRIGGER | Panel grows out of the thing you clicked (modals exempt — they stay centered) |
| Animation on ⌘K / keyboard action | none | 100+/day; Raycast has no open animation — correct |
| 400ms UI toggle | 150–250ms | <300ms rule |
| Keyframes on toast/toggle | CSS transition | Transitions retarget mid-flight; keyframes restart from zero |
| Animating width/height/margin/padding | transform + opacity | GPU-only: transform, opacity, clip-path |
| Ungated `:hover` motion | `@media (hover:hover) and (pointer:fine)` | Touch fires false hovers on tap |
| Missing `prefers-reduced-motion` | gentler variant, not zero | Keep opacity/color, drop movement — ships WITH the animation |
| Everything entering at once | 30–80ms stagger | Group entrances; never block interaction during it |

## Recipes (copy-paste starting points)

**Button press** — any pressable; children scale with it, which is what
makes it read as physical:

```css
.button { transition: transform 160ms var(--ease-out); }
.button:active { transform: scale(0.97); }
```

**Popover / dropdown / menu** — grows out of its trigger:

```css
.popover {
  transform-origin: var(--transform-origin); /* Base UI supplies this */
  transition: opacity 200ms var(--ease-out), transform 200ms var(--ease-out);
}
.popover[data-starting-style], .popover[data-ending-style]
  { opacity: 0; transform: scale(0.95); }
```

**Tooltip** — fast, and the detail most miss: after the first tooltip,
neighbours open INSTANTLY (no delay, no animation):

```css
.tooltip[data-instant] { transition-duration: 0ms; }
```

**Modal** — the ONE that stays centered; backdrop animates with it as one
surface:

```css
.modal { transform-origin: center;
  transition: opacity 250ms var(--ease-out), transform 250ms var(--ease-out); }
.backdrop { transition: opacity 250ms var(--ease-out); }
```

**Toast** (soft-shell projects: bottom-center or top-center, translateY
percentages = own height):

```css
.toast { opacity: 1; transform: translateY(0);
  transition: opacity 400ms ease, transform 400ms ease;
  @starting-style { opacity: 0; transform: translateY(100%); } }
```

**Hold to confirm** (destructive actions) — slow where the user DECIDES,
snappy where the system RESPONDS:

```css
.overlay { clip-path: inset(0 100% 0 0);
  transition: clip-path 200ms var(--ease-out); }        /* release: fast */
.button:active .overlay { clip-path: inset(0 0 0 0);
  transition: clip-path 2s linear; }                    /* press: deliberate */
```

**Tab indicator color transition** — duplicate the tab list, style the copy
as active, clip to the active tab, animate the clip. One element revealed
beats two colors interpolated:

```css
.tabs-active-copy { clip-path: inset(0 60% 0 20%);   /* position of active */
  transition: clip-path 250ms var(--ease-in-out); }
```

**Stagger a group entrance** (occasional lists only; never all-day lists):

```css
.item { opacity: 0; transform: translateY(8px);
  animation: fadeIn 300ms var(--ease-out) forwards; }
.item:nth-child(2) { animation-delay: 50ms; }
.item:nth-child(3) { animation-delay: 100ms; }
@keyframes fadeIn { to { opacity: 1; transform: translateY(0); } }
```

**Scroll reveal** — marketing surfaces ONLY, fire once:

```css
.reveal { clip-path: inset(0 0 100% 0);
  transition: clip-path 600ms var(--ease-in-out); }
.reveal[data-visible] { clip-path: inset(0 0 0 0); }
```

## Springs & gestures (when a finger is involved)

Springs carry velocity through interruption; timing curves restart. If the
user can grab it mid-motion, it's a spring:

```js
{ type: "spring", duration: 0.5, bounce: 0.2 }  // Apple-style
```

- Bounce 0.1–0.3 max, and **only when the gesture carried momentum** —
  overshoot on a menu that faded in feels wrong; on a flicked card, right.
- Velocity-based dismissal: `Math.abs(distance) / elapsed > ~0.11` → dismiss
  on a flick regardless of distance.
- Rubber-band boundaries, never hard stops; drag tracks 1:1 respecting the
  grab offset; `setPointerCapture`; ignore extra touch points mid-drag.
- Exit the way it entered — toast in from bottom leaves through the bottom
  (symmetric paths make swipe-to-dismiss obvious).

## Accessibility (ships with the animation, never as follow-up)

```css
@media (prefers-reduced-motion: reduce) {
  .el { animation: fade 0.2s ease; }  /* opacity/color stay, movement drops */
}
@media (hover: hover) and (pointer: fine) {
  .card:hover { transform: translateY(-2px); }
}
```

Reduced motion = **fewer and gentler, NOT zero**.

## Feel-checks code can't decide

Slow-motion it (2–5× duration or DevTools animation inspector),
frame-by-frame for coordinated properties, real device for gestures,
fresh eyes the next day. When feel can't be judged from code, say so
instead of inventing a value.
