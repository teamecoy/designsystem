# Christmas 2026 · sale identity

Christmas 2026, BOGO 50%, running Tue 1 to Mon 21 Dec 2026, straight after Black Friday. Designed by Sam on a concept board, not by an agency: there is no Figma file. The source is the board `releases/christmas-2026/concepts/christmas-concepts.html` in the Ecoy Web Development folder, published as the claude.ai artifact `JvFQ3ir24nmFMRg89NzHTu` (v84, 4 Nov 2026). Codified here on 2026-11-04 so Claude Design, Alex's `generate-static-ads` skill and the website plugin (`ecoy-sale-rollout`) can make new pieces that belong to the same campaign.

**This is a sale identity, not the brand system.** Inside this sale, this file overrides `BRAND.md` wherever they disagree. None of it carries into evergreen work after 21 Dec, and the Boxing Day Sale (from Tue 22 Dec) has its own brief. See [BRAND.md](../../BRAND.md#start-here-is-this-sale-or-evergreen). Unlike most sales, this one uses the **evergreen brand fonts and brand colours only**; what makes it Christmas is the wrapping paper, the ribbon and the copy.

**What to say, and when, is in [BRIEF.md](BRIEF.md)** (offer, phases, email plan, guardrails), a snapshot of Sam's Notion brief. Read it before writing any copy.

Load `sale.css` and put `.xm26` on an ancestor (the page body or a wrapper). Live demos: `components/templates.html` (every format in both phases, at production sizes) and `components/callouts.html` (the global rules: formats, accent rule, ribbon, paper scale, callouts, lockup). Campaign assets (ribbon renders, paper tiles, symbols) are in `assets/`; photos load from the Shopify CDN. New ribbon renders: [FLOATING-RIBBON-PROMPT.md](FLOATING-RIBBON-PROMPT.md).

**For the website** (`ecoy-sale-rollout`): there is no sale font and no `logo/` folder; the theme already loads Malinton and Satoshi, and the lockup is the Ecoy wordmark. Copy only the blocks you need from `sale.css` into the theme's `assets/sale.css` as named blocks (its `@import` and font paths are for this repo). Upload the paper tiles and any renders to Shopify Files first and point at the CDN, never at this repo. Site pills and product badges stay evergreen (TAGS-AND-CHIPS.md); only campaign artwork (heroes, banners, bars, callouts in creative) uses this identity.

**Rebuilding:** `build/build_from_board.py` regenerates `sale.css`, `components/` and `assets/` from the board after board edits. The Markdown files, `assets/assets.json` and `reference/` are kept by hand.

**Every piece belongs to one phase: launch (Tue 1 to Tue 15 Dec) or last chance (Wed 16 to Mon 21 Dec).** The phase sets the grounds, the paper colour and the button colours (§3).

---

## 1. The idea in one line

**"One for them, one for you."** Ecoy is the gift: our bedding wrapped like a present in a white satin ribbon, on Christmas wrapping paper made from Ecoy's own pillar shapes. BOGO 50% and the free Tote support the gifting story; they never lead on depth (Black Friday ran up to 64% off).

## 2. Type

Evergreen brand fonts only, loaded from `../../fonts/` by `sale.css`. No licences to buy.

| Role | Font | Setting |
|---|---|---|
| **Headline** | Malinton Bold 700 | Sentence case, tracking -0.03em, line-height 1. Three lines at most; two is better. Feed 10cqw, story 10.5cqw. |
| **Offer and sub-lines** | Malinton SemiBold 600 | "Buy 1, Get 1 50% Off", "One for them, one for you". |
| **Pills and buttons** | Malinton Bold 700 | Always wrap the label in `<span class="pt">`: Malinton's capitals sit high, and `.pt` drops them 0.09em so the text looks centred (measured 4 Nov). No pill without it. |
| **Small print** | Satoshi Medium 500 | 30px or more on a 1080px frame (3cqw feed, 3.6cqw story). |
| **Callout type** | Malinton Bold | Inside the flower shape: "BOGO / 50% / Off", "Order by / 18 Dec", "FREE / TOTE", "Last / chance". |
| **Email live text** | Inter | Klaviyo shell font for body, buttons, product names and prices. Malinton headlines ship as image blocks. |

Rules:
- Headlines are a feeling or a gift line ("One for them. One for you.", "The best present is a sleep-in", "Under the tree in time?"), never a discount headline at launch. The offer sits in the pill.
- Never set body copy in Malinton, and never set a headline in Satoshi or Inter.

## 3. Colour on type

**No new colours.** Every colour is a brand token from `css/tokens.css`: Deep Green `#004C39`, Burgundy `#A30042` (the "red"), Off White `#F6F2E8`, Light Green `#A3C2A7`, Light Pink `#FFBAB5`. `sale.css` maps them as `--deep-green`, `--burgundy`, `--off-white`, `--light-green`, `--light-pink`. Bright Orange is not used in this sale.

### 3.1 The phase rule

| Phase | Dates | Main grounds | Paper | Labels, panels, bands | Red is for |
|---|---|---|---|---|---|
| **Launch** | Tue 1 to Tue 15 Dec | **Deep Green, Off White or Off White paper.** Burgundy is never a launch ground. | Off White paper (`assets/wrap-offwhite.svg`) | **Deep Green** ("live is Deep Green, not red", Sam 4 Nov) | Buttons, callouts, small gift tags, accent words |
| **Last chance** | Wed 16 to Mon 21 Dec | **Light Pink is the main ground.** Never Deep Green or Off White as the main colour. | Burgundy paper (`assets/wrap-burgundy.svg`) | Off White labels on red paper; Burgundy small panels | Burgundy is the paper and the small elements: callouts, tags, icons, peels, small panels |

The switch on 16 Dec keeps layout, product and headline; the date goes into the pill ("Order by Fri 18 Dec"). After the 18 Dec shipping cutoff the message moves to the 30% gift voucher (21 Dec).

### 3.2 Accent rule: the ground sets the type colours

| Ground | Headline | Accent line / word | Small print |
|---|---|---|---|
| Off White (and Off White paper) | Deep Green | Burgundy | Deep Green or Burgundy |
| Deep Green | Off White | Light Green | Light Green |
| Burgundy (callouts and small panels) | Off White | Light Pink | Off White |
| Light Pink (last chance) | Burgundy | Deep Green | Deep Green |
| Photo wall (full-screen photos) | Off White | Burgundy for one word (e.g. "Free") | Off White |

### 3.3 Buttons: one dark and one light per phase

| Phase | Dark (default) | Light |
|---|---|---|
| Launch | Burgundy, Off White text, on every launch ground | Off White, Burgundy text, only inside a red label or callout |
| Last chance | Deep Green, Off White text, on Light Pink, red paper, Off White labels and photos | Off White, Deep Green text, only where a Deep Green panel can't be avoided |

No pink, Light Green or outlined buttons. CTA copy: **"Shop Christmas"** (never "Shop the gift guide"); "Shop now" and "Shop all bedding" are fine in emails.

## 4. Lockup and logo

**There is no sale name.** The lockup is the Ecoy wordmark (the real `logos/*.svg`, also `#ecoy` in `assets/symbols.svg`) over the offer: short form "BOGO 50%" for stamps, bars and story tops; long form "Buy 1, Get 1 50% Off" where there's room.

| Channel | Logo width | Where |
|---|---|---|
| Ads, feed 4:5 | 18cqw | Top centre, or inside the label or band |
| Ads, story 9:16 | 24cqw | Top centre, below the 14% safe zone |
| Email (600) | 20% of width | Its own Off White block above the hero |
| Web hero (1920) | 8cqw inside the label | Label top-left |
| Web hero mobile (390) | 20cqw inside the label | Label top |
| Full-screen photo | 14 to 16cqw, Off White | On the wall above the product |

The logo never sits on a busy photo: on photo-led frames it moves into the band or label.

## 5. Layout and components

All classes are scoped `.xm26 <class>`. Sizes are cqw of the frame (`container-type: inline-size`).

| Component | Class | Rules |
|---|---|---|
| **Frame** | `.f.feed` (4:5), `.f.story` (9:16), content in `.in` | Feed: 8% margins. Story: keep the top 14% and bottom 20% clear (`.safe` guides; `#board.hide-safe` hides them). Headline, offer and logo take their own height; the product fills the rest. |
| **Wrapped product** | `.prod > img` (an `assets/hf-*.webp` cut-out) | Top piece tied with a white satin ribbon and bow; every lower piece has a white ribbon over its side end only, never across the front. Mid to deep colours so the white reads. **A product never sits on its own colour.** |
| **Fan of three** | `.prod.fan` + `img.side.l`, `img.mid`, `img.side.r` (add `.cut` for cut-outs) | One hero in front, two smaller ones behind, left and right (Tote story, "Still one to wrap?"). |
| **Wrapping paper** | `.paper` (full paper), `.pp > .pin` (full border), `.paperf > .ph` (photo in a paper border) | The core graphic. The paper tiles are the brand's lobed, eight-lobe and pinched pillar shapes. |
| **Torn corner (peel)** | `span.peel.{tr,br,bl,tl}` (+ `.sm` 13cqw, `.sm2` 18cqw) with `.ptear`, `.pcorner` (paper image), `.pflap` | Flap colour follows the ground via `--fl1/--fl2/--fl3`. Needs clear space: never on a callout, copy, a face or the product. Vary the corner across a set. |
| **Label** | `.label` (statics), `.wlabel` (web), `.baselabel` | Holds the copy on paper. Launch: Deep Green. Last chance: Off White on red paper. |
| **Ribbon band** | `.rib.h`, `.rib.v`, `.wrib`, `.wribv` | Runs behind the label, centred on it. |
| **Callout** | `.stampx` with `<svg><use href="#blob"/></svg>` (or `#blob-lobed` on paper) and `.st > .s1/.s2/.s3` | **Always an approved brand shape, never a circle or a random blob.** One per ad. Launch: red with Off White and Light Pink type ("BOGO 50% Off"). Last chance: "Order by 18 Dec"; on heroes a Light Pink "Last chance" callout with Burgundy type (`.lcall`). Product tiles: a small corner callout (`.pcall`). Tote: "FREE TOTE" (`.tcall`, `.tcall2`). |
| **Arrow and doodles** | `svg.hand-drawn` | From the design system glyph library only (`components/hand-drawn.html`). The only arrow is the straight one (`M12 58V4M4 14 12 4l8 10`), rotated to point. 2.5px non-scaling stroke, round caps, charcoal on light or photo grounds, no shadow. |
| **Gift tag** | `.tagbox > .thread + .bigtag > .fld(.k,.v) + .ps` | To/From tag; on Off White it turns Burgundy. Last chance: the postage label (Order by / Arrives / Postage). |
| **Photo with band** | `img.photo` + `.band` | Christmas morning. Copy sits in a solid band, never on the photo. |
| **Icon row** | `.busy .bicons > .ic` | The three facts on busy ads: Free shipping $200+, Ends Mon 21 Dec (or Order by 18 Dec first in last chance), Free Tote $300+. |
| **Email** | `.em` (600 wide) and `.em.mob` (375 wide) | Blocks: `.ebar`, `.elogo`, `.ehero`, `.blk`, `.steps`, `.sum`, `.prods`, `.tote`, `.ship`, `.count`, `.post`, `.foot`. `.em.mob` scales live text ×1.45 so Inter body stays about 15px on a phone, stacks two-column blocks and lists products one per row with a description and "Shop now →". |
| **Web hero** | `.wp` (1920×720), `.wfs` (full-screen hero, 1.4% paper border), `.wpm` (mobile 390×640, `.fsm` for the full-screen version) | Paper ground, solid label, product on the paper. Mobile stacks the gift on top and the label below, with the ribbon (`.wribv`) running down behind both. |
| **Announcement bar** | `.pbar` (+ `.m` for 390 mobile), `.obar` (ad overlay 1080×100) | Text always on a solid pill. Launch light bar over dark sections, dark bar (`wrap-dark.svg`, Deep Green paper, red blobs) over light paper sections. Last chance: red bar, or the pink bar (`wrap-pink.svg`) over red paper. |

**Formats**

| Format | Size | Class |
|---|---|---|
| Feed post | 1080×1350 | `.f.feed` |
| Story / reel cover | 1080×1920 | `.f.story` |
| Email | 600 wide (desktop), 375 (mobile) | `.em`, `.em.mob` |
| /christmas hero | 1920×720 | `.wp`, `.wfs` |
| Mobile hero | 390×640 | `.wpm` |
| Announcement bar | full width × about 44px | `.pbar` |
| Ad overlay banner | 1080×100 | `.obar` |

### 5.1 The five formats

Use all five across an ad set for variety (examples at the top of `templates.html`):

1. **Gift-wrapped product.** The workhorse for product and offer ads, including the BOGO explainer.
2. **Christmas morning.** Real shoot photos of a lie-in; copy in a solid band.
3. **Wrapping paper.** The core graphic: a label on the present. Every banner, hero and bar.
4. **Gift tag.** Copy-led: To/From, the shipping date, the postage label.
5. **Full-screen photo with a paper border.** Photo-led ads and heroes still carry the paper.

### 5.2 The paper scale: nothing goes out without one of three

| Level | What | Default use |
|---|---|---|
| Torn corner | `.peel` on a plain ground | Busy ads, stories, Tote photos, photo-with-band frames |
| Full border | `.pp`, `.paperf` | Product, offer and photo-led posts, email blocks, **full-screen photos (always the border, never the peel)** |
| Full paper | `.paper`, `.wp` | Site heroes, banners, announcement bars, the strongest ads |

In last chance the paper turns Burgundy at every level. On stories the paper stays outside the copy so the safe zones stay clear.

## 6. Photography

**Real photos and approved renders only, never placeholders or AI-invented product.**

- **Shoot photos** load from the Shopify CDN (`assets/assets.json` lists every one used, mapped to its CDN file). Room shots: Midnight Pine quilt cover with a mug (`BambooQuiltCover-Solid-MidnightPine-Freestyle-Talent-Real-17`), Forest Green sheet set overhead (`BambooSheetSet-Solid-ForestGreen-Overhead-Talent-Real-01`), Forest Green Polka jump (`…ForestGreenPolka-Freestyle-Vertical-Talent-Real-46`), Burgundy Polka mug (`…BurgundyPolka-Freestyle-Vertical-Talent-Real-58`), Burgundy quilt cover room (`…Solid-Burgundy-Freestyle-Horizontal-Talent-Real-01`).
- **Tote photos** are real and untouched: AllColours line-up and talent, MatchaForest, OatmealCharcoal and EggplantPink (High45, overhead, close-up, talent). Never AI-render a gift inside a Tote: the model cross-ties the ribbons. Composite a real Tote photo with a floating cut-out instead. `assets/cut-tote-matcha.webp` is the real Matcha High45 shot cut out.
- **Ribbon renders** (`assets/hf-*.webp`, Nano Banana edits of our pack shots, cleaned): Forest Green, Burgundy, Midnight Pine, Caramel, Sky, Sage, Jacaranda (quilt cover stacks), Burgundy sheet set stack, Forest Green pillowcases, Strawberry Merlot Stripe (light face), plus the Deep Green linen gift box: closed, open with white sheets, and open with Iced Chocolate stripe (`hf-box-open-icedchoc.webp`). New colours or patterns: follow [FLOATING-RIBBON-PROMPT.md](FLOATING-RIBBON-PROMPT.md).
- **Pack shots** (statics on studio stools): Iced Chocolate Polka, Blooming Pink Stripe, Malt Caramel Stripe (CDN `…Packshot…`).
- **Every cut-out** is checked at 5x on red before use (no grey or white halo), see FLOATING-RIBBON-PROMPT.md.
- Only live colourways (`assets/colour-status.json`); none of the colours used here is retired (checked 4 Nov).
- **Copy never sits on a talent's face. Always show the product:** a tall photo goes side by side rather than in a thin crop.

## 7. Phases

| Phase | Dates | Headline | Offer on creative | Visual cue |
|---|---|---|---|---|
| Launch | Tue 1 to Tue 15 Dec | Gift lines ("One for them. One for you.", "The gift they'll sleep in") | "Buy 1, Get 1 50% Off" / "BOGO 50% Off" pill or callout; "Free Tote Bag on $300+" | Off White paper, Deep Green labels, red buttons |
| Last chance | Wed 16 to Mon 21 Dec | "Last call for Christmas", "Under the tree in time?", "Still one to wrap?" | "Order by Fri 18 Dec" in the pill; "BOGO 50% ending soon" | Light Pink grounds, Burgundy paper, green buttons |
| After the cutoff | Sat 19 to Mon 21 Dec | Gift voucher | "30% Off Christmas Gift Voucher" (21 Dec, mechanic TBC) | Last-chance look |

Copy that is approved on the board: "One for them, one for you", "The gift they'll sleep in", "The best present is a sleep-in", "Do not disturb until Boxing Day", "The gift bag's on us", "Free tote with your new bed sheets on $300+ orders", "Wrapped. Bagged. Sorted.", "Room for one more", "A bag for both", "Happy Christmas x" (gift tags), "Last call for Christmas", "Final parcels ship 18 December", "BOGO 50% Off until 21 Dec", "Order by Fri 18 Dec for cutoff", "Shop Christmas".

## 8. Picks Sam has made

All made on the board on 4 Nov: the accent rule, live is Deep Green, last chance is Light Pink with Burgundy paper, the tie (bow on top, ribbon over the lower pieces' sides), white ribbons, callouts on the brand shapes, the paper scale, the button rules, and that shoppers choose their Tote colour.

## 9. Open items

- [ ] **Tote stock** after Black Friday phase 2 before leading with it, and whether **"Worth $70"** is the real value (only the full-screen Tote static says it).
- [ ] **18 Dec shipping cutoff** to be checked against Malpa's guidance (the brief flags it too).
- [ ] **Ribbon band colour in live:** the desktop heroes use Deep Green bands; Sam asked for Burgundy on the two mobile heroes (4 Nov). Pick one rule for both.
- [ ] **AI stripes:** the Strawberry Merlot Stripe ribbon render and the Iced Chocolate stripe gift box were checked against the real fabric by eye (thin-thick-thin clusters), but they are AI edits. Sam to sign them off before paid use.
- [ ] **Mobile email product descriptions** ("Fitted, flat and pillowcases in silky, cooling bamboo", "Reversible quilt cover with matching pillowcases", "The cool side of the pillow, in your colour") need Sam's OK.
- [ ] **Publish the renders to the Shopify CDN** (photo CDN publish skill) before the website uses them, named by the photography grammar with Source `AI`. Until then they live only in `assets/`.
- [ ] **Not designed yet:** the pop-up ($30 gift card, mechanic TBA in the brief), the 21 Dec gift voucher creative, the /christmas landing page and gift guide, the nav treatment.
- [ ] `STAGES.md` (the website plan) is written by the `ecoy-sale-rollout` skill, not here.
