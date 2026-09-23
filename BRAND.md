# Ecoy Brand

Distilled from the Ecoy Rebrand 2026 V2 brand guide (Version 1.0, 33 pages). Page numbers in brackets. Tokens and classes live in `css/`; this file is the why behind them.

## Start here: is this sale or evergreen?

This is the first question for any Ecoy design, before layout, colour or copy. The answer decides which rulebook applies.

**Evergreen** (everything that is not a named sale: product launches, colour drops, brand content, site, packaging, retention emails, always-on ads) follows this design system exactly. Palette, Malinton and Satoshi, pillar shapes, pill buttons, tag taxonomy, motion. Consistency is the point: the brand should be instantly recognisable across every evergreen touchpoint.

**Promotions** (Mother's Day, Father's Day, Valentine's Day, Easter: gift- or bundle-led moments that are not a sitewide sale) are **not sales**. They follow this design system, like evergreen, with the moment carried by copy, product and styling rather than a sale identity. An ad's `CampaignMoment` says which of the three it is; see [ads/ADS.md](ads/ADS.md).

**Sales** (Black Friday, Cyber Monday, Boxing Day, Christmas, Birthday Sale, Mid Year Sale, EOFY, Spring, Winter and Summer sales, flash sales) get their **own creative identity**, briefed per sale in a Sale Identity Brief. Each sale is an event with a name, theme, look and stamped sale logo, so the campaign cuts through and reads as one thing across paid, email, organic and site. The sale identity, not this system, is the source of truth for that sale's look. What stays constant inside a sale:

- The Ecoy wordmark is featured in the sale logo lockup, so spend builds brand equity.
- The brand palette is the sandbox the sale's designer works within; they define how many colours and how they are used per channel and per phase.
- Three switchable phases: Hype, Sale Live, End of Sale. Same offer, recoloured announcement bars, headlines and "last chance" callouts.
- Voice and honesty rules. The offer architecture (headline discount, timed boost, code, proof tiles) is proven and reused.
- Nothing from a sale identity carries into evergreen afterwards, and no two sales share a look.

Rule of thumb: if the piece would still make sense with the discount removed, it is evergreen and this system applies. If it only exists because of the sale, the Sale Identity Brief applies. The brief is produced with the `ecoy-sale-identity` skill; past briefs are the reference for depth and house style.

## Who we are (p3–p10)

Ecoy is more than bedding. It's a mindset, a promise of better comfort and sleep. "We make naturally better sleep simple. So every night feels calmer, softer, and made for you." (p4)

**Character (p6):** Comfort · Bold · Warm · Natural · Honest · Thoughtful · Modern.

**Values (p7)**
- **Comfort-first.** Every decision starts with how it feels. If it doesn't feel good at night, it doesn't belong.
- **Honest.** Clarity over hype. Natural materials, straightforward benefits, no unnecessary complexity.
- **Modern.** Bold but never loud. Warmth balanced with clarity. Considered, calm, relevant, without chasing trends.
- **Purpose-led.** Everything serves better rest. Meaningful improvements, not gimmicks.

**The four pillars of sleep (p9):** Climate (temperature, airflow), Comfort (softness, weight, fit), Light (calm, visual softness, less stimulation), Function (durability, performance, thoughtful details). "Better sleep comes from getting the fundamentals right." Each pillar has a shape and a colour, see Pillar shapes.

## Voice (p8)

Calm, confident, considered. Tone shifts with the moment; character stays.

| Pillar | We are | Not |
|---|---|---|
| Grounded | clear · warm · natural | complicated · corporate · forced |
| Confident | assured · considered · trusted | loud · salesy · trendy |
| Warm | friendly · supportive · relaxed | fluffy · instructional · rigid |
| Modern | minimal · current · confident | cold · fleeting · chaotic |

No jargon, no exaggeration. Say more by saying less. Copy rules for landing pages (honesty, no em dashes, rounded stats) live in the landing-page-builder skill.

## Messaging (p10)

- **Primary:** Naturally better sleep, designed for real life.
- **Secondary:** Sleep made comfortable · Cooling where it counts · Designed for hot sleepers · Built for better nights · Comfort that lasts · Rest deeper. Wake better. · Because your bed deserves better.
- **Descriptive:** Ecoy creates bedding designed to work naturally with your body, supporting deeper, more comfortable sleep night after night. From breathable, temperature-regulating fabrics to thoughtful construction and fit, our products are made to feel right, not just look good. We focus on the fundamentals of great sleep: comfort, climate, light, and function. No gimmicks. No excess.

## Logo (p12–p15) · `components/logo.html`

A word mark. Bold, rounded forms for softness, warmth and confidence. Always clear, uncluttered, given space.
- **Clear space:** 100% of logo height on every side, every configuration (p13).
- **Colour:** dark logo on light grounds, light on dark; black or white where contrast is limited; over photography only in low-noise areas with real contrast, add an overlay if needed. Clarity first (p14).
- **Never:** transparency, stretching, effects or shadows, rotation, outlines, another typeface (p15).
- Files: `logos/logo-deep-green.svg`, `logo-white.svg`, `logo-black.svg`.

## Colour (p17–p19) · `components/colors.html`

Warm, confident, considered. Grounded natural tones with bolder expressive ones: calm where it matters, expressive where it counts.

| Colour | Hex | Role |
|---|---|---|
| Deep Green | `#004C39` | Primary dark ground, headings, primary CTA, newness tags |
| Off White | `#F6F2E8` | Primary light ground, text on dark |
| Bright Orange | `#FF6301` | Accent only, never a foundation. Eyebrows, value tags, hand-drawn accents |
| Burgundy Red | `#A30042` | Expressive campaign colour, urgency tags |
| Light Green | `#A3C2A7` | Soft ground, pillar fill |
| Light Blue | `#A5CAD9` | Soft ground |
| Light Pink | `#FFBAB5` | Soft ground, pillar fill |
| Chocolate Brown | `#583200` | Warm dark ground |
| Deep Blue | `#0F6A91` | Cool dark ground |
| Charcoal Black | `#1C1C1C` | Ink, monochrome ground |

**Rules (p18):** pair rich, deep tones with light neutrals; bright colours as accents, not foundations; softer pairings lead in product, editorial and functional contexts; bolder combinations for campaigns. Every combination must support legibility and hierarchy. The ten approved pairings are tokens (`--pair-*`) and are drawn on `components/colors.html`.

**In practice (p19):** full colour-blocked screens (Deep Green hero with Light Green headline; Chocolate ground with Light Pink statement shape; Off White ground with Deep Green headline and a circled word in orange).

## Typography (p21–p22) · `components/type.html`

One typeface creates one clear voice. Type is a core brand asset, not decoration.
- **Malinton** leads everywhere: headlines, subheads, body, campaign, packaging.
- **Satoshi** is a tool, not a second personality. Allowed when size gets small, information density increases, or legibility is critical (print, packaging, functional UI, all tags).
- **Inter** is the Google-safe stand-in for Satoshi and is mandatory in EDM.
- Leading 120%, raise to 140% for legibility. Tracking −2% on everything.
- Type can be scaled, cropped, layered or pushed to the edge for impact in campaign and digital work, balanced with restraint.
- Site scale (from the tag spec §06): h1 40/32, h2 28/24, h3 20/18, body 16/15, price 16/15, small 13. Desktop/mobile, in `css/tokens.css`.

## Visual assets (p24–p26)

**Pillar shapes** (`components/pillar-shapes.html`, `shapes/`): five scalloped blobs, the visual foundation of the brand. Frame content, support layouts, or act as bold moments. Scale, crop, stack or gently distort; keep the core form recognisable. Climate green, Comfort burgundy, Light orange, Function blue.

**Photography (p25):** real moments of rest, grounded and warm, never over-styled. Product shots clean and considered, letting material, form and quality speak.

**Feature chips** (`components/feature-chips.html`): stack, group or place over imagery. Support the message, never dominate. Short, scannable copy; consistent spacing; never overcrowd.

**Hand-drawn accents** (`components/hand-drawn.html`): circled words, arrows, zzz. Only to direct attention or guide flow, never decoration. Subtle scale, consistent line weight.

**UI vocabulary seen across the guide:** fully rounded pill buttons, big rounded cards (24px), colour-blocked sections, chips over hero imagery.

## Motion (p33) · `components/motion.html`

Quiet, confident, thoughtful. Natural over mechanical (always easing, never linear). Purposeful (if it doesn't add clarity or hierarchy it isn't needed). Soft timing and restraint (short and subtle beats long and exaggerated). Consistent across text, chips and UI. Durations in tokens are our proposal, see CHANGELOG.

## Brand in practice (p28–p31)

References, not templates: outdoor billboard on Chocolate with Light Pink headline and blob-masked photography; Deep Green packaging with a repeating pillar pattern in Light Green and Off White; social tiles on Deep Blue with Light Blue and Burgundy statement shapes; a Burgundy 8-lobe flower carrying "Make every night of sleep count". Rendered in `reference/`.
