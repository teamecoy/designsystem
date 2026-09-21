# Ecoy Design System

The single source of truth for how Ecoy looks and sounds on screen: colours, type, tags and badges, buttons, pillar shapes, logo rules, motion and voice. Built as plain HTML + CSS so Claude Design, Claude Code, Shopify theme work and any teammate can consume the same values.

Sources: **Ecoy Rebrand 2026 V2** brand guide (33 pages) and **Tag & Chip Spec v0.1**. Every rule here cites the page it came from. Anything the sources left open is marked **TBC** and listed in [CHANGELOG.md](CHANGELOG.md).

## Before you design anything: sale or evergreen?

Evergreen work (launches, colour drops, site, brand content, retention) follows this system exactly. Named sales get their own creative identity from a Sale Identity Brief, with the Ecoy wordmark in the sale logo and the brand palette as the sandbox. Full rule in [BRAND.md](BRAND.md#start-here-is-this-sale-or-evergreen). Ask this first, every time.

## What's here

| Path | What it is |
|---|---|
| `css/tokens.css` | Every design token as a CSS custom property. Generated. |
| `tokens.json` | The same tokens in W3C Design Tokens format for Figma, Claude Design and tooling. Generated. |
| `scripts/build_tokens.py` | The one place tokens are edited. Run it to regenerate both files above. |
| `css/fonts.css` | `@font-face` for Malinton and Satoshi (files in `fonts/`), with Inter and Fredoka fallbacks. |
| `css/base.css` | Body, headings, type scale, colour-block utilities, cards, motion defaults. |
| `css/components.css` | `.badge` `.tag` `.pill` `.chip` `.btn` `.pillar` `.circled` and friends. |
| `components/*.html` | One demo page per part of the system. Open any in a browser. Each starts with an `@dsCard` comment naming its group. |
| `BRAND.md` | The brand guide distilled: character, voice, pillars, messaging, logo, colour, type, visual assets, motion. |
| `TAGS-AND-CHIPS.md` | The tag spec distilled: taxonomy, three placement specs, casing, contrast, do and don't. |
| `assets/library/` | **42 curated photographs — the images you design with.** 1200px WebP, every one a live colourway. Indexed in `assets/library-shortlist.json` with product, colour and angle. |
| `assets/` | The rest of the photography layer: the naming grammar (`naming.json`), an index of all 9,233 files in Drive (`library-index.json`), and which colourways are still for sale (`colour-status.json`). Read [ASSETS.md](assets/ASSETS.md) first. |
| `logos/` `shapes/` `fonts/` | Logo SVGs, the five pillar-shape SVGs, the font files the CSS needs. |
| `reference/` | Rendered pages from the brand guide and the spec, for visual context. |
| `examples/` | Ten real Klaviyo emails that performed, images localised, indexed by brand status and what to copy. See `examples/README.md`. |

## Using it

**Claude Design.** Link this repo under "Link code from GitHub" in the project settings, and drop `fonts/*.otf` and `logos/*.svg` into "Add fonts, logos and assets". Claude Design reads the CSS for tokens, the `components/` pages for component anatomy, and **`assets/library/` for photography** — reference those images by relative path, e.g. `assets/library/Wide Lifestyle/BambooSheetSet-Solid-Caramel-Side-NoTalent-Real-10.webp`. `assets/library-shortlist.json` lists every one with its product, colour and angle, so pick from there rather than guessing a filename.

**Claude Code.** Clone the repo at `Ecoy Web Development/design-system/`. The `design` skill finds `css/tokens.css` and the fonts automatically before drawing anything.

**Shopify / web.** Load `fonts.css`, `tokens.css`, `base.css`, `components.css` in that order. Use the classes in `components.css`; never hardcode a hex or a font size that has a token.

**Humans.** Read `BRAND.md` first, then open `components/colors.html` and `components/tags-badges.html`.

## Changing something

1. Tokens: edit `scripts/build_tokens.py`, run `python3 scripts/build_tokens.py`. Never hand-edit `tokens.css` or `tokens.json`.
2. Components and rules: edit the CSS or markdown directly.
3. Note the change in `CHANGELOG.md`, commit, push. Claude Design picks up the repo on its next sync or re-link.

## Rules that are not negotiable

- Design only with the photographs in `assets/library/`. Everything else lives in Drive, named to the convention in `assets/ASSETS.md`. Images in `examples/` and `reference/` are compressed reference renders, never design assets.
- Never use a retired colourway. `assets/colour-status.json` is the list; 23 are live, 10 are retired. The curated library already excludes them.
- High45 is the preferred angle for ads and hero creative, then Low45, then Side.
- Sale or evergreen is decided first. Evergreen follows this system; a sale follows its Sale Identity Brief.
- Bright Orange is an accent, never a foundation.
- One tag category per job: urgency Burgundy, value Orange, newness Deep Green, filter neutral to green.
- Max one on-image badge per card, max one inline tag per item.
- Malinton by default; Satoshi only when small, dense or legibility-critical; Inter only as the Google-safe stand-in (mandatory in EDM).
- Motion always eases. Nothing linear, nothing rushed.
- Fonts are licensed. This repo is private; do not republish `fonts/` elsewhere.
