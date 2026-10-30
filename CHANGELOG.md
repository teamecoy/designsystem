# Changelog

- 2026-10-30 — BFCM 2026: the sale logo now exists as files. `sales/bfcm-2026/logo/` has BLACK FRIDAY and CYBER MONDAY alone and as the Ecoy lockup, in the four phase colours (white, green, orange, ink), as outlined SVGs with the LED glow and 2400px transparent PNGs, built by `build_logo.py` from the sale font. Until now the lockup was live type only, so nothing outside the templates could find a logo.
- 2026-10-27 — BFCM 2026: offer stacks now space evenly. New `.bf26-offerstack` in `sale.css` (lead-in, offer, tail) trims every line to its capitals and sets one gap, the small line's cap height, above, below and between rows, matching Nick's statics. The five hand-built stacks in `templates.html` now use it, and `callouts.html` has a demo. Fixes the extra space under "54% OFF" in the 27 Oct Claude Design hype round. Rule and Figma settings in IDENTITY §5.
- 2026-10-26 — BFCM 2026: phase colours locked (hype white, live green `#77D686`, end orange `#FF6301`; PGS Colour Breakdown and Nick's final statics agree) and the **Static Ads page resynced as final** from the PGS copy `q8VGTz4nTuVSd52p4RqO3i` (`2016:1141`). 33 reference frames replace the drafts: four sets (hype, hot sleepers, old winners, ending), each piece as a 4:5 feed and a 9:16 story. New in `sale.css`: `.bf26--feed` (1080×1350), stat line, night timeline, comparison table, tape, pill, receipt, battery, lock screen and photo quote; the small lockup is now full-strength accent (white in End); badges in live are green, white or ink (merlot and orange dropped). `templates.html` gets all 16 feed statics with real VoC reviews and brief-correct offers. Copy conflicts with BRIEF.md (54% in hype, "60% off everything", "Santi B.") listed in IDENTITY §7.
- 2026-10-23 — BFCM 2026 type fix: offers, tickers, stamps, countdowns, codes and every other dot-matrix line move from LED Display St to **Doto** (square dots, Bold 700), matching Nick's frames. LED Display St stays for the event name only ("BLACK FRIDAY", "CYBER MONDAY"). Adds `fonts/Doto-Variable.ttf` (SIL OFL, free for commercial use), `--bf26-font-dot`, and `.bf26-dot--light` (500) / `.bf26-dot--heavy` (900) weight steps. IDENTITY.md §2 updated.
- 2026-10-20 — BFCM 2026 templates are fuller. New story formats from Nick's drafts and PGS: a hot-sleepers review static (four real VoC reviews), Ecoy vs Dumb Bedding, a split grid, Every Colour with a 12-colour stack grid, a talent hero and a hype countdown. New website pieces from the PGS skeleton: announcement bar, shipping notice, homepage hero desktop and mobile (live and Cyber Monday), collection banner, mega-menu tile, secondary tiles, PDP badge, price and gift callout, cart drawer progress, gift block (hype and live), and the hidden-hype code, countdown and sign-up modules. New PGS frame sizes and module classes are in `sale.css`.
- 2026-10-20 — BFCM 2026: ending orange `#FF6301` confirmed (Sam), following PGS's phase colour system (Figma `2005:2`). The End default is now black fabric with orange LED; Nick's orange grounds stay as the paid-statics alternative. PGS's phase rules are added: one colour per phase, a 40 to 50% black overlay on photos, black fabric in hype, a dark band behind tickers on light images, and undimmed product tiles. LED offers stay (Sam's call over PGS's "LED is the event name only"). Badges (`.bf26-burst`) now follow the phase, with merlot `#6B1E2E` and orange alternates and a new Every Colour badge demo.
- 2026-10-19 — BFCM 2026: LED colour now follows the phase (Sam). Hype = white, Live (5 to 26 Nov) = green `#77D686`, End (27 to 30 Nov) = FOMO colour TBA, with Bright Orange `#FF6301` holding until it's confirmed. New phase classes `.bf26--hype` / `--live` / `--end` in `sale.css`; ink LED on orange ending grounds; offers white in every phase; quiet silver headline when the offer leads; frame tickers, starburst stickers and an LED CTA pill from the draft statics. The Light Green `#A3C2A7` ticker rule is replaced. BRIEF.md adds the Win Back Your Order weekend (13 to 15 Nov), GWP 2, the flash offer and Christmas placeholders, the hidden hype landing pages with codes `BFEXTRA10` / `BFCMEXTRA10`, and the skeleton's open items. Source: PGS Figma `NEP7LWbP6wf89uKLcqKWxO`. The static ads are drafts and need a resync.
- 2026-10-16 — Tags: on-image badges and inline tags are about 12% smaller (Sam, after the nav review). `tag/md` 13px → 11.5px, badge padding 6×14 → 5×12, badge radius 8px → 7px. `tag/sm` 12px → 10.5px, inline padding 4×10 → 3.5×9. Filter pills unchanged. The minimum size for white-on-orange is now 10.5px. Changed in `scripts/build_tokens.py`; tokens regenerated; TAGS-AND-CHIPS.md and the tags-badges demo updated.
- 2026-10-15 — Photography README: CDN routes that work without the repo (Shopify Files query, public CDN url); not-live-on-site colours are still on the CDN; Drive is last resort; no third-party brands; ad counts must match photo.

## v0.8 · 2026-10-05

**Voice of customer**
- Added `voc/`: every published Judge.me review (5,600, Nov 2020 to 4 Oct 2026), tagged for copywriting. Each review carries 29 themes, 12 complaint types, naming-sheet Persona and Angle, product category and fabric, colours (with a retired-colour flag), Judge.me survey answers, a pull quote, a best sentence per theme and a 0–10 ad score.
- `voc/INSIGHTS.md` is the copywriter's summary: 4.81★ across all products (4.84★ bedding), 90% of the 1,926 who answered say their sleep improved, 63% switched from cotton, theme and complaint counts, and 8 de-duplicated quotes per theme.
- `voc/VOC.md` covers the fields, how to query with jq or Python, and the rules for using reviews in ads (word for word, first name + initial, survey stats with their base, no competitor names, no retired colours).
- `voc/build_voc.py` rebuilds everything from a fresh export. It drops emails and IP addresses and shortens names. The raw export is never committed.

## v0.7 · 2026-10-05

**Awards**
- Added `awards/bedbuyer/`: five Bedbuyer award badges as transparent PNGs trimmed to the artwork. There are 3-year (2023–2025) stacked and framed versions in colour, and 2025 horizontal and stacked versions (horizontal in colour and white). The untrimmed originals are in `source/`.
- `awards/AWARDS.md` covers when to use a badge (any "award-winning" claim or trust signal), which file goes on which ground, one badge per piece, never altering the artwork, and copy that matches the claim.
- `components/awards.html` is a new demo card in the Brand group.
- Open: award category TBC (don't name a winning product yet). There's no white 3-year version; ask Bedbuyer if one is needed.

## v0.6 · 2026-09-29

- **Polka** is named after the dot colour on the fabric: EggplantPolka, BurgundyPolka, IcedChocolatePolka, ForestPolka, CaramelPolka. The first shoot (981 images) was renamed and moved into the standard `Product / Polka / Colour / Talent / Orientation` layout, and queued for the CDN.
- **Sky and Burgundy** have vocabulary entries and count as live (25 live, 10 retired). Their photos are still in the "to be renamed" folder.
- 450 new Solid shots queued: Butter and Burnt Orange quilt covers and sheet sets, Jacaranda fitted sheets.
- The pipeline is complete in the repo: `build_upload_manifest.py` is new, the notebook now makes its own web copies, the library index keeps its descriptions on rebuild, and shot numbers can run past 99. See "After a new shoot" in ASSETS.md.

## v0.6 · 2026-09-28

**Sales**
- Added `sales/`, one folder per named sale identity, kept apart from the evergreen system. See `sales/README.md`.
- `sales/bfcm-2026/`: Black Friday + Cyber Monday 2026, codified from Nick's Figma (`xt3zyQMwBYDSJ5WofvTwJJ`, page `0:1`). Includes `IDENTITY.md` (LED Display St headlines, Clash Display caps sub-headlines, colours sampled for every type role, lockup and logo sizes for ads vs emails vs web, tickers, circular callouts, phases, and a PDP banner recommendation), a `sale.css` scoped to `.bf26` with container-unit sizing, two demo pages, fonts, and 25 reference renders.
- `sales/bfcm-2026/stack-cutouts.json`: transparent folded-stack cut-outs checked by eye. The library's `Deepetch` angle mixes stacks with packaging, stool shots and opaque white-background files.
- `sales/bfcm-2026/BRIEF.md`: offer by phase, GWP tiers and copy guardrails from James's Notion agency brief (Notion stays the source). Up to 54% main sale; Day 1 extra 10% via an earned code, never shown in public creative; ending phase steps to 60%, shown as a small struck-out old offer above a big new one; Cyber Monday is the last day of the one sale.
- Ticker green is brand Light Green `#A3C2A7`, per Sam.
- Open: LED Display St needs a commercial licence; James to confirm the 60% step; leftover EOFY/Birthday copy and placeholder offers in Nick's frames.

## v0.5 · 2026-09-24

**Ads**
- Added `ads/`. `parse_ad_name.py` reads Meta ad names in all three styles in use: v2 (since May 2026), the older pre-May convention, and creator-program ads (identified by an `@handle` or `CP-UGC`). It returns the campaign moment and its type (sale, promotion or evergreen), designed vs creator, angle, format, persona, awareness stage, concept, and the photo colour to resolve imagery with. Tested on the top 25 ads by spend: 17 v2, 6 creator, 5 legacy, 2 free-form.
- `ad-naming.json` is generated by `build_ad_naming.py` from a snapshot of the team's "Ecoy Naming Convention Generator" sheet, which stays the single source and should always be pulled fresh.
- BRAND.md and README: **promotions** (Mother's Day, Father's Day, Valentine's, Easter) follow the brand system, not a sale identity; **Christmas is a sale**. New rule: every winner gets "how do we turn this into another 5 ads?"
- Gaps recorded in `ads/ADS.md`: the sheet's "forecast parser" didn't exist (this is it now), four colour aliases to confirm, StrawberryMerlot missing from the sheet, glossary values the dropdowns lack.

**Photography (2026-09-21 to 09-23)**
- `assets/library/` grew from 42 to 287 curated photographs.
- 6,340 library images are on the Shopify Files CDN at urls derived from the filename. `assets/resolveImage.js` and `cdn-catalog.json` look one up by product, colour and angle (High45 first) and return a live url or null. 10 files are flagged not yet live pending an uploader run.
- The naming vocabulary gained an optional Orientation field (Vertical/Horizontal, new shoots only) and five Polka colours.
- README no longer caps design work to the in-repo library.
- `showcases/` holds two React pages reconciled from Claude Design (reference only; they need the artifact's runtime).

## v0.4 · 2026-09-17

- Added `assets/`: the photography naming grammar as code. `naming.json` (generated from the VA's filename spreadsheet, which stays the single source) carries 22 product tokens, 33 solid and 5 stripe colours, 7 camera angles, and the talent and real-or-AI flags. `ASSETS.md` explains how to compose a filename and locate it in Drive. `check_filenames.py` validates a name or a whole folder.
- Stated explicitly that the repo holds no photography and that images in `examples/` and `reference/` are reference renders, never design assets.
- Recorded the known gaps: Polka has no assets yet, combo colours have no dropdown, the spreadsheet's "How to use" tab says `Solo` where everything else says `NoTalent`, and Shopify media follows no convention.

## v0.3 · 2026-09-16

- Added the opening rule to BRAND.md, README.md, index.html and the examples index: **sale or evergreen?** Evergreen follows this system exactly; each named sale gets its own creative identity from a Sale Identity Brief (Ecoy wordmark in the sale lockup, brand palette as sandbox, three switchable phases). Examples re-labelled from "pre-rebrand" to "sale identity" to match.

## v0.2 · 2026-09-16

- `examples/`: ten real Klaviyo campaigns, images localised and compressed (4.8 MB total), indexed with performance data, brand status (on-brand vs pre-rebrand) and what to copy. Selection: top revenue, revenue per recipient, open rate and click rate over 12 months, plus product launches and colour drops. April Fools excluded on Sam's instruction.
- Surfaced: Klaviyo shell font is Montserrat, not Inter; sale templates were still pre-rebrand in Feb 2026.

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
