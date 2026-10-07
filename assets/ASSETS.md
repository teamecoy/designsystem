# Assets: where they live and how to ask for the right one

**This repository holds no photography.** The master library is Google Drive, in the Ecoy shared drive under [Photography](https://drive.google.com/drive/folders/18qRGqMBgXvmb-tKALvXgkPHhYuH6Setz). Source files run 20 to 55 MB each and the library is well over 100 GB, so it is never copied into git.

What the repo gives you instead is the **grammar**: enough to name the exact asset you need and say precisely where it sits in Drive. Name it correctly and anyone can pull it in seconds.

## Do not use these as assets

Two folders in this repo contain images. Neither is an asset library.

- `examples/*/img/` are compressed reference renders of past emails, capped at 900px. They exist so you can see what an email looked like. Never place them in a design.
- `reference/` are rendered pages of the brand guide PDF, for visual context only.

Real photography comes from Drive. Logos are in `logos/`, pillar shapes in `shapes/`, fonts in `fonts/`. Those three are genuine, reusable, and correct to use.

## The filename convention

Every image in Drive is named the same way:

```
Product-Pattern-Colour-Angle-People-Source-NN.ext
```

```
BambooSheetSet-Solid-Dusk-High45-NoTalent-Real-01.jpg
BambooSheetSet-Solid-BurntOrangexWhite-High45-NoTalent-AI-01.jpg
AmbiQuiltCover-Stripe-MatchaForestStripe-Freestyle-Talent-Real-07.jpg
CloudQuilt-Overhead-NoTalent-Real-02.jpg
```

| Part | Values | Notes |
|---|---|---|
| Product | 22 tokens, `BambooSheetSet`, `AmbiQuiltCover`, `FlannelSheetSet` … | Always first |
| Pattern | `Solid`, `Stripe`, `Polka` | Omitted for quilts, pillows, protector |
| Colour | 33 solid, 10 stripe, 5 polka | Omitted where the product has no colourway |
| Angle | `High45`, `Low45`, `Overhead`, `Side`, `CloseUp`, `Freestyle`, `Deepetch` | |
| Orientation | `Vertical`, `Horizontal` | **New 2026-09-23, new shoots only** — see below. Omitted on everything shot before that date; that's normal, not a mistake. |
| People | `NoTalent`, `Talent` | Whether a person is in shot |
| Source | `Real`, `AI` | Camera photo or AI generated |
| NN | `01`, `02`, … | Two digits, zero padded |

**Two-colour shots** join both colours with a lowercase x and no spaces: `BurntOrangexWhite`, `ByronxLagoon`. Used for reversible Ambi pairs and any styled two-colour set.

**Picking an angle.** `Deepetch` is cut out for compositing. `Overhead` is a flat lay. `Freestyle` is styled lifestyle. `CloseUp` is a fabric or detail crop. The rest are what they sound like.

**Orientation is new.** Added to the spreadsheet 2026-09-23, sitting between Angle and People: `Product-Pattern-Colour-Angle-Orientation-People-Source-NN.ext`, e.g. `BambooQuiltCover-Stripe-CookiesCreamStripe-CloseUp-Horizontal-NoTalent-AI-01.jpg`. It exists so a design brief can ask for a widescreen vs. a portrait crop of the same shot. It applies to **new shoots only** — none of the 9,233 already-indexed library files have it, and a batch rewrite of old filenames to add it has been discussed but isn't scheduled. Every parser in this repo (`build_library_index.py`, `check_filenames.py`) treats a missing orientation as normal, not invalid — never flag an old file for lacking one.

**Polka colourways are named after the dot colour on the fabric**: `EggplantPolka`, `BurgundyPolka`, `IcedChocolatePolka`, `ForestGreenPolka`, `CaramelPolka` (folders "Eggplant Polka" and so on). The first shoot, 981 images across the Sheet Set and Quilt Cover, landed 2026-09-29 and sits in the standard layout: `Bamboo Quilt Cover Set / Polka / Eggplant Polka / Talent / Vertical /`. Naming by dot colour works while every Polka product has a different dot colour; a second colourway with the same dot would need its base colour in the name too.

The full vocabulary, including every product and colour token, is in `naming.json`.

## Which angle to reach for

**High45 is the preferred angle for ads and hero creative.** When several frames of the same product and colour exist, rank High45 first, then Low45, then Side. `naming.json` records this under `library.anglePreference`.

The library does not reflect that preference yet: High45 is only 3.4% of images while Freestyle is 47.9%. Freestyle is largely a catch-all covering packaging shots, product stacks, wide room shots and styled vignettes, not a bucket of mislabelled angles, so most of it is not recoverable by renaming. Where an image has been looked at, `seen.angle` records the angle actually observed, which is more reliable than the filename.

## The curated set in this repository

`assets/library/` holds 287 photographs, and they are the only photographs in this repo (16.5 MB total). Everything else lives in Drive. They exist because Claude Design can read this repository and nothing else, so a design needing a real Ecoy photograph needs the pixels here.

They come from the human-curated shortlist in Drive at `Photography - Web/Claude Photos`, downscaled to 1200px, 2.9 MB in total. `library-shortlist.json` is the manifest: each entry carries its slot, the master it came from, dimensions, and the parsed product metadata.

```bash
python3 assets/build_shortlist.py                  # rebuild after the shortlist changes
python3 assets/build_shortlist.py --max-edge 1600  # larger, if a hero needs it
```

The build deliberately refuses two kinds of file, and records why in the manifest's `skipped` list. **A retired colourway is never copied**, so a design physically cannot show a dead SKU. **A filename that does not parse is never copied**, because it cannot be traced back to a master. Fix the name in Drive and rebuild to recover it.

## Two trees: masters and web copies

The library exists twice in the Ecoy shared drive.

| | Masters | Web copies |
|---|---|---|
| Root | `Photography` | `Photography - Web` |
| Extension | `.jpg .jpeg .png .tif .tiff` | `.webp` |
| Size | ~24 MB | ~237 KB, up to ~900 KB for texture crops |
| Longest edge | original | 2400px, aspect ratio exact |
| Use for | print, retouching | everything on screen |

**Resolving one to the other:** swap the root folder, replace the extension. The relative path and filename stem are byte-identical, so `Photography/Bamboo Sheet Set/Solid/Dusk/No Talent/…-01.jpg` becomes `Photography - Web/Bamboo Sheet Set/Solid/Dusk/No Talent/…-01.webp`. Colour profiles are preserved and rotation is baked in, so a web copy matches its master.

```bash
python3 assets/resolve_web.py "<library-relative path>"   # returns the best available file
python3 assets/resolve_web.py --coverage                  # how much of the mirror exists
```

Three things to know. **A missing `.webp` means not generated yet, not absent**, so always fall back to the master rather than erroring. **Three folders are permanently excluded**: `NEW IMAGERY - to be renamed`, `Archive`, and `Founder BTS & OLD Content`. **HEIC files get no web copy**, since the conversion covers only the five extensions above.

## The images are also on a CDN

As of 2026-09-29, 8,466 of the web copies above (every eligible one) are mirrored to the Shopify Files CDN, and every filename got there unchanged — Shopify has renamed zero of them across two runs. That means a url is **derivable from the filename alone**, with no lookup table to maintain:

```
https://cdn.shopify.com/s/files/1/0498/6100/1367/files/<filename>.webp
```

These urls need no auth, are not rate-limited, and are correct to use in email, ads and any published web page — unlike a Drive path, which is not fetchable from outside Drive at all. `naming.json` records the pattern under `library.cdn`.

**Use `assets/resolveImage.js` rather than composing that url by hand.** It looks up a real, uploaded image by product, colour and angle against `assets/cdn-catalog.json` (generated from `shopify-upload-manifest.json`, the confirmed-upload list), applying the High45-first angle preference automatically and returning `null` rather than a broken url when nothing matches:

```js
import catalog from './cdn-catalog.json'
import { resolveImage } from './resolveImage.js'

const hero = resolveImage(catalog, { product: 'BambooSheetSet', pattern: 'Solid', colour: 'Dusk' })
// hero.url -> .../BambooSheetSet-Solid-Dusk-High45-NoTalent-Real-01.webp
```

Rebuild the catalog after any upload run:

```bash
python3 assets/build_cdn_catalog.py
```

Every manifest entry is live (checked by HTTP 2026-09-29). If a future run leaves gaps, list them in `KNOWN_NOT_YET_LIVE` in `build_cdn_catalog.py` so `resolveImage` skips them. Pass `orientation: "Horizontal"` or `"Vertical"` to prefer a landscape or portrait crop; only shoots from September 2026 on carry one, and older ones are returned when nothing matches. Only the 287 in `assets/library/` also exist as pixels in this repo; everything else on the CDN exists only as a url, which is enough for anything that renders in a browser or email client.

Use the shared drive, not My Drive. A stale `Photography` folder with old year-based subfolders still exists there and should be ignored.

## After a new shoot: getting it onto the CDN

Run these in order. Steps 1, 2 and 4 are local; step 3 is the Colab notebook, which only Sam can run (it needs the Shopify secrets).

1. **Check the names.** `python3 assets/check_filenames.py "<Drive folder>"`. Fix anything it flags in Drive before going further: a CDN file can't be renamed, only replaced, so a wrong name that reaches the CDN stays there.
2. **Index, scan and queue.** `python3 assets/build_library_index.py` re-walks Drive (keeping every `seen` description). `python3 assets/scan_new_photos.py` lists what's new since the last upload, queued vs skipped with the reason, so a misnamed photo isn't silently left behind. Then `python3 assets/build_upload_manifest.py --drive` adds the new, eligible files to the manifest and copies it to `Photography - Web/`, backing up the old copy. It never changes existing entries, and it skips excluded folders (including `NEW IMAGERY - to be renamed`, the placeholder folder for colours like Sky and Burgundy), retired colours, names that don't parse, and anything on `HOLD` in the script.
3. **Let Drive finish syncing, then run the notebook** (`Photography - Web/ecoy_photography_to_shopify.ipynb`, `LIMIT = None`). It makes any missing web copies on Google's side (step 3b: 2400px, WebP quality 78, colour profile kept), then uploads everything not already in Shopify Files. It skips what's already there, so a re-run is safe.
4. **Publish the lookup.** `python3 assets/build_cdn_catalog.py`, then commit. Do this after the upload, not before, or `resolveImage` will hand out urls that don't exist yet.

**Renaming after upload.** A CDN file can't be renamed, only replaced. Rename it in Drive (master and web copy), rebuild the vocabulary and index, then run `build_upload_manifest.py --prune --drive`: the old entries leave the manifest and go on `shopify-delete-list.json`, and the new names are queued. The notebook uploads the new ones; its step 8 deletes the old ones only when Sam sets `CONFIRM_DELETE = True`, and only if that run was clean.

**Sequence numbers** are two digits, zero padded; once a shoot passes 99 frames they carry on with three (`-100`, `-101`).

## The Polka shoot (September 2026)

981 images, live on the CDN since 2026-09-29. Resolve them with `pattern: 'Polka'`:

| Token (filenames, `resolveImage`) | Shopify colour option | What it looks like | Images |
|---|---|---|---|
| `EggplantPolka` | Eggplant Polka Dot / Eggplant Solid | eggplant dots on pink; solid eggplant reverse | 245 |
| `BurgundyPolka` | Burgundy Polka Dot / Burgundy Solid | burgundy dots on cream; solid burgundy reverse | 162 |
| `IcedChocolatePolka` | Chocolate Polka Dot / Chocolate Solid (the token stays IcedChocolatePolka on purpose) | chocolate dots on ice blue; solid chocolate reverse | 185 |
| `ForestGreenPolka` | Forest Green Polka Dot / Forest Green Solid | forest dots on mint; solid forest reverse | 183 |
| `CaramelPolka` | Caramel Polka Dot / Caramel Solid | caramel dots on cream; solid caramel reverse | 206 |

```js
resolveImage(catalog, { product: 'BambooQuiltCover', pattern: 'Polka', colour: 'CaramelPolka', orientation: 'Vertical', people: 'Talent' })
```

**Products.** Photographed as `BambooQuiltCover` (818) and `BambooSheetSet` (163). On Shopify, Polka is five new colour options on the existing "(New Colours)" products (Reversible Quilt Cover, Pillowcase Set, Fitted Sheet, Flat Sheet), not new products. The quilt cover is reversible, polka on one side and solid on the other, and `BambooQuiltCover` is its correct token. `AmbiQuiltCover` is only the reversible *stripe*. A single draft product, "Cooling Bamboo Sheet Set | Forest Green Polka dot", also exists.

**What was shot** (checked by eye 2026-09-29: every close-up, overhead, side and 45° frame, and a 1-in-9 sample of the lifestyle frames):
- Styled beds from every angle, shown both ways up (polka face and solid face), including turn-backs that show the solid reverse.
- 548 quilt-cover lifestyle frames with talent (lying, reading, jumping, holding pillows, smoothing the quilt). The sheet set has no talent frames.
- 15 close-ups, all fabric texture and drape. None for Eggplant or Burgundy on the quilt cover.

**Not shot, so it's a gap for AI fill or a reshoot:**
- Deep-etch cut-outs of any kind, including stacked sets (0 `Deepetch` frames).
- Packaging (none seen).
- Zip and loop details (none seen).
- Hands fitting a fitted-sheet corner (not in any close-up or sampled lifestyle frame; the nearest is hands smoothing the quilt top).
- A dedicated binding detail. Turn-backs show the solid reverse at bed scale, but no close-up shows the dot binding on the solid face.

## Where it sits in Drive

```
Photography / {Product} / {Pattern} / {Colour} / {Talent | No Talent} / {file}
```

For example `BambooSheetSet-Solid-Dusk-High45-NoTalent-Real-01.jpg` lives at
`Photography / Bamboo Sheet Set / Solid / Dusk / No Talent /`.

Folder names are written for humans and keep their spaces, so the `Burnt Orange` folder holds files whose token is `BurntOrange`, and the `No Talent` folder holds `NoTalent` files. Compare them with spaces removed.

## How to use this when designing

1. Decide what the design needs: which product, colourway, angle, with or without a person.
2. Compose the filename from the table above.
3. Reference that exact filename in the design and say which Drive folder it comes from.

Never invent a colour. If it is not in `naming.json` it is not a live colourway, and someone has to confirm it before it is used. Never substitute a compressed reference image because the real one is not to hand.


## The library index

`library-index.json` is a structured index of all 9,233 files in the Drive library: 8,983 images and 250 videos. Every field is parsed from the filename, so building it opened no images and cost nothing but a directory walk.

Use it to find assets without touching Drive. Each row carries the relative path plus whichever of product, pattern, colour, angle, people, source, orientation and sequence the filename declared. A row marked `"valid": false` has an `unknown` list naming the tokens that did not parse.

```bash
python3 assets/build_library_index.py            # rebuild after new shoots land
python3 assets/build_library_index.py --reparse  # re-derive fields after a vocabulary change, no re-walk
```

It reads the library from the Google Drive for Desktop mount, so Drive for Desktop must be running.

### What has been looked at

336 images, one per unique combination of product, pattern, colour, angle and talent, have been viewed and carry a `seen` object recording what is genuinely in the frame: the subject, the colours actually visible, the setting, whether a person appears, whether the branding looks dated, and a quality grade of hero, solid or weak. Retired colourways were skipped.

Of those: 110 grade hero, 207 solid, 19 weak. 22 carry the old lowercase wordmark. `flagged-images.csv` lists every image needing a look before reuse, with the reason.

Prefer `seen.quality` of hero for anything leading a page, and never ship an image whose `seen.dated` is true without checking the branding.

**A filename is not a description.** The index tells you what someone typed, not what is in the frame. A file named `BambooPillowcase-Solid-Charcoal-Deepetch-NoTalent-Real-01.png` turned out to be a photo of a packaging box carrying the old logo. Always confirm the image before shipping it.

## Is this colour still for sale?

`colour-status.json` answers it. The **Cooling Bamboo Sheet Set is the north star**: if a colour is not a live sheet set option it is retired, whatever lingers on accessories. Twenty-five colours are live and ten are retired. Sky and Burgundy got their vocabulary entries on 2026-09-29; their photos are still in `NEW IMAGERY - to be renamed`, waiting to be renamed.

This matters because 1,140 images in the library, about one in eight, shoot retired colours. Paprika alone accounts for 536 and Canyon 290. Never design bedding around a colour listed as retired.

Refresh it by querying the Shopify Admin API for active products and reading the sheet set's Colour option values, then rewriting the file. Do not scrape the storefront: automated requests to ecoy.com.au trip bot protection for the whole office.

## Renaming work

`rename-suggestions.csv` lists files whose names can be corrected without a judgement call, mostly stripe colourways recorded under half their pair name. Each row gives the folder, the current name and the name to use. It is regenerated whenever the index is rebuilt.

## Checking filenames

For renaming work, this checks a single name or a whole folder and says exactly what is wrong:

```bash
python3 assets/check_filenames.py "/path/to/folder"
```

## Keeping the vocabulary current

`naming.json` is generated from the VA's spreadsheet at `assets/source/Ecoy_Photography_Filename_Generator.xlsx`, which stays the single source for product and colour names. When a colour or product is added there, regenerate and commit:

```bash
python3 assets/build_naming.py
```

Never hand-edit `naming.json`.

## Known gaps

- **Combo colours have no dropdown** in the spreadsheet, so they are typed by hand and can drift. The checker validates them.
- **The spreadsheet's "How to use" tab says `Solo`** where every other tab, and every real file, says `NoTalent`. The dropdowns are right, that one tab is stale.
- **`NEW IMAGERY - to be renamed`** in Drive does not follow the convention yet.
- **Shopify product media follows no convention** (`Image_1097.jpg`, `FOREST-GREEN-QC-1X1.jpg`) and cannot be resolved from a filename. Store CDN images are also compressed and limited to a few per variant, so treat them as thumbnails, not assets. (This is unrelated to the Shopify Files CDN mirror above, which is our own upload and does follow the filename convention exactly.)
