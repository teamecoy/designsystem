# Sale identities

One folder per named sale, each with its own look. Evergreen and promotions never use anything in here; see [BRAND.md](../BRAND.md#start-here-is-this-sale-or-evergreen).

| Folder | Sale | Status |
|---|---|---|
| [`bfcm-2026/`](bfcm-2026/IDENTITY.md) | Black Friday + Cyber Monday 2026 | Codified from Nick's Figma 2026-09-28; open items in §9 |

**Designing for a sale:** read that sale's `IDENTITY.md` first, load its `sale.css`, and wrap the piece in its scope class (e.g. `.bf26`). Photos still come from the main library (`assets/resolveImage.js`), filtered by the sale's own rules.

**Adding a sale:** create `sales/<sale>-<year>/` with the same shape:
- `IDENTITY.md`: type, colour on type, lockup and logo sizes per channel, components, photography, phases, open items
- `BRIEF.md`: the offer, phases and copy guardrails, taken from the agency brief with a link back to its source
- `sale.css`: everything scoped under one class so it can't leak
- `fonts/`: the sale's fonts, with licence status recorded in `IDENTITY.md`
- `components/*.html`: demo pages, each starting `<!-- @dsCard group="Sale · <Name>" -->`
- `reference/`: the designer's original frames as compressed WebP (reference only, never assets)

The creative brief for a sale comes from the `ecoy-sale-identity` skill. This folder is the version Claude Design and Claude Code can build from.
