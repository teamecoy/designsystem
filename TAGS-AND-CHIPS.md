# Tags, chips and badges

Distilled from Tag & Chip Spec v0.1. Covers on-image badges, inline tags and filter pills across web and EDM. Everything here is implemented in `css/components.css` and shown in `components/tags-badges.html`. All values are the spec's **proposed defaults pending audit against the live site**.

## 01 · Taxonomy: one colour per job

Every tag belongs to exactly one category. The category sets the colour. No exceptions.

| Category | Colour | Examples | Rule |
|---|---|---|---|
| Urgency | Burgundy `#A30042` | Last chance, Sale, Low stock | Time-bound only |
| Value | Bright Orange `#FF6301` | 30% off, Best seller | Commercial benefit only |
| Newness | Deep Green `#004C39` | New, New colours | Currently split across orange and burgundy on site: consolidate |
| Filter | Neutral at rest, Deep Green active | Sheets, Quilts, Best Sellers | Interactive browsing pills. Never a badge |

## 02 · Anatomy: one spec per placement

All tags: Satoshi (Inter in EDM), tracking −2%, line height 100%.

**2026-10-16:** On-image badges and inline tags were reduced about 12% from Tag & Chip Spec v0.1 (13px → 11.5px and 12px → 10.5px, with padding and badge corners scaled to match) after review on the nav mock. Filter pills are unchanged.

| | On-image badge `.badge` | Inline tag `.tag` | Filter pill `.pill` |
|---|---|---|---|
| Sits | on product imagery and hero tiles | next to nav links, product names, prices | in browse and collection filters |
| Font | 11.5px Semi Bold (`tag/md`) | 10.5px Semi Bold (`tag/sm`) | 14px Medium (`tag/lg`) |
| Padding | 12px x · 5px y | 9px x · 3.5px y | 20px x · 10px y |
| Radius | 7px | Full pill | Full pill |
| Case | Sentence | Sentence (see §03) | Sentence |
| Limit | 1 per card | 1 per item | n/a |
| States | n/a | n/a | Rest neutral grey + ink · Active green + white · Hover fill darkened ~8% (TBC) |
| Contrast | 4.5:1 on any image | | |

Shape is deliberate: 7px corners on badges so they read as a label on the photo, not a button. Full pills for inline tags and filter pills; inline tags stay small and quiet next to text, filter pills read as interactive.

## 03 · Casing: one rule everywhere

Current state: nav mega-menu uses LAST CHANCE in caps; product cards use Last chance in sentence case. Same message, two treatments.
**Proposed rule (TBC with Ecoy before locking): sentence case for all badges and tags, all placements. Caps reserved for nothing.** The CSS implements sentence case.

## 04 · Tag type scale

| Token | Size | Weight | Used for |
|---|---|---|---|
| `tag/lg` | 14px | Medium | Filter pills |
| `tag/md` | 11.5px | Semi Bold | On-image badges |
| `tag/sm` | 10.5px | Semi Bold | Inline tags (nav, price) |

Tags keep their own scale and do not resize between breakpoints. Satoshi has no 600 cut; Semi Bold renders as Satoshi Bold.

## 05 · Readability and shape

Functional text on chips targets 4.5:1. Solid fills only on imagery, no tints.

| Pairing | Ratio | Verdict | Use |
|---|---|---|---|
| Burgundy + white | 8.0:1 | Pass AA | Default for urgency badges |
| Deep Green + white | 10.0:1 | Pass AA | Default for newness and active pills |
| Bright Orange + white | 3.0:1 | AA Large only | Allowed: brand accent, badges only |
| Bright Orange + charcoal | 5.7:1 | Pass AA | Alt where max legibility needed |
| Neutral fill + charcoal | 13.5:1 | Pass AA | Default for filter pills at rest |

Ratios recomputed from the tokens and match the spec, except the neutral-fill row: the spec printed 11.5:1 for its unnamed grey, our proposed `#E9E5DB` gives 13.5:1. **White on Bright Orange is an accepted brand exception for badges:** keep labels short, minimum 10.5px Semi Bold (the inline tag size), never for functional or body text. Charcoal on orange is the fallback where legibility is critical.

## 06 · Site type scale

See `BRAND.md` Typography and `css/tokens.css`. Headings Malinton, body and functional text Satoshi, Inter in EDM. Same element = same token everywhere. No size drift between placements.

## 07 · Do and don't

**Do:** max one on-image badge per card plus max one inline tag at price level · use the category colour, always · keep labels to two words max · check contrast on imagery before shipping.

**Don't:** stack Sale + Last chance on the same card (pick one) · put newness in burgundy or orange · mix caps and sentence case across placements · restyle a filter pill as a badge or vice versa.

## Open items

- Filter pill neutral fill: spec says pull from the live site. Proposed `#E9E5DB` until confirmed.
- Hover treatment: ~8% darken, TBC.
- Casing rule: sentence case, to confirm with Ecoy.
- Full audit of tag values against the live build.
