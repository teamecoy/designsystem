# Black Friday / Cyber Monday 2026: web stages

Sources: Marketing Calendar (read 3 Nov), James's Notion brief (`BRIEF.md`), identity `IDENTITY.md`, runsheet `Black_Friday_2026_Web_Rollout_Runsheet` (Google Sheet `1uA6sp158S_x5EsjVYgbDzz-30ZYFrHW9ofJRa2qWmng`), pricing artifact `NBB6pcHESoFZCxwEqJ9dHz` (read 4 Nov).
Sale menu: `main-menu-bfcm-2026` (`Menu/273402527996`): Black Friday, Bed linen, Bedding, Shop by need, Bundles [Save], Reviews. Live menu `main-menu-shop-by-need` untouched.
CSS prefix in `assets/sale.css`: `BF`.

This file was written on 4 Nov, after the work, as the first worked example of the `ecoy-sale-rollout` skill. Status reflects 4 Nov evening.

## Headline % by collection

| Collection | Max % | From | Source | Banner text |
|---|---|---|---|---|
| bamboo-sheets | 54 | 5 Nov | Phase 1 colours (Burgundy, Caramel, Dune, Dusk, Lagoon, Matcha, Storm Blue) | Up to 54% off |
| solid | 54 | 5 Nov | same | Up to 54% off |
| ambi | 25 → 54 | 5 Nov → **Fri 27 Nov** | BF weekend bait: Cloudy Sky, Cookies & Cream, Sage Coconut, Sandy Reef | Up to 25% off → **change to 54 on 27 Nov** |
| polka | 15 | 5 Nov | every polka colour 15% | 15% off |
| flannelette | 54 | 5 Nov | clearance, whole range | Up to 54% off |
| quilts-pillows-mattress-protectors | 54 | 5 Nov | legacy LW/MW quilts until sold out (about 40 without them) | Up to 54% off |
| quilts (megamenu tile) | 54 | 5 Nov | same | Up to 54% off quilts |
| all-products (Bed linen, 85 products) | 54 | 5 Nov | bamboo Phase 1 colours, flannelette, legacy quilts | Up to 54% off (`image_hero_EUj4ky` tag `tag_NhzAp3`, was a disabled "Up to 51% off") |

Checked against the pricing artifact, not the imported prices. Re-check after the import.

## Stage themes

| Stage | Dates (AEDT) | Theme |
|---|---|---|
| Launch | Thu 5 Nov | `189127819516` "Stiletto \| Black Friday Sale" |
| Main sale | Fri 6 → Thu 12 Nov, then Mon 16 → Thu 19 Nov 20:00 | `189767254268` "… \| Main sale" |
| Win Back Your Order | Fri 13 → Sun 15 Nov | `189774364924` |
| GWP phase 2 | Thu 19 Nov 20:00 → Fri 27 Nov 00:00 | runsheet says pre-built theme + bar; not built as of 4 Nov. Cart flip: Tote replaces Sleep Mask at $250+ |
| BFCM weekend | Fri 27 Nov 00:00 | not built as of 4 Nov (up to 60%, orange End phase) |
| Cyber Monday | Mon 30 Nov → 23:00 | not built as of 4 Nov (countdown to 23:00) |

## Changes on Launch, Main sale and Win Back (4 Nov)

All three verified by `checksumMd5`; checked visually on the Launch preview, desktop and 390px.

| Surface | Change | File / setting |
|---|---|---|
| Nav | Black Friday item first, LED pill (`#77D686` on `#080808`); Last chance removed; reordered | menu above; `header-group.json` `menu`; sale.css "BF NAV PILL" |
| Megamenu (Bedding) | Black Friday tag, "Up to 54% off quilts", Shop quilts → `/collections/quilts`, LightweightQuilt-High45-Square-NoTalent-Real-01, bottom fade | `header-group.json` block `full_width_meganav_fDKnE9`; sale.css "BF MEGANAV PROMO TAG" |
| Homepage | quilt bundles hidden; Bamboo + Quilts & pillows video banners back; video accents "Up to 54% off" pills; creators + stats + review wall replace the reviews carousel; 30px section spacing + divider above creators | `index.json`; sale.css "BF HOMEPAGE VIDEO ACCENT", "BF HOMEPAGE SPACING" |
| Collection banners | "Up to X% off" pills per the table | `collection.bamboo-sheets/flannelette/quilts-pillows/solid-collection/polka-collection/ambi-collection/all-products.json`; `sections/main-collection-banner.liquid` `sale_tag`; sale.css "BF COLLECTION HERO TAG", "BF COLLECTION PATTERN TAGS" |
| Flannelette banner | "LAST CHANCE" accent hidden | `accent_JGTFjD` disabled |
| Sale badge | "Black Friday" replaces "Sale" (cards + PDP) and shows on cards | `snippets/product-badges.liquid`; `assets/local.js` `updateDesktopBadge`; sale.css "BF SALE BADGE", "BF CARD BADGE" |
| Hype tile badge | "ON SALE 5.11" removed | sale.css (block replaced by a comment) |
| PDP | GWP callout after buy buttons (35 templates); price note cleared; Bundle & save 0% | product templates |

December draft `189469098236` got the homepage social proof and spacing only.

## Open (4 Nov)

- `/collections/sale` is **not published** to the Online Store: 404 for customers. Publish before 5 Nov 00:00.
- Ambi banner to 54% on Fri 27 Nov (`collection.ambi-collection.json` → `banner.sale_tag`).
- BFCM weekend and Cyber Monday themes, 60% badges and copy.
- Re-check every % after the price import.
- Mocked, not built (awaiting Sam): homepage headlines in caps (evergreen font), Cloud Quilt photo on the Quilts and pillows tile (`CloudQuilt-High45-NoTalent-Real-01`, needs a cropped copy uploaded).
- Runsheet "Open items" tab: 10 undecided.

## Re-sync list

`assets/local.js`, `assets/sale.css`, `snippets/product-badges.liquid`, `sections/main-collection-banner.liquid`, `sections/header-group.json`, `templates/index.json`, the six collection templates above, every product template (GWP placement, price note, Bundle & save 0%), `assets/theme.js` (slider threshold, Size-click no-scroll; also on live).

## Revert (1 Dec)

Publish the Christmas theme (or live), which drops every theme-level change. Store-wide leftovers: the sale menu (keep, unused), `/collections/sale` visibility, hype redirects.

## Post-mortem

To write after 30 Nov.
