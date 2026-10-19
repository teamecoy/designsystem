# BFCM 2026 · sale identity

Black Friday 2026, running Thu 5 to Mon 30 Nov with Cyber Monday as the last day. Designed by Nick in Figma (`xt3zyQMwBYDSJ5WofvTwJJ`, page `0:1`), codified here on 2026-09-28 and updated on 2026-10-19 from the PGS phase pages (`NEP7LWbP6wf89uKLcqKWxO`: 01 Hype `1:15`, 02 Launch `1:66`, 03 Main Sale `1:151`, 04 Static Ads `2016:1141`) so Claude Design and Claude Code can make new statics that belong to the same campaign.

**This is a sale identity, not the brand system.** Inside this sale, this file overrides `BRAND.md` wherever they disagree (fonts, Bright Orange as a ground, linear ticker motion). None of it carries into evergreen work after the sale, and no future sale reuses it. See [BRAND.md](../../BRAND.md#start-here-is-this-sale-or-evergreen).

**What to say, and when, is in [BRIEF.md](BRIEF.md)** (offer by phase, GWP tiers, copy guardrails), taken from James's agency brief in Notion. Read it before writing any copy.

Load `sale.css` and wrap every piece in `.bf26`. Live demos: `components/templates.html` (every format) and `components/callouts.html` (type, colours, tickers, circular callouts). Nick's originals: `reference/` (reference only, never assets). The 19 Oct additions are `reference/live-hero-launch.webp` and `reference/draft-static-{hype,hot-sleeper,old-winner,ending}.webp` (**drafts, to be resynced**).

**Wrap every piece in `.bf26` plus one phase class: `.bf26--hype`, `.bf26--live` or `.bf26--end`** (§3.1).

---

## 1. The idea in one line

A stadium-scoreboard LED sign in a dark bedroom: dot-matrix headlines glowing over near-black grounds and crumpled sheets, with scrolling ticker strips carrying the offer and the urgency.

## 2. Type

Two typefaces, nothing else.

| Role | Font | Setting |
|---|---|---|
| **Headline** | **LED Display St** (`fonts/LedDisplaySt.ttf`) | ALL CAPS, weight 400, tracking 0, line-height 1, soft glow. "BLACK FRIDAY", "CYBER MONDAY", offers, "NEVER THIS CHEAP AGAIN". |
| **Sub-headline** | **Clash Display Semibold** (`fonts/ClashDisplay-Semibold.*`) | ALL CAPS. "SALE" under the headline, proof lines ("LOVE AWARD WINNING COOLING SHEETS?"), eyebrows ("AWARD-WINNING COOLING SHEETS FOR HOT SLEEPERS"), GWP cards, CTA pills. Clash Medium for longer supporting lines. |
| Tickers, countdown digits, circular callouts, "DON'T MISS OUT" footer | LED Display St | ALL CAPS |

Rules:
- LED is for short, loud lines only: up to about 3 words a line and 3 lines. Anything longer goes in Clash.
- Never set a headline in Clash, Malinton or Satoshi, and never set body copy in LED.
- Email body copy stays in the Klaviyo shell font. The sale shows up in the hero, tickers and CTAs, not the paragraphs.
- Sizes are proportional to the frame (see §5). `sale.css` uses container units, so the same class works at any size.

**Licence, action needed.** LED Display St by southype is "free for personal and non-profit use"; commercial use needs a licence from southype@gmail.com. Buy it before anything goes live. Clash Display (Indian Type Foundry, Fontshare) is under the ITF Free Font License, which allows commercial use.

## 3. Colour on type

### 3.1 The phase rule (2026-10-19)

**The LED accent colour tells you which phase you're in.** Every frame carries one phase class, and that class recolours the headline, the accent offer line, value tickers and stamps. Offers stay white.

| Phase | Dates | Class | LED accent | Seen in |
|---|---|---|---|---|
| **Hype** | Mon 2 to Wed 4 Nov | `.bf26--hype` | **White `#FFFFFF`** (Sam, 19 Oct: hype type changed to white) | Hidden hype pages, countdown, "COMING SOON · DAY 1 CODE INSIDE" frame tickers, hype statics |
| **Live** | Thu 5 to Thu 26 Nov (Day 1, main sale, win-back, GWP 2) | `.bf26--live` | **Green `#77D686`** (Sam, 19 Oct; sampled exactly in the PGS frames) | Homepage and landing heroes ("BLACK FRIDAY / SALE NOW LIVE"), ticker "UP TO 54% OFF", hot-sleeper and old-winner statics |
| **End** | Fri 27 to Mon 30 Nov | `.bf26--end` | **FOMO colour, TBA.** Bright Orange `#FF6301` holds until it is confirmed | Sale-ending statics: orange frames and grounds, "LAST CHANCE", "FINAL HOURS" |

When the FOMO colour is confirmed, change `--bf26-led-orange` (and its glow) in `sale.css` and the End row here. Nothing else needs to change.

### 3.2 Colour by element

| Element | Colour | Notes |
|---|---|---|
| Headline, lockup (web heroes, banners, mega-menu tile) | Phase accent | Green on every live-phase web hero; white in hype. |
| Headline, quiet (`.bf26-headline--quiet`) | White at 64% with white glow; ink at 70% on orange | Used in statics where the **offer is the hero**: BLACK FRIDAY sits small above "UP TO 54% OFF". |
| Offer ("54% OFF", "60% OFF", "AN EXTRA 10% OFF ON LAUNCH DAY") | White `#FFFFFF`, white glow | Every phase. `.bf26-offer--accent` gives the phase-coloured line, e.g. green "UP TO 54% OFF" under white "EVERY COLOUR". |
| Old offer, struck out (End only) | White at 45% on dark, white on orange; strike in the same colour | LED, about 45% of the new offer's size, **above** the new offer ("UP TO ~~54%~~ / 60% OFF"). |
| Ticker, value message ("UP TO 54% OFF", "EXTRA 10% OFF", "DAY 1 CODE INSIDE") | Phase accent | Replaces the 28 Sep Light Green `#A3C2A7` rule. |
| Ticker, phase label ("COMING SOON", "SALE LIVE", "SALE ON NOW") | White in Hype and Live | Live strips alternate white label and green value. |
| Ticker, End ("LAST CHANCE") | Ink `#0A0A0B` on an orange frame; orange on dark | |
| Lead line on an orange ground ("LAST CHANCE TO SAVE") | Ink `#0A0A0B`, no glow | From the ending statics. |
| Headline crossing a product stack on orange | White `#FFFFFF` (`.bf26-headline--white`) | Ink disappears into dark stacks; white keeps the 28 Sep rule. |
| End headline on a dark photo ("FINAL HOURS") | FOMO colour (orange for now) | |
| Hot-sleeper accent line ("WON'T SHUT UP") | Live green | Inside a white LED headline. Green also fills the "ECOY vs DUMB BEDDING" panel and the bottom value band (ink text on green). |
| "SALE" under the headline, lockup wordmark, countdown digits | White at 64% (≈ `#A4A4A7`) | |
| Standalone top wordmark | White `#FFFFFF` (black on orange) | |
| CTA pill | White pill. LED ink text in statics ("TAP TO REVEAL CODE"); Clash Deep Green on web | `.bf26-cta--led` for the static version. |
| Starburst sticker | Ink, white or Live green ground; Clash caps | `.bf26-burst`. "FREE GIFTS", "+10% DAY 1", feature callouts. |
| Circular callout | Phase accent on dark grounds, white on orange | |
| "DON'T MISS OUT" footer | White at 45% | |

**Grounds:** near-black `#080808` (default), Deep Green `#004C39` (the frames sample `#0F4D3A`; the brand token wins), Bright Orange `#FF6301` (End phase: the whole ground, or a frame around rounded photo panels), or a full-bleed photo darkened to about 55% brightness. The PGS frames lean on two photo grounds: **Strawberry Merlot Stripe** (plum stripes, used across Live heroes and statics) and dark teal or black crumpled sheets (hype). In this sale Bright Orange **is** allowed as a ground, overriding the brand rule that it is only ever an accent.

## 4. The lockup and the logo

**Sale lockup** (always centred, stacked):
1. Ecoy wordmark (`logos/logo-white.svg`) at 64% white
2. LED headline
3. "SALE" in Clash Semibold caps at 64% white

The wordmark is the real Ecoy logo, not "ECOY" typed in the LED font. It is always about the same width as "SALE", and about **13.5% of the headline's width**, in every format.

**Logo size by channel:**

| Channel | Lockup wordmark | Standalone wordmark |
|---|---|---|
| **Ads**, 9:16 story (1080×1920) | ≈ 10% of frame width (≈ 108px); headline ≈ 74% | Only when the lockup isn't used (e.g. the proof story): top centre, ≈ **15% of frame width (≈ 160px)**, ≈ 11.5% down from the top, 100% white |
| **Ads**, 1:1 feed (1080×1080) | Same ratio to the headline | ≈ 15% of width, top centre |
| **Emails** (600px Klaviyo width) | ≈ **11% of email width (≈ 64px at 600px)**; headline ≈ 78% | **None.** The email relies on the lockup; the shell header carries the brand. |
| **Web hero**, desktop (1920 wide) | ≈ 6.8% of width (≈ 130px); headline ≈ 48% | None; the site header carries the logo |
| **Web hero**, mobile | As the 9:16 story | None |
| **PDP banner** | Not used; the headline stands alone | None |

So the wordmark is proportionally a little bigger in emails, because the email headline fills more of the width. It never goes above the headline's cap height and is never full-strength white inside the lockup.

## 5. Layout and components

| Component | Class | Rules |
|---|---|---|
| Ticker strip | `.bf26-ticker` (+ `--top`, `--bottom`, `--small`, `--live`) | Full-bleed LED marquee, top and bottom edge on stories (cap height ≈ 75% of the headline's). Alternate a value message (phase accent) with a phase label (white; ink or orange in End). Starts mid-word at the edge, like a sign caught mid-scroll. Proof variant: two small strips sandwiching the headline. Live (animated) on web, email GIF and video; constant speed, so linear motion is correct here (an exception to the brand's easing rule). |
| Frame ticker | `.bf26-ticker--side` + `--left` / `--right`, with `--top` / `--bottom` | A ticker running round all four edges, with the content in rounded `.bf26-panel` blocks inside. Hype (black frame, "COMING SOON · DAY 1 CODE INSIDE") and End (orange frame, "LAST CHANCE"). |
| Starburst sticker | `.bf26-burst` (+ `--white`, `--green`) | Scalloped badge, Clash caps, tilted about 12°. Overlaps a corner of the offer or the product. One or two per piece; feature callouts may use four on an End static. |
| Product stack | `.bf26-stack` | A deep-etched folded sheet set, centred behind the lockup and about 92% of frame width, so the headline crosses the stack. Pick from `stack-cutouts.json`, never by angle alone (§6). |
| Photo ground | `.bf26-photo` | Full-bleed crumpled sheet, dark colourways, darkened. |
| Offer escalation | `.bf26-offer` + `.bf26-offer__was` | **Ending phase only, from Fri 27 Nov.** Struck-out old offer set small on top ("UP TO 54% OFF"), then the new offer big ("60% OFF"), white LED. Never shown before 27 Nov. |
| Circular callout | `.bf26-stamp` (SVG `textPath`) | LED text on a circle, the phrase repeated twice with a separator. For short urgency: DON'T MISS OUT, LOW STOCK, ENDING SOON, SELLING FAST, LAST CHANCE, DAY 1 ONLY. One per piece at most. May overlap a corner of the headline (Nick's PDP option 1); never covers the offer or the CTA. May spin slowly on web. |
| Proof block | `.bf26-proof` | ★★★★★ above one Clash line, bottom third of the frame. |
| CTA | `.bf26-cta` (+ `--led`) | White pill. Statics: LED ink text. Web: Deep Green Clash caps. Not on flat JPEGs that can't be clicked (PDP banner). |
| Countdown | `.bf26-countdown` | LED digits, Clash labels. Hype phase and web hero. |
| GWP card | `.bf26-gwp` | White rounded card: Deep Green Clash title, grey Clash small print, product cut-out. |

**Formats Nick designed:**

| Format | Size | Class |
|---|---|---|
| Story / reel | 1080×1920 | `.bf26--story` |
| Feed square | 1080×1080 | `.bf26--square` |
| Email hero | 600 wide (Nick's frames are 800) | `.bf26--email` |
| Web hero, desktop | 1920 wide, **hero only**; below-the-fold sections are the normal site | `.bf26--hero` |
| Web hero, mobile | 9:16 | `.bf26--story` |
| PDP banner | 1360×464 JPEG, below add-to-cart | `.bf26--pdp` |

## 6. Photography

Nick's photos are placeholders. Use the whole Ecoy library for variety: `assets/resolveImage.js` against `assets/cdn-catalog.json`, or `assets/library/`. Only live colourways (`assets/colour-status.json`).

- **Stack cut-outs:** use `stack-cutouts.json`, a list checked by eye. The library's `Deepetch` angle also contains boxed packaging, stool shots and some opaque white-background files, so resolving `angle: 'Deepetch'` alone gives the wrong thing about half the time. `neatStack` (the folded set with the band on top) is Nick's look.
- **Photo grounds:** CloseUp or Freestyle shots of dark colourways (Black, Charcoal, Midnight Pine, Ocean, Storm Blue, Eggplant, Merlot, Mulberry, Forest Green, dark stripes), darkened so the LED reads.
- **Pairing:** keep the stack colour clear of the ground: a dark stack on an orange or green ground, a rich colour (Merlot, Eggplant, Mulberry, Burnt Orange) on black. Rotate colourways across a set of ads; don't repeat one stack colour in a carousel.
- **Gap:** there's no clean Forest Green neat stack (Nick's Black Friday hero colour) apart from AI-01 and AI-02, which can show a blue edge. Every stack is an AI render; there is no Real neat stack yet.

## 7. Phases and copy

The phase schedule, offers, GWP tiers and copy guardrails are in **[BRIEF.md](BRIEF.md)**. In short:

| Phase | Dates | Headline | Offer on creative | Visual cue |
|---|---|---|---|---|
| Hype (white) | 2 to 4 Nov | Black Friday | "An extra 10% off on launch day"; get your code on the hidden page | COMING SOON · DAY 1 CODE INSIDE frame tickers, countdown |
| Launch, Day 1 (green) | Thu 5 Nov | Black Friday | Up to 54% off + extra 10% with your Day 1 code (**no code on public creative**) | DAY 1 ONLY / EXTRA 10% OFF tickers |
| Main sale (green) | 6 to 12 Nov, 16 to 26 Nov | Black Friday | Up to 54% off storewide, GWP tiers | SALE LIVE / SALE ON NOW tickers, proof, GWP card |
| Win Back Your Order (green) | Fri 13 to Sun 15 Nov | Black Friday | Win-back competition; own countdown to Sun 15 Nov close | Takes over homepage hero and announcement bar. **Not designed yet** (placeholders in the PGS file) |
| GWP phase 2 (green) | From Thu 19 Nov (night) | Black Friday | Tote Bag replaces Sleep Mask at $250+ | GWP card copy swap |
| Ending, BFCM weekend (FOMO, TBA) | 27 to 29 Nov | Black Friday | ~~Up to 54%~~ → up to 60% off | Orange frame, LAST CHANCE, FINAL HOURS, offer escalation, starbursts |
| Ending, Cyber Monday (FOMO, TBA) | Mon 30 Nov | **Cyber Monday** | Up to 60% off, final day | Orange ground, ink LED, ENDS TONIGHT |

"Cyber Monday" is the final day of Black Friday 2026, not a second sale.

**Copy to check in the draft statics (19 Oct)** — they are work in progress and get a resync:
- The "Hype statics" say "UP TO 54% OFF + EXTRA 10% OFF, DAY 1 ONLY" and "FREE GIFTS". BRIEF.md has no public offer before Thu 5 Nov, so as drawn these are Day 1 ads, or the hype rule needs to change. Check with James.
- "TAP TO REVEAL CODE" / "TAP FOR EXTRA 10% OFF": fine on hype ads that land on the hidden page; on Day 1 public ads the code must not appear (Launch page note).
- Old-winner static: "FREE GIFTS WORTH $XXX" and "WORTH $320" are placeholders.
- Ending statics say "60% OFF EVERYTHING"; the brief says "up to". Always "up to 60% off".

**Copy to fix in Nick's earlier frames** (placeholder or left over from earlier sales, don't copy it):
- Offers of 44%/54% and "Free Flip Cooling Pillow worth up to $119 when you spend $300" are placeholders. Use BRIEF.md: 54% main, 60% ending, GWP at $150/$250/$350.
- "USE CODE: TEN" and "EXTRA 10% OFF NEXT 10 HOURS" in an email: the real mechanic is an extra 10% for all of Day 1, and the code appears only in email, lead gen and the pop-up.
- Emails 1 and 2 say "Our EOFY Sale is here…" and "This one's only around 'til the end of financial year".
- The web heroes (desktop and mobile) say "BIRTHDAY SALE STARTS IN", and the nav pill reads "BDAY SALE".
- The web hero's below-the-fold section says "BIRTHDAY SALE COMING SOON" (not in scope; hero only).

## 8. PDP banner: recommendation

Nick drew four options (`reference/pdp-banner-01..04.webp`): (1) headline + orange circular stamp + Shop Now; (2) tickers + headline + Shop Now; (3) two GWP cards + headline + Shop Now; (4) one wide GWP card + headline + Shop Now.

**Recommended: option 4 without the Shop Now pill.** The banner sits under add-to-cart, so its job is to lift basket size, and the GWP threshold is the one message that does that at that moment. Copy from BRIEF.md: "Free Flip Cooling Pillow when you spend $350+" with "free shipping over $150" as the small print. The card changes when the Tote Bag replaces the Sleep Mask on 19 Nov only if the $250 tier is shown. One card stays legible on a phone, where the 1360px JPEG shrinks to about 360px wide; option 3's two cards drop the small print to about 7px. The pill is a false promise on a flat JPEG that can't be clicked, and the shopper is already on the product. Option 2 is the fallback if there is no GWP. **Pending Sam's pick.**

## 9. Open items

- [ ] **End/FOMO colour: TBA.** Bright Orange holds; swap `--bf26-led-orange` when it lands.
- [ ] **Resync the Static Ads page** (`2016:1141`) in a few days: the statics are drafts (Sam, 19 Oct). Rerun the export and update `reference/draft-static-*.webp` and §3.
- [ ] Pages 04 Win Back Your Order, 05 GWP Phase 2, 06 BFCM, 07 Flash Offer and 08 Christmas haven't been read yet (the first is placeholders only); add them when they're designed.
- [ ] Check that Strawberry Merlot Stripe is still a live stripe (`colour-status.json` only covers solids).

- [ ] Buy the LED Display St commercial licence.
- [ ] Confirm with James that the 60% ending step is going ahead (Notion says confirmed; Sam said "if we need to push").
- [ ] Nick to confirm the glow values.
- [ ] Sam to pick the PDP banner.
- [ ] Fix leftover EOFY / Birthday copy in Nick's frames.
- [ ] More designs from Nick are coming; add their references here and in `reference/`.
- [ ] A clean, Real Forest Green neat-stack cut-out would help.
