# Photography

## Rules

**Filenames are structured**, so you can read an image without opening it: `Product-Pattern-Colour-Angle-Talent-Source-NN.webp` for the files here; CDN files also carry an orientation after the angle (`BambooSheetSet-Solid-Burgundy-High45-Vertical-NoTalent-Real-01.webp`). `Real` is a photograph; `AI` is generated. `NoTalent` has no person in frame.

**No third-party brands in shot** (Oct 2026). Crop or swap any frame showing another brand's logo or product (e.g. a designer bag on a shelf).

**What the ad says must match the photo** (Oct 2026). Shoots are styled with 4 pillows but a sheet set includes 2 pillowcases: don't print a count the photo contradicts.

## Every other Ecoy photo: resolve it, don't upload it

The full 9,233-file Drive library is mirrored on the Shopify Files CDN, including colours that are **not yet live on ecoy.com.au** (e.g. Burgundy, Oct 2026). "Not on the website" never means "no photos": always search the CDN before Drive or asking anyone for uploads. Any of these three routes works; use whichever your session has.

**1a. With the `teamecoy/designsystem` repo attached:** `assets/resolveImage.js` looks a photo up against `assets/cdn-catalog.json`. Call it with a product, pattern, colour and angle; it returns a live `https://cdn.shopify.com/...` url, or `null` if that combination hasn't been shot.

**1b. With the Shopify connector (no repo needed):** query Shopify Files by filename, e.g. `files(first: 250, query: "filename:*Solid-Burgundy*") { edges { node { ... on MediaImage { image { url } } } } pageInfo { hasNextPage endCursor } }`, paginating with `after`. Each result's url is the live CDN url.

**1c. With neither (no repo, no Shopify connector):** CDN files are public, no login needed, at `https://cdn.shopify.com/s/files/1/0498/6100/1367/files/<filename>.webp` (cdn.shopify.com is on Ecoy's network allowlist). Use only filenames a person, a listing or one of the routes above has given you; ask a teammate to run 1b and paste the list if you have none. Suggest connecting Shopify for next time.

Never invent a filename or hand-type a CDN url: use only urls these routes return.

**2. Drive, only when every CDN route comes back empty.** That means the photo genuinely isn't on the CDN yet. Only then find the exact filename in the repo's `assets/library-index.json` (it encodes product, pattern, colour, angle, talent, and Real vs AI), and confirm it isn't a retired colourway in `assets/colour-status.json`. Drive needs the person's own @ecoy.com.au account (connector or Google Drive for desktop); if the connector shows no shared drive it's signed in to the wrong account. An agent that can't reach Drive asks someone with Drive connected to pull the file, convert it to WebP, and add it to this group.

**3. Never generate or approximate a photo.** If it can't be resolved and isn't in Drive, say so.
