# Christmas 2026 · floating gift shots with a ribbon

How to make a new floating product shot wrapped as a gift, for when the board doesn't already have the colour or pattern you need. Approved by Sam on 4 Nov 2026. Look at `reference/approved-ribbon-stack.webp` before you start: every new shot has to match it.

**Use this when** someone asks for "another colour with a ribbon", "a stripe/polka version of the gift stack", "wrap the [colour] sheet set", or any floating gift shot that's missing from the set.

## The approved look

| | Rule |
|---|---|
| Ribbon colour | **White** satin (Sam prefers white over red). Use cream `#F6F2E8` only on very light fabrics, where white disappears |
| Top piece | Ribbon wraps around it with **one full bow** on top: two plump loops, two tails with angled cut ends |
| Middle and bottom pieces | Ribbon over the **side ends only** (it wraps the short ends). **No band across the front face, and no bow** |
| Front face | Always clean: the fabric and the small dark green Ecoy tag stay visible |
| Background | Plain light grey `#EEEEEE`, so the shot can be cut out |

## Before you start

1. **Colour check:** the colour must be live in `assets/colour-status.json`. Never wrap a retired colourway.
2. **Source:** start from a real pack shot (stack cut-out) of that exact colour and pattern from the CDN (`assets/resolveImage.js`). Never ask the AI to invent the product. Stripes and polka dots must come from the photo, because the AI draws them wrong (see the pattern render rules).
3. **Model:** Higgsfield Nano Banana 2.1, image edit at 2k, with the pack shot as image 1 and `reference/approved-ribbon-stack.webp` as image 2.

## The prompt

Fill in the `[brackets]`. Send it in one go; don't build it up over several edits.

```
Photo edit of image 1, a folded [colour] [pattern, e.g. solid / stripe / polka]
bamboo [product, e.g. sheet set stack]. Keep the bedding EXACTLY as it is: same
shape, same folds, same fabric colour and pattern, same lighting, same framing,
and keep the small dark green ECOY tags exactly as they are.

Wrap it as a gift to match the ribbon style of image 2:
- TOP piece: a white satin ribbon wraps around it, with one neat full bow on top
  (two plump loops, two tails with angled cut ends).
- MIDDLE and BOTTOM pieces: white satin ribbon wraps over their SIDE ENDS only.
  NO ribbon band across their front faces, and NO bows on them.
Realistic satin sheen, the ribbon follows every fold and edge and tucks slightly
under each layer, with soft shadows either side.

Smooth, silky bamboo sateen, no coarse or grainy weave. Plain light grey seamless
background #EEEEEE, soft contact shadow under the product only. No other objects,
no text, no extra tags. Photorealistic.
```

For a single item (pillowcase pair, one folded quilt cover): drop the middle/bottom lines and use "a white satin ribbon wraps around it with one neat full bow on top."

## Known failure modes (check every output)

| Failure | Fix |
|---|---|
| Bows on the middle and bottom pieces | Edit: "remove the bows on the middle and bottom pieces; the top bow stays" |
| A ribbon band across the front of the lower pieces | Edit: "erase the vertical ribbon bands on the front faces of the middle and bottom pieces, restoring the plain fabric; the ribbons over the side ends stay" |
| Red or cream ribbon when you asked for white | Say "white satin" twice and add image 2 |
| Tag repainted or misspelt ("ECOV") | Re-run the edit, or patch the tag from the source pack shot |
| Stripes or dots redrawn, warped or wrong scale | Throw it out and start again from the real pack shot. Never accept AI-drawn pattern |
| Gifts cross-tied inside a tote | Don't generate totes with gifts. Composite a real tote photo with floating cut-outs |

## Cut-out (don't skip)

1. Run Higgsfield `remove_background`, then clean the edge band (`cutclean.py` method: key out the backdrop colour in a 10px edge band only, never a global colour key, which eats white sheets and bows).
2. **Zoom to 5x on a red ground** and check the top edge, the bow and the ribbon ends for grey or white halos before you use it anywhere.
3. Save it as WebP and name it by the photography naming grammar (`assets/naming.json`) with Source `AI`.
