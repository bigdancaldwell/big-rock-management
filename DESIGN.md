# Design: The Patch Collection

The Big Rock logo is already an embroidered patch. Every company in the family gets a sibling patch, and the site is the collection board where a visitor picks theirs. Everything else (buttons, tags, form, cards) is made of the same materials: canvas cloth, navy-ink borders, and dashed tan stitching.

## Color

Restrained canvas ground, with one spot color per company that floods that company's page hero.

| Token | Value | Role |
|---|---|---|
| `--ink` | `#121a2b` | Text, patch borders, dark sections, primary buttons |
| `--ink-soft` | `#3a3326` | Secondary text on canvas and cream |
| `--canvas` | `#efe4cf` | Page ground (with a faint canvas weave) |
| `--canvas-deep` | `#e4d4b4` | Collection board, footer |
| `--cream` | `#fbf6ec` | Quiet alternating sections, form card |
| `--tan` | `#d8b277` | Stitching, labels on ink |
| `--tan-deep` | `#6e5126` | Small labels on canvas |
| `--rentals` | `#ea5576` | Rentals spot (`--rentals-text` `#c0284f` for text on canvas) |
| `--cleaning` | `#f2793a` | Big Rock Service Solutions spot |
| `--hauling` | `#f6c544` | Hauling spot, primary submit button |
| `--realty` | `#6a3fa0` | Big Rock Realty Group spot (cream text on it) |

Ink text on each spot passes AA. The spot colors are never used as gradients.

## Type

- **Display:** Alfa Slab One (self-hosted), matching the logo's slab. Headlines at `clamp(2.6rem, 6vw, 5.6rem)`, line-height 1.02, tracking -0.01em.
- **Labels:** Archivo at width 125, weight 800, uppercase, tracking 0.08–0.16em, matching the logo's "MANAGEMENT" lettering. Minimum size 11px.
- **Body:** Archivo at width 100, 17px / 1.6.

## Patches

`.patch` = round dome (a scene from `assets/patches.svg`, a navy border, an inner dashed cream stitch) + navy label bar (white slab name, tan wide label). Scenes are flat cut-color layers only: sky bands, sun, butte, navy silhouettes. Depth comes from overlap, never from shading or gradients. Patches sit with a slight tilt (±2–5°) and a soft drop shadow.

New company → new `<symbol id="scene-*">` in `patches.svg`, a new spot token, and an entry in `PATCHES` in `_src/build.py`.

## Components

- **Buttons:** pill, ink fill, inner dashed stitch (`::after`, inset 5px). Variants: `--light` (cream), `--gold` (submit). `:active` scale 0.97.
- **Tags:** small outlined pills with a Lucide icon, for the three approved claims only.
- **Photos:** 22px radius, 3px ink border, a patch overlapping one corner.
- **Lists:** Lucide check ticks. **FAQ:** native `<details>` with a rotating plus icon.
- **Form:** cream card with a dashed stitch inset, 2px ink inputs at 12px radius, and a gold focus ring.

## Motion

- Sew-on: on page load, the patches settle in (opacity, an 18px rise, a 6° rotation, scale 0.94→1), 620ms `cubic-bezier(0.23,1,0.32,1)`, staggered 70ms. Under reduced motion this becomes an opacity fade only.
- Hover (fine pointers only): patches straighten and lift 6px; buttons lift 2px.
- Mobile menu: 200ms fade and 6px drop.

## Layout

Max width 76rem, gutter `clamp(1rem, 4vw, 3rem)`, sections padded `clamp(4rem, 9vw, 7.5rem)`. Single breakpoint at 880px for most layouts. On mobile, the collection board moves directly under the home headline, so all four companies are visible in the first screen.
