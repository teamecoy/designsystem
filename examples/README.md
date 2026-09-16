# Examples: real Ecoy emails that performed

Ten Klaviyo campaigns from the last 12 months (Sep 2025 to Sep 2026), chosen by revenue, revenue per recipient, open rate and click rate, then screened for design value. Each folder holds the campaign's `index.html` with every image localised into `img/`, so the design is fully self-contained. Open any `index.html` in a browser at 600px wide to see the email as sent.

**Read the "Brand status" column first.** Ecoy rebranded in February 2026. Emails marked **on-brand** show the current system (new ECOY wordmark, Malinton headings, Deep Green pill CTAs, pillar shapes, colour-blocked sections) applied well: copy their styling. Emails marked **pre-rebrand** out-performed on commercial mechanics (offer hierarchy, hype sequencing, proof tiles) but use the old logo, Montserrat and off-palette colours: copy their structure and copy, never their styling.

## Index

| Folder | Campaign · sent | Brand status | Why it's here | Copy this |
|---|---|---|---|---|
| `edm-2026-04-flannelette-launch` | Flannelette 2/6 Launch · 2026-04-30 · 75k · 35.6% open · $11.4k | **on-brand** | Highest-revenue non-sale email of the year, and the cleanest expression of the system in EDM. | Full-bleed lifestyle hero with wordmark, one eyebrow ("NEW"), Malinton headline, Deep Green pill CTA. Product shot sitting on a Light Green pillar blob. Colourway grid of labelled photo tiles. |
| `edm-2026-08-ambi-v2-launch` | Ambi v2 Launch · 2026-08-13 · 61k · 40.1% open · $7.9k | **on-brand** | Product launch for the flagship reversible stripe. Shows the review-in-a-pillar-shape device and colour-pair naming. | Lifestyle hero, "MEET THE NEW AMBI" hierarchy, customer review set inside the 8-lobe pillar flower in Deep Green, Light Pink colour-blocked section, "RICH & WARM · Merlot / Strawberry" pair labels in Burgundy and Light Pink. |
| `edm-2026-08-ambi-v2-teaser` | Ambi v2 Teaser · 2026-08-12 · 52k · 40.5% open · 1.11% CTR | **on-brand** | Best on-brand click rate. Type-as-image and the blurred-chips reveal device. | Tonal Burgundy hero with the headline as the visual, "Shop while you wait" secondary CTA, review in pillar flower, feature chips blurred behind a Bright Orange pillar sticker reading "Coming 13 August", Deep Green social-proof band with UGC grid, giant cropped ECOY wordmark as footer. |
| `edm-2026-08-fathers-day-bundle-launch` | Father's Day Bundle Launch · 2026-08-19 · 58k · **62.5% open** · $8.2k | **on-brand** | Highest open rate of the year. Only example that uses all three tag colours correctly in one email. | Bright Orange ticker bar carrying the value message, Deep Blue lifestyle hero with Off White pill CTA, Off White bundle-contents grid on a light ground, Deep Green section with an orange pillar sticker "25% OFF", social proof band. |
| `edm-2026-07-dusk-colour-launch` | Dusk launch V1 · 2026-07-28 · 30k · 42.1% open · 1.11% CTR | **on-brand** | Single-colourway launch. Shows how a section takes its tone from the product colour. | Tonal hero in the product colour, "MEET / DUSK" scale contrast, Deep Green CTA on pink, dusty-pink benefits section with three line icons, photo grid mixing product and mood (sunset) shots. |
| `edm-2026-02-bday26-sale-launch` | BDAY26 Sale launch · 2026-02-25 · 104k · 1.25% CTR · **$89.9k, #1 revenue** | pre-rebrand | Biggest revenue email of the year. The offer architecture is the lesson. | Ticker "SALE LIVE" bar, offer stack (up to X% → plus extra Y% for Z hours → code), product hero, four icon proof tiles (first sale, gifts value, customers, trial), repeated offer block with four category pill buttons. Restyle with Malinton, Burgundy urgency and Deep Green CTAs. |
| `edm-2025-11-bfcm25-launch` | BFCM25 Launch · 2025-11-05 · 73k · **$1.09 per recipient, #1** | pre-rebrand | Highest revenue per recipient. Same offer architecture as BDAY26 in a black and neon-green campaign skin. | Structure only. The black plus `#00FF9D` skin is outside the palette; the equivalent bold campaign moment today is Burgundy on Charcoal or Deep Green with Light Green. |
| `edm-2026-02-bday26-hype-3-sale-tomorrow` | BDAY26 Hype 3/3 · 2026-02-25 · 45k · 37.8% open · $40.7k | pre-rebrand | The "tomorrow" hype email that fed the #1 launch. | "SALE TOMORROW" ticker, product hero, outlined display type ("BIIIIG"), alarm-clock motif with exact drop time, Deep Green social-proof band with UGC grid and pay-later logos. That band is already on-brand. |
| `edm-2025-11-bfcm25-hype-1-offer-reveal` | BFCM25 Hype 1/3 · 2025-11-01 · 32k · **56.7% open** · 2.70% CTR | pre-rebrand | Curiosity mechanic: short email, one "Reveal offer" button. | Length and single-CTA discipline. Subject "Black Friday Sneak Peek" plus preview "Want to reveal the offer?". |
| `edm-2026-03-cofounder-letter` | Customer Research 1/3 Cofounder Letter · 2026-03-12 · 24k · 2.92% CTR · $10.3k | plain text | Best click rate outside sale periods. No design; a voice example. | First-person, short lines, one link repeated twice, plain gratitude. Shows the "warm, not corporate" voice working commercially. |

## How the visual analysis was done

The Klaviyo HTML is a table shell; almost all design lives in the images. So analysis was done on the rendered email, not the markup:

1. Every image was downloaded, converted to JPEG, capped at 900px wide and stored in `img/` (whole folder under 5 MB).
2. Each email was rendered at 600px and read as an image: hierarchy, colour blocking, CTA style, logo version, typeface, proof devices.
3. The HTML was scanned for fonts and hex values. Result: post-rebrand emails carry `#004C39`, `#F6F2E8` and `#1C1C1C` in their code; pre-rebrand ones carry `#171814`, `#EFF1F3`, `#00FF9D`, `#FF7A00`. The shell font in every Klaviyo template is Montserrat, which is not in the brand system.
4. Performance data came from Klaviyo's campaign report (Placed Order as the conversion metric, 12 months, sends over 2,000 recipients only).

## Gaps this surfaced

- Klaviyo's fallback font stack is Montserrat/Helvetica in every template. The guide names Inter as the EDM stand-in. Worth changing the Klaviyo brand fonts once.
- Sale campaigns had not yet moved to the new system as of Feb 2026. MYSALE26 (June 2026) was not pulled; check it before the next sale build.
- April Fools 2026 had the year's highest click rate (6.53%) but drew a negative reaction and is deliberately excluded.

## Adding one

1. Pick a piece you'd be happy for every future design to resemble.
2. Klaviyo: fetch the template HTML, localise the images (the script pattern is in the project history), cap images at 900px JPEG.
3. Name the folder `edm-yyyy-mm-short-slug` and add a row above with the numbers and the brand status.
