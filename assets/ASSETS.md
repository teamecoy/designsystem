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
