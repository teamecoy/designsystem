# BFCM 2026 · sale logo files

The Black Friday "logo" is the event name set in LED Display St, with the Ecoy wordmark above it (IDENTITY.md §4). Inside the
templates it is live type, so until 30 Oct 2026 there was no file to hand to anyone. These are the files. Glyphs are outlines, so
nothing needs the font installed. Use them wherever the sale name has to be dropped in as an asset: email builders, Figma, Klaviyo,
ad tools, other agents.

| File | Use |
|---|---|
| `bfcm-2026-black-friday-<colour>.svg` / `.png` | Event name alone (statics, where the offer is the hero and the name sits small) |
| `bfcm-2026-lockup-black-friday-<colour>.svg` / `.png` | Ecoy wordmark above the event name (web heroes, emails, anything that leads with the lockup) |
| `bfcm-2026-cyber-monday-<colour>.svg` / `.png` and `…lockup-cyber-monday…` | Mon 30 Nov only, the final day of the one sale |

**Colour follows the phase** (IDENTITY.md §3.1): `white` for hype (2 to 4 Nov), `green` `#77D686` for live (5 to 26 Nov), `orange`
`#FF6301` for the ending (27 to 30 Nov) on black fabric, `ink` `#0A0A0B` for the ending on an orange ground. There is no green Cyber
Monday because it only ever appears in the ending phase. The coloured versions carry the LED glow; ink has none.

PNGs are 2400px wide on a transparent ground. SVGs are tight to the glow with a small margin and scale to any size; the wordmark
is 13.5% of the headline width in the lockup, as in every template.

Not in these files: "SALE" under the headline (the 28 Sep lockup; the final statics dropped it), countdowns, offers. Those are
type, set with `sale.css`.

Rebuild after a font or colour change: `python3 build_logo.py` (needs fontTools, Pillow and Google Chrome for the PNGs).
