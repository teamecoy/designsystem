# Voice of customer: Ecoy reviews, tagged for copywriting

Every published Judge.me review (5,600, Nov 2020 to 4 Oct 2026), each one tagged by theme, persona, ad angle, product, colour and complaint, with a ready-made pull quote and an ad-readiness score. Use it to write static ad copy, headlines, PDP proof and email lines in the customer's own words, and to check what customers actually say before making a claim.

**Start with [INSIGHTS.md](INSIGHTS.md)**: the headline numbers, theme counts, complaints and the best quotes by theme. Go to `reviews.jsonl` when you need more than that.

## What's here

| File | What it is |
|---|---|
| `INSIGHTS.md` | The summary a copywriter reads first. Generated. |
| `reviews.jsonl` | One review per line, every field below. The source for queries. Generated. |
| `reviews.csv` | The same, flattened for Sheets (lists joined with `\|`). Generated. |
| `tags.json` | Every tag's regex and count, plus the persona and angle maps. Generated. |
| `build_voc.py` | Builds all four from a Judge.me export. **The only place tags are edited.** |

## Fields (`reviews.jsonl`)

| Field | Meaning |
|---|---|
| `id` | Judge.me review handle. Cite it when you use a quote. |
| `date`, `rating`, `sentiment` | Date posted; 1–5 stars; positive (4–5) / neutral (3) / negative (1–2). |
| `title`, `body` | Exactly as the customer wrote them (curly quotes straightened). |
| `pull_quote` | The single best sentence for an ad: on-theme, 20–180 characters, no complaint words. Empty if nothing qualifies. |
| `theme_quotes` | The best sentence for each theme in this review, e.g. `theme_quotes.pet`. Use this when you query by theme, so the line is actually about that theme. Same length and complaint rules. |
| `ad_score` | 0–10. 0 = not usable (under 5 stars or mentions a complaint). 8+ = 5 stars, specific, several themes, clean quote. |
| `reviewer` | First name + last initial only, e.g. "Kate M." This is the attribution to use. |
| `city`, `state`, `country` | From Judge.me. Location can come from IP, so it's sometimes overseas for an Aussie buyer. |
| `product_handle`, `product_category`, `fabric`, `is_bedding` | The product reviewed. Category: `sheet_set`, `quilt_cover`, `fitted_sheet`, `pillowcase`, `bundle`, `quilt`, `pillow`, `mattress_protector`, `mattress_topper`, `blanket`, `sleep_accessory`, `eco_lifestyle`. |
| `colours`, `retired_colour` | Colours from the survey, the text and the handle. `retired_colour: true` means don't show this quote next to that colour (see `assets/colour-status.json`). |
| `themes` | What the review talks about. See the table below. |
| `complaints` | What went wrong. See the table below. |
| `personas` | Matches the naming sheet's **Persona** field (`HotSleeper`, `PetHair`, `HomeInterior`, `SensitiveSkin`, `Allergies`, `Couple`, `FitnessRecovery`, `Eco`, `Hair`). Comes from the survey where answered, otherwise from the text. |
| `angles` | Matches the naming sheet's **Angle** field (`SocialProof`, `ComparisonClaim`, `ProblemHighlight`, `Aspiration`, `PriceLed`, `Origin`, `Trust`) that this review could support. |
| `survey` | Judge.me's optional questions, when answered: `age`, `describes_me`, `sleep_improved`, `previous_material`, `favourite_features`, `reason_for_purchase`, `sleep_position`, `previous_pillow`, `previous_quilt_filling`. |
| `has_photos`, `photo_urls` | Customer photos on Judge.me's CDN (709 reviews). UGC only with the customer's permission. |

### Themes

| Tag | Means the review talks about |
|---|---|
| `cooling` | Sleeping cool, hot sleepers, sweats, humidity, menopause. Survey hot sleepers who ticked "Temperature regulation" count too. |
| `pet` | Dogs, cats, fur, shedding, pet hair. Survey "pets that shed" + "Pet hair friendly" count too. |
| `style` | Colour, looks, the bedroom, compliments. |
| `softness` | Soft, silky, buttery, smooth, cloud. |
| `luxury` | Luxurious, hotel, premium, five-star. |
| `quality` | Quality, well made, stitching. |
| `durability` | Still good after months, years or many washes. |
| `sleep_better` | Sleeping better, through the night, waking less. |
| `skin`, `allergy`, `hair` | Sensitive skin, eczema, irritation; allergies, asthma, dust mites; frizz and bed-head. |
| `eco` | Sustainability, natural fibre, non-toxic. |
| `value` | Price, worth it, sale, investment. |
| `gift` | Bought as a present. |
| `vs_cotton`, `vs_linen`, `vs_other_brand` | Compares Ecoy with cotton, linen, or a named brand / "other bamboo". |
| `wash_care`, `fit`, `delivery`, `packaging`, `customer_service` | The practical stuff. |
| `repeat_buyer` | Second set, another colour, every bed in the house. |
| `recommend` | Recommends Ecoy, telling friends, 10/10. |
| `couple`, `kids` | Partner, husband, wife; children's beds. |
| `winter_warmth` | Warm in winter, cosy, all year round. |
| `sceptic_converted` | Was doubtful, took a chance, exceeded expectations. |
| `superlative` | Best ever, never going back, obsessed, game changer. |

### Complaints

`pilling`, `fading_colour`, `staining` (mostly oil and sweat marks on dark colours), `colour_mismatch`, `too_hot`, `shrinkage`, `thin_tear`, `wrinkles`, `fit_issue` (includes "too slippery, slides off the bed"), `delivery_issue`, `static_lint`, `smell`. Words like "no pilling" or "hasn't faded" are praise, not complaints, and are excluded.

## How to look things up

```bash
# Best 20 pet quotes on sheets
jq -c 'select(.theme_quotes.pet and .product_category=="sheet_set" and .ad_score>=7) | [.theme_quotes.pet, .reviewer, .id]' voc/reviews.jsonl | head -20

# Hot sleepers who switched from cotton
jq -c 'select(.theme_quotes.cooling and .survey.previous_material=="Cotton" and .ad_score>=7) | .theme_quotes.cooling' voc/reviews.jsonl

# Everything said about one colour
jq -c 'select(.colours|index("Mulberry")) | [.rating, .pull_quote]' voc/reviews.jsonl
```

```python
import json
R = [json.loads(l) for l in open("voc/reviews.jsonl")]
quotes = [r for r in R if "sceptic_converted" in r["themes"] and r["ad_score"] >= 8]
```

No terminal (Claude Design, a chat): read `INSIGHTS.md`, or open `reviews.csv` and filter the columns.

## Using reviews in ads: the rules

1. **Quote word for word.** You may trim with an ellipsis (…) and fix an obvious typo. Never reword, merge two reviews, or change the meaning. Keep the `id` in the handoff so anyone can check the source.
2. **Attribute as `reviewer` gives it**, with a verified-buyer cue if the design needs one ("Kate M., verified buyer"). Never the full surname, never the email.
3. **Match the product.** A quote about sheets goes on a sheets ad. `product_handle` is what they bought, but the text sometimes talks about another item, so read the full review.
4. **No retired colours.** Skip quotes with `retired_colour: true` when the ad shows that colour.
5. **Survey numbers need their base.** "90% said their sleep improved" is from the 1,926 reviewers who answered an optional question. Write it as "9 in 10 reviewers say they sleep better" and keep the base in the handoff. Don't present it as a clinical result.
6. **Headline proof is in INSIGHTS.md** (rating, review count). It changes, so re-run the build or check the site before each job. The site's own figure wins if they differ.
7. **Don't name competitors** from `vs_other_brand` quotes in paid ads. Use the comparison, not the brand.
8. **Complaints are a brief, not a secret.** Staining on dark colours, slipperiness, and the odd "not cool enough" are the top real issues. Don't claim the opposite (e.g. "never stains"). Copy that answers them honestly can work.
9. **Customer photos need permission** before they appear in an ad.

## The customer's own words

These phrases come up again and again. Use them in headlines before inventing new ones. Counts are reviews that use the phrase, from the October 2026 build.

| Phrase | Reviews |
|---|---|
| silky | 617 |
| so soft | 455 |
| luxurious | 384 |
| hot sleeper | 299 |
| best sheets (I've) ever | 263 |
| buttery | 86 |
| game changer | 77 |
| obsessed | 77 |
| never going back | 49 |
| worth every cent | 48 |
| like sleeping on a cloud | 38 |
| (dog/pet) hair slides / falls / wipes straight off | 26 |
| cool to the touch | 21 |

## Refreshing it

1. In Judge.me, export all published reviews as CSV ("Judge.me format").
2. Run `python3 voc/build_voc.py ~/Downloads/<export>.csv`.
3. Look over the themes and complaints in `INSIGHTS.md` for anything odd, then commit. **Never commit the raw export**: it has emails and IP addresses. The build drops both.

To fix a wrong tag, edit its pattern in `TAGS` inside `build_voc.py` and rebuild. Tags are keyword rules, not a model. They were spot-checked by hand (October 2026) and are accurate for the big themes. They miss some paraphrases, so complaint counts are a floor, not a ceiling.
