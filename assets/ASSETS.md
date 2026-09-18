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
| Colour | 33 solid, 5 stripe | Omitted where the product has no colourway |
| Angle | `High45`, `Low45`, `Overhead`, `Side`, `CloseUp`, `Freestyle`, `Deepetch` | |
| People | `NoTalent`, `Talent` | Whether a person is in shot |
| Source | `Real`, `AI` | Camera photo or AI generated |
| NN | `01`, `02`, … | Two digits, zero padded |

**Two-colour shots** join both colours with a lowercase x and no spaces: `BurntOrangexWhite`, `ByronxLagoon`. Used for reversible Ambi pairs and any styled two-colour set.

**Picking an angle.** `Deepetch` is cut out for compositing. `Overhead` is a flat lay. `Freestyle` is styled lifestyle. `CloseUp` is a fabric or detail crop. The rest are what they sound like.

The full vocabulary, including every product and colour token, is in `naming.json`.

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

Four things to know. **A missing `.webp` means not generated yet, not absent**, so always fall back to the master rather than erroring. **Three folders are permanently excluded**: `NEW IMAGERY - to be renamed`, `Archive`, and `Founder BTS & OLD Content`. **HEIC files get no web copy**, since the conversion covers only the five extensions above. And **there is no CDN**: these are Drive files, so a web copy still cannot be referenced by URL from a published page. Getting hotlinkable URLs is a separate decision.

Use the shared drive, not My Drive. A stale `Photography` folder with old year-based subfolders still exists there and should be ignored.

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

`colour-status.json` answers it. The **Cooling Bamboo Sheet Set is the north star**: if a colour is not a live sheet set option it is retired, whatever lingers on accessories. Twenty-three colours are live, ten are retired, and two live ones (Sky and Burgundy) have no vocabulary entry yet.

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

- **Polka** is a valid pattern with no Drive assets yet.
- **Combo colours have no dropdown** in the spreadsheet, so they are typed by hand and can drift. The checker validates them.
- **The spreadsheet's "How to use" tab says `Solo`** where every other tab, and every real file, says `NoTalent`. The dropdowns are right, that one tab is stale.
- **`NEW IMAGERY - to be renamed`** in Drive does not follow the convention yet.
- **Shopify product media follows no convention** (`Image_1097.jpg`, `FOREST-GREEN-QC-1X1.jpg`) and cannot be resolved from a filename. Store CDN images are also compressed and limited to a few per variant, so treat them as thumbnails, not assets.
