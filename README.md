# Ecoy Design System

The single source of truth for how Ecoy looks and sounds on screen: colours, type, tags and badges, buttons, pillar shapes, logo rules, motion and voice. Built as plain HTML + CSS so Claude Design, Claude Code, Shopify theme work and any teammate can consume the same values.

Sources: **Ecoy Rebrand 2026 V2** brand guide (33 pages) and **Tag & Chip Spec v0.1**. Every rule here cites the page it came from. Anything the sources left open is marked **TBC** and listed in [CHANGELOG.md](CHANGELOG.md).

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
| `logos/` `shapes/` `fonts/` | Logo SVGs, the five pillar-shape SVGs, the font files the CSS needs. |
| `reference/` | Rendered pages from the brand guide and the spec, for visual context. |
| `examples/` | Curated real creative (emails, ads) with an index explaining what each one gets right. See `examples/README.md`. |

## Using it

**Claude Design.** Link this repo under "Link code from GitHub" in the project settings, and drop `fonts/*.otf` and `logos/*.svg` into "Add fonts, logos and assets". Claude Design reads the CSS for tokens and the `components/` pages for component anatomy.

**Claude Code.** Clone the repo at `Ecoy Web Development/design-system/`. The `design` skill finds `css/tokens.css` and the fonts automatically before drawing anything.

**Shopify / web.** Load `fonts.css`, `tokens.css`, `base.css`, `components.css` in that order. Use the classes in `components.css`; never hardcode a hex or a font size that has a token.

**Humans.** Read `BRAND.md` first, then open `components/colors.html` and `components/tags-badges.html`.

## Changing something

1. Tokens: edit `scripts/build_tokens.py`, run `python3 scripts/build_tokens.py`. Never hand-edit `tokens.css` or `tokens.json`.
2. Components and rules: edit the CSS or markdown directly.
3. Note the change in `CHANGELOG.md`, commit, push. Claude Design picks up the repo on its next sync or re-link.

## Rules that are not negotiable

- Bright Orange is an accent, never a foundation.
- One tag category per job: urgency Burgundy, value Orange, newness Deep Green, filter neutral to green.
- Max one on-image badge per card, max one inline tag per item.
- Malinton by default; Satoshi only when small, dense or legibility-critical; Inter only as the Google-safe stand-in (mandatory in EDM).
- Motion always eases. Nothing linear, nothing rushed.
- Fonts are licensed. This repo is private; do not republish `fonts/` elsewhere.
