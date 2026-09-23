# Ads: how to read an Ecoy ad name, and what to do with a winner

This folder makes Ecoy's Meta ads readable to the design system: what an ad name means, whether an ad was a sale, a promotion or evergreen, whether it was designed or made by a creator, and which real photography matches its colour. A winning-ads log, fed by Motion, will sit alongside it (planned; see "Coming next").

## What's here

| File | What it is |
|---|---|
| `source/naming-sheet.md` | A snapshot of the **Ecoy Naming Convention Generator** Google Sheet, the single source for ad-name vocabulary. Never hand-edit. |
| `build_ad_naming.py` | Turns the snapshot into `ad-naming.json`. |
| `ad-naming.json` | The vocabulary as data: every field and its allowed values, the glossary, which campaign moments are sales, and a lookup from ad colour names to photo colour names. Generated. |
| `parse_ad_name.py` | Reads any ad name into structured fields. Handles all three naming styles in real use. |

## Always pull the sheet fresh

The sheet ([Ecoy Naming Convention Generator](https://docs.google.com/spreadsheets/d/1Hi0_UgLseaj4UphXm9ApcWh18AXYWKh_vwPcy2xsTYI/edit), file `1Hi0_UgLseaj4UphXm9ApcWh18AXYWKh_vwPcy2xsTYI`) changes as the team adds options. Before relying on the vocabulary, re-pull it:

1. Read the sheet through the Google Drive connector (`read_file_content` keeps the columns aligned; a plain text export does not).
2. Save the Reference table and the Glossary over `source/naming-sheet.md`.
3. Run `python3 ads/build_ad_naming.py` and commit.

## The three naming styles

```bash
python3 ads/parse_ad_name.py "<ad name>"          # read one or more names
python3 ads/parse_ad_name.py --report names.txt   # summarise a list, one name per line
```

| Style | Looks like | Notes |
|---|---|---|
| **v2** (since May 2026) | `2026-September-Static-EmilieCS-Untested-Problemaware-HomeInterior-USP-Static-Evergreen-Bamboo-Sheets-Eggplant-DanicaDesigner-V5-JOB-3318-4x5` | 18 fields, hyphen-separated, in the order in `ad-naming.json`. |
| **legacy** (before May 2026) | `2026-Feb-Video-AMBI-AlexCS-Untested-Newrelease-Sheets-MixedColours-Greg-V1-JOB-1843` | Shorter, looser. **Never rename these.** |
| **creator** | `2026_July_@emcombsfitness_Productaware_Lifestyle_CP-UGC_Bamboo_Sheets_CherryBlossom_9x16` | Identified by the `@handle`; usually underscores. Not covered by the sheet. |

The parser recognises each word by its vocabulary, not its position, because real names drop fields, add spaces ("Cherry Blossom") and reorder. Words it can't place are kept in `unknown`, never dropped. Names with no convention at all (mostly Shopify collection ads, "– Copy 3") come back as `unparsed`, with any recognisable colour or product kept in `hints`.

**Dimensions are often blank at ad level** (the name ends `JOB-2788-`) because one ad serves several ratios. That's expected, not an error.

## Sale, promotion or evergreen

The `CampaignMoment` field says which, and it decides the rulebook:

| Type | Moments | Design rule |
|---|---|---|
| **Sale** | EOFY, BlackFriday, CyberMonday, BFCM, BoxingDay, **Christmas**, SpringSale, WinterSale, SummerSale, MidyearSale, BirthdaySale | The sale's own **Sale Identity Brief**. |
| **Promotion** | MothersDay, FathersDay, Valentines, Easter | The **Ecoy brand system**, like evergreen. Promotions are not sales. |
| **Evergreen** | Evergreen, NewRelease, Restock, AmbiLaunch, CordLaunch, CollabPost, PartneredAd, Seeding | The **Ecoy brand system** exactly. |

Not yet placed: ANZACDay, AustraliaDay, NewYear, Bundles. The parser returns `unknown` for them rather than guessing.

**Never learn from a sale ad as if it were evergreen.** A price-led Spring Sale static can post 9.56 ROAS; that says nothing about how an evergreen ad should look.

## Designed ads and creator ads

- **Designed ads** (statics, GIFs, agency and designer videos): the design system can make these.
- **Creator ads** are real footage from Ecoy's creator program, which Emilie manages. The design system **cannot** make them; the most it can do is brief ideas to creators. The parser marks an ad `creator` when its name has an `@handle` or `CP-UGC`, or its moment is CollabPost, PartneredAd or Seeding.

## The iteration rule

**For every winner, ask: how do we turn this into another 5 ads?** Iteration is the core of the SOP for winners. The name's `Concept` field records how a new ad relates to an old one: `Iteration` (builds on something that worked), `WinnerClone` (same hook, different creator), `Refresh` (winner edited for fatigue).

- A **winning designed ad** becomes five variations: new colourways, formats (Static, GIF, Carousel), ratios, angles or personas, keeping what made it win.
- A **winning creator ad** can't be reshot by the system, but its **hook or concept can be iterated into statics** and designed ads, and briefed back to creators as new takes. Motion transcribes each creator's spoken hook, which is exactly the raw material for both.

## From an ad colour to real photography

Ad names and photo filenames spell colours differently (`CookiesAndCream` vs `CookiesCreamStripe`). `ad-naming.json` → `colourToPhoto` maps each ad colour to its photo colour, and the parser returns it as `photoColour`, ready for `assets/resolveImage.js`. It also flags retired colours (Canyon, Moss, Paprika, Wildberry, Honeycomb, Rockmelon): an old winner in a retired colour is a lesson, never something to recreate in that colour.

## Known gaps

- **The "forecast parser" the sheet mentions doesn't exist.** The sheet's instructions say "the forecast parser handles both" old and new names, but no such parser was found. `parse_ad_name.py` is that parser now; the sheet's line should point here.
- **Four colour aliases are guesses** to confirm: CookiesAndCream → CookiesCreamStripe, PeachStripe → BurntPeachStripe, ChocolateIced → IcedChocolateStripe, Coconut → SageCoconutStripe.
- **The sheet is missing StrawberryMerlot**, which real names use (`StrawberryAndMerlot`) and photography has (`StrawberryMerlotStripe`).
- **The glossary defines values the dropdowns lack**: TopOfFunnelTest, Refresh, Brandaware, CoupleSleeper, Eco, Allergies, BFCM. The parser accepts them.
- **"New Release"** (an Angle) has a space, against the sheet's own no-spaces rule, and collides with the `NewRelease` moment. The parser only reads it as an Angle when the space is there.
- **Creator ads have no naming standard**, and some have no convention at all (`2026-04-@ugc.byemiliee-ambi-cheryblossom-styling`).

## Coming next

The winning-ads log: a monthly pull from Motion of every ad over the spend bar in the last 90 days, ranked by ROAS against the account average, each tagged by this parser, with thumbnails, stats, Motion's creative summary and spoken hook, a "tested and lost" section, and five iteration ideas per winner.
