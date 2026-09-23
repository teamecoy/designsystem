# Showcases: reconciled from Claude Design, not yet fully portable

These are React/JSX pages built inside the **Ecoy Design System** Claude
Design artifact, then reconciled into this repo after they were found to
have drifted (built there, never pushed back — see "Known gap" below).

This is a different content type to `components/`. `components/*.html` are
standalone HTML demo pages that need nothing but this repo's own CSS
(`css/tokens.css`, `css/base.css`, `css/components.css`) and each start with
a `<!-- @dsCard group="…" -->` marker for the Design System pane.
`showcases/*.jsx` are React components that only run inside the Claude
Design artifact's own runtime — they are not standalone, and are not
`@dsCard`-registered.

## What's here

- `index/LaunchEmail.jsx` — a Winter Flannelette launch EDM/Klaviyo showcase.
- `index2/Sections.jsx` — lower storefront homepage sections (range bands,
  bundle tabs, stats, founders, impact).

## Why they don't run standalone

Both depend on `window.EcoyDesignSystem_9bc9f5`, the artifact's compiled
component bundle (`Button`, `Logo`, `Badge`, `ProductCard`, etc.) — source
not in this repo.

`Sections.jsx` additionally references `EIMG`, `CDN`, `Icon` and
`cardProps` as bare globals. These are defined by a sibling `Shell.jsx` in
the same artifact session, which also included `Home.jsx`, `Collection.jsx`,
`Product.jsx` and `App.jsx`. **None of those five files exist in this repo**
(confirmed: searched every branch, none found) — so `Sections.jsx` cannot
render even inside a page that only has this repo's contents.

**Before treating either file as production-ready**, pull the missing
pieces from the artifact too:
1. The `EcoyDesignSystem_9bc9f5` bundle source (or find out what generates
   it, if it's built rather than hand-authored).
2. `Shell.jsx`, `Home.jsx`, `Collection.jsx`, `Product.jsx`, `App.jsx`.

## What was fixed on reconciliation (2026-09-23)

- `LaunchEmail.jsx`'s colourway grid claimed "Five colours" but rendered
  six, one labelled "Oat Milk" — not a real Ecoy colourway. Removed the
  fabricated sixth entry and resolved the remaining five against the real
  Flannelette Sheet Set line (`assets/cdn-catalog.json`): Oatmeal, Forest
  (ForestGreen), Jacaranda, Eggplant, Sage — an exact match, confirming
  this actually is the live 5-colour range.
- `Sections.jsx`'s bundle tile images (`tile-*.jpg`) were left untouched:
  they're staged bundle-composite renders, not single-product photography,
  so they're out of scope for `assets/resolveImage.js`. Someone who can see
  what each hash actually depicts (open the artifact) needs to confirm or
  replace them.

## The bigger gap this surfaced

The sync between this repo and the Claude Design artifact is currently
one-way (repo → artifact, via "Link code from GitHub"). Nothing pushes
artifact-authored work back here automatically, which is how these two
files — and potentially the five siblings and the component bundle above —
drifted out of sync undetected. See the reconciliation process proposed in
the PR that added this file for a lightweight fix going forward.
