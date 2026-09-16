# Changelog

## v0.1 · 2026-09-16

First conversion of the two PDFs into code.

**Sources**
- `Ecoy_Rebrand_2026_V2.pdf`, 33 pages. Palette p17, pairings p18, colour-in-use p19, type p22, pillar shapes p24, UI chips and hand-drawn p26, brand usage p28–31, motion p33.
- `Tag & Chip Spec — v0.1.pdf`, one page. Taxonomy §01, anatomy §02, casing §03, tag scale §04, readability §05, site type scale §06, do/don't §07.

**Values we proposed ourselves (TBC, awaiting Ecoy confirmation)**
| Token | Proposed | Why |
|---|---|---|
| `--color-neutral-fill` | `#E9E5DB` | Filter pill at rest. Spec says "pull from live site". We do not scrape the live storefront (project rule), so this is an Off White shade that keeps 11.5:1 with charcoal. |
| `--color-neutral-fill-hover` | `#D8D3C6` | Spec proposes "fill darkened ~8%". |
| `--color-deep-green-hover` | `#003D2E` | Deep Green darkened ~8% for CTA and active-pill hover. |
| `--motion-*` durations and curves | 150 / 250 / 400 ms, `cubic-bezier(.4,0,.2,1)` | Guide p33 gives principles only. |
| Casing | Sentence case everywhere | Spec §03 proposal, "to confirm with Ecoy before locking". |
| Feature chip fill | Off White at 82% with blur | Read from guide p26 imagery; the guide gives no value. |
| Card radius | 24px / 16px | Read from guide layouts; no value given. |

**Known gaps**
- Satoshi has no 600 cut. The spec's "Semi Bold" renders as Satoshi Bold (700).
- All tag values are the spec's "proposed defaults pending audit against live site". Audit is Sam's to run.
- `examples/` is empty. Fill with curated real creative as v0.2.
- Product fabric colours (Master Colour Register) are deliberately not here; they are a different system.
