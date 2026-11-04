# Sale identities

One folder per named sale, each with its own look. Evergreen and promotions never use anything in here; see [BRAND.md](../BRAND.md#start-here-is-this-sale-or-evergreen).

| Folder | Sale | Status |
|---|---|---|
| [`bfcm-2026/`](bfcm-2026/IDENTITY.md) | Black Friday + Cyber Monday 2026 | Codified from Nick's Figma 2026-09-28; phase colours from the PGS pages 2026-10-19, locked 2026-10-26; final statics (33 frames, 4:5 + 9:16) resynced 2026-10-26; open items in §9 |
| [`christmas-2026/`](christmas-2026/FLOATING-RIBBON-PROMPT.md) | Christmas BOGO 50% 2026 (1–21 Dec) | Not codified yet (concept board in progress). Has the approved prompt for floating gift shots with a ribbon in any new colour or pattern |

**Designing for a sale:** read that sale's `IDENTITY.md` first, load its `sale.css`, and wrap the piece in its scope class (e.g. `.bf26`). Photos still come from the main library (`assets/resolveImage.js`), filtered by the sale's own rules.

**Adding a sale:** create `sales/<sale>-<year>/` with the same shape:
- `IDENTITY.md`: type, colour on type, lockup and logo sizes per channel, components, photography, phases, open items
- `BRIEF.md`: the offer, phases and copy guardrails, taken from the agency brief with a link back to its source
- `sale.css`: everything scoped under one class so it can't leak
- `fonts/`: the sale's fonts, with licence status recorded in `IDENTITY.md`
- `components/*.html`: demo pages, each starting `<!-- @dsCard group="Sale · <Name>" -->`
- `reference/`: the designer's original frames as compressed WebP (reference only, never assets)
- `STAGES.md`: the website plan per stage (theme IDs, every surface and its copy, headline % per collection, re-sync list, revert, post-mortem). Written and kept by the `ecoy-sale-rollout` skill in the ecoy-shopify-dev plugin; `bfcm-2026/STAGES.md` is the worked example

The creative brief for a sale comes from the `ecoy-sale-identity` skill. This folder is the version Claude Design and Claude Code can build from.
