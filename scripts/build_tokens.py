#!/usr/bin/env python3
"""Single source of truth for Ecoy design tokens.

Edit the dicts below, run `python3 scripts/build_tokens.py`, and both
css/tokens.css and tokens.json are regenerated. Never hand-edit those two.

Sources: Ecoy_Rebrand_2026_V2.pdf (guide) and Tag & Chip Spec v0.1 (spec).
Anything marked tbc=True is a proposal awaiting Ecoy confirmation.
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- colours (guide p17)
COLORS = {
    "deep-green":     {"hex": "#004C39", "cmyk": [100, 0, 35, 57], "name": "Deep Green",     "role": "Primary dark ground. Headings on light, hero and footer fills, primary CTA, newness tags, active filter pills."},
    "off-white":      {"hex": "#F6F2E8", "cmyk": [0, 2, 6, 4],     "name": "Off White",      "role": "Primary light ground. Page background, text on dark grounds, light CTA on dark."},
    "bright-orange":  {"hex": "#FF6301", "cmyk": [0, 61, 100, 0],  "name": "Bright Orange",  "role": "Accent only, never a foundation. Eyebrows, hand-drawn accents, value tags (discounts, best seller)."},
    "burgundy":       {"hex": "#A30042", "cmyk": [0, 86, 54, 32],  "name": "Burgundy Red",   "role": "Expressive campaign colour. Urgency tags (sale, last chance, low stock)."},
    "light-green":    {"hex": "#A3C2A7", "cmyk": [16, 0, 14, 24],  "name": "Light Green",    "role": "Soft ground and pillar-shape fill; pairs with Deep Green and Deep Blue."},
    "light-blue":     {"hex": "#A5CAD9", "cmyk": [24, 2, 0, 14],   "name": "Light Blue",     "role": "Soft ground; pairs with Deep Blue."},
    "light-pink":     {"hex": "#FFBAB5", "cmyk": [0, 27, 29, 0],   "name": "Light Pink",     "role": "Soft ground and pillar-shape fill; pairs with Burgundy and Chocolate."},
    "chocolate":      {"hex": "#583200", "cmyk": [0, 43, 100, 65], "name": "Chocolate Brown","role": "Warm dark ground; pairs with Light Pink."},
    "deep-blue":      {"hex": "#0F6A91", "cmyk": [90, 27, 0, 43],  "name": "Deep Blue",      "role": "Cool dark ground; pairs with Light Blue and Light Green."},
    "charcoal":       {"hex": "#1C1C1C", "cmyk": [0, 0, 0, 89],    "name": "Charcoal Black", "role": "Near-black ink and monochrome ground. Body text on light, high-contrast alt on orange."},
}

# Derived neutrals (not in the guide; proposed for UI states). tbc flags them.
DERIVED = {
    "neutral-fill":   {"hex": "#E9E5DB", "name": "Neutral fill",  "role": "Filter pill at rest. Spec says 'pull from live site'; this is an Off White shade proposed until confirmed.", "tbc": True},
    "neutral-fill-hover": {"hex": "#D8D3C6", "name": "Neutral fill hover", "role": "Filter pill hover: neutral fill darkened ~8% per spec proposal.", "tbc": True},
    "deep-green-hover": {"hex": "#003D2E", "name": "Deep Green hover", "role": "Primary CTA and active pill hover: Deep Green darkened ~8%.", "tbc": True},
    "white":          {"hex": "#FFFFFF", "name": "White", "role": "Text on saturated tag fills. Pure white, not Off White, so the spec's contrast ratios hold."},
}

# Approved pairings as shown on guide p18 (ground -> accents). Order matches the slide.
PAIRINGS = [
    {"id": "green-lightgreen",      "ground": "deep-green",    "accents": ["light-green"]},
    {"id": "burgundy-pink-orange",  "ground": "burgundy",      "accents": ["light-pink", "bright-orange"]},
    {"id": "lightblue-deepblue",    "ground": "light-blue",    "accents": ["deep-blue"]},
    {"id": "chocolate-pink",        "ground": "chocolate",     "accents": ["light-pink"]},
    {"id": "lightgreen-deepblue-green", "ground": "light-green", "accents": ["deep-blue", "deep-green"]},
    {"id": "orange-burgundy",       "ground": "bright-orange", "accents": ["burgundy"]},
    {"id": "deepblue-lightblue",    "ground": "deep-blue",     "accents": ["light-blue"]},
    {"id": "pink-burgundy-chocolate","ground": "light-pink",   "accents": ["burgundy", "chocolate"]},
    {"id": "offwhite-charcoal",     "ground": "off-white",     "accents": ["charcoal"]},
    {"id": "charcoal-offwhite",     "ground": "charcoal",      "accents": ["off-white"]},
]

# ---------------------------------------------------------------- type (guide p22, spec §06, §04)
FONTS = {
    "display": {"family": "Malinton", "fallback": "'Fredoka', 'Nunito', system-ui, sans-serif", "role": "Primary. Headlines, subheads, body, campaign, packaging. Default everywhere."},
    "text":    {"family": "Satoshi",  "fallback": "'Inter', system-ui, -apple-system, sans-serif", "role": "Supporting. Small sizes, dense information, legibility-critical, all tags and functional UI text. Inter is the Google-safe stand-in, mandatory in EDM."},
}
TYPE_RULES = {"line-height": 1.2, "line-height-legible": 1.4, "letter-spacing": "-0.02em", "tag-line-height": 1.0}
TYPE_SCALE = {  # token: (desktop px, mobile px, weight, family key, use)
    "h1":    (40, 32, 700, "display", "Page and hero headings"),
    "h2":    (28, 24, 700, "display", "Section headings"),
    "h3":    (20, 18, 600, "display", "Card and product titles"),
    "body":  (16, 15, 400, "text",    "Paragraphs, descriptions"),
    "price": (16, 15, 600, "text",    "Prices"),
    "small": (13, 13, 400, "text",    "Meta, captions, strikethrough prices"),
}
TAG_SCALE = {  # fixed across breakpoints (spec §04)
    "lg": (14, 500, "Filter pills"),
    "md": (13, 600, "On-image badges"),
    "sm": (12, 600, "Inline tags (nav, price)"),
}
WEIGHTS = {"regular": 400, "medium": 500, "semibold": 600, "bold": 700}

# ---------------------------------------------------------------- shape + spacing (spec §02, §05; guide visuals)
RADIUS = {"badge": "8px", "pill": "999px", "card": "24px", "card-sm": "16px", "button": "999px"}
TAG_PADDING = {"badge": "6px 14px", "inline": "4px 10px", "filter": "10px 20px"}
BUTTON = {"padding": "14px 28px", "padding-sm": "10px 20px", "min-height": "44px"}
SPACE = {"1": "4px", "2": "8px", "3": "12px", "4": "16px", "5": "24px", "6": "32px", "7": "48px", "8": "64px", "9": "96px"}

# ---------------------------------------------------------------- motion (guide p33; numbers are our proposal)
MOTION = {
    "ease": "cubic-bezier(0.4, 0, 0.2, 1)",
    "ease-out": "cubic-bezier(0, 0, 0.2, 1)",
    "duration-fast": "150ms", "duration-base": "250ms", "duration-slow": "400ms",
}

# ---------------------------------------------------------------- tag taxonomy (spec §01)
TAG_CATEGORIES = {
    "urgency": {"fill": "burgundy",     "text": "white", "examples": ["Last chance", "Sale", "Low stock"], "rule": "Time-bound only. Burgundy only."},
    "value":   {"fill": "bright-orange","text": "white", "examples": ["30% off", "Best seller"],           "rule": "Commercial benefit only. Bright Orange only. White text is the brand exception (3.0:1); use charcoal text where legibility is critical."},
    "newness": {"fill": "deep-green",   "text": "white", "examples": ["New", "New colours"],               "rule": "New products or colourways. Deep Green only. Consolidate from the current orange/burgundy split."},
    "filter":  {"fill": "neutral-fill", "text": "charcoal", "active-fill": "deep-green", "active-text": "white", "examples": ["Sheets", "Quilts", "Best Sellers"], "rule": "Interactive pills for browsing. Never a badge, never carries urgency or value copy."},
}

# ================================================================ writers
def css():
    L = ["/* Ecoy design tokens. GENERATED by scripts/build_tokens.py from the brand guide (Rebrand 2026 V2) and Tag & Chip Spec v0.1. Do not hand-edit; edit the script. */", ":root {"]
    L.append("  /* Colour: brand palette (guide p17) */")
    for k, v in COLORS.items():
        L.append(f"  --color-{k}: {v['hex']};")
    L.append("  /* Colour: derived UI neutrals. TBC = proposed, awaiting Ecoy confirmation */")
    for k, v in DERIVED.items():
        L.append(f"  --color-{k}: {v['hex']};" + ("  /* TBC */" if v.get("tbc") else ""))
    L.append("  /* Colour: semantic roles */")
    L += ["  --color-ground: var(--color-off-white);",
          "  --color-ground-dark: var(--color-deep-green);",
          "  --color-ink: var(--color-charcoal);",
          "  --color-ink-on-dark: var(--color-off-white);",
          "  --color-heading: var(--color-deep-green);",
          "  --color-accent: var(--color-bright-orange);",
          "  --color-primary: var(--color-deep-green);",
          "  --color-primary-hover: var(--color-deep-green-hover);  /* TBC */",
          "  --color-tag-urgency: var(--color-burgundy);",
          "  --color-tag-value: var(--color-bright-orange);",
          "  --color-tag-newness: var(--color-deep-green);",
          "  --color-tag-filter: var(--color-neutral-fill);  /* TBC */",
          "  --color-tag-filter-hover: var(--color-neutral-fill-hover);  /* TBC */",
          "  --color-tag-filter-active: var(--color-deep-green);"]
    L.append("  /* Colour: approved pairings (guide p18). ground / accent(s) */")
    for p in PAIRINGS:
        L.append(f"  --pair-{p['id']}-ground: var(--color-{p['ground']});")
        for i, a in enumerate(p["accents"], 1):
            L.append(f"  --pair-{p['id']}-accent{'' if i == 1 else i}: var(--color-{a});")
    L.append("  /* Type: families (guide p22) */")
    for k, v in FONTS.items():
        L.append(f"  --font-{k}: '{v['family']}', {v['fallback']};")
    L.append("  /* Type: rules (guide p22, spec §02) */")
    L += [f"  --line-height: {TYPE_RULES['line-height']};",
          f"  --line-height-legible: {TYPE_RULES['line-height-legible']};",
          f"  --line-height-tag: {TYPE_RULES['tag-line-height']};",
          f"  --letter-spacing: {TYPE_RULES['letter-spacing']};"]
    for k, v in WEIGHTS.items():
        L.append(f"  --weight-{k}: {v};")
    L.append("  /* Type: site scale, desktop (spec §06). Mobile values swap in below 768px */")
    for k, (d, m, w, f, use) in TYPE_SCALE.items():
        L.append(f"  --text-{k}-size: {d}px;")
        L.append(f"  --text-{k}-weight: {w};")
        L.append(f"  --text-{k}-family: var(--font-{f});")
    L.append("  /* Type: tag scale, fixed across breakpoints (spec §04) */")
    for k, (s, w, use) in TAG_SCALE.items():
        L.append(f"  --tag-{k}-size: {s}px;")
        L.append(f"  --tag-{k}-weight: {w};")
    L.append("  /* Shape (spec §02, §05) */")
    for k, v in RADIUS.items():
        L.append(f"  --radius-{k}: {v};")
    for k, v in TAG_PADDING.items():
        L.append(f"  --tag-{k}-padding: {v};")
    for k, v in BUTTON.items():
        L.append(f"  --button-{k}: {v};")
    L.append("  /* Space */")
    for k, v in SPACE.items():
        L.append(f"  --space-{k}: {v};")
    L.append("  /* Motion (guide p33 principles; durations are our proposal) */")
    for k, v in MOTION.items():
        L.append(f"  --motion-{k}: {v};")
    L.append("}")
    L.append("@media (max-width: 767px) {")
    L.append("  :root {")
    for k, (d, m, w, f, use) in TYPE_SCALE.items():
        if m != d:
            L.append(f"    --text-{k}-size: {m}px;")
    L.append("  }")
    L.append("}")
    return "\n".join(L) + "\n"

def w3c():
    def c(v, extra=None, tbc=False, desc=None):
        t = {"$type": "color", "$value": v}
        ext = dict(extra or {})
        if tbc: ext["status"] = "tbc"
        if ext: t["$extensions"] = {"com.ecoy": ext}
        if desc: t["$description"] = desc
        return t
    out = {"$schema": "https://tr.designtokens.org/format/", "$description": "Ecoy design tokens v0.1. Generated by scripts/build_tokens.py. Sources: Ecoy Rebrand 2026 V2 brand guide, Tag & Chip Spec v0.1.",
           "color": {}, "font": {}, "typography": {}, "tag": {}, "radius": {}, "space": {}, "motion": {}, "pairing": {}}
    for k, v in COLORS.items():
        out["color"][k] = c(v["hex"], {"name": v["name"], "cmyk": v["cmyk"], "source": "guide p17"}, desc=v["role"])
    for k, v in DERIVED.items():
        out["color"][k] = c(v["hex"], {"name": v["name"], "source": "derived"}, tbc=v.get("tbc", False), desc=v["role"])
    for k, v in FONTS.items():
        out["font"][k] = {"$type": "fontFamily", "$value": [v["family"]] + [s.strip().strip("'") for s in v["fallback"].split(",")], "$description": v["role"]}
    out["typography"]["rules"] = {"line-height": {"$type": "number", "$value": TYPE_RULES["line-height"]},
                                  "line-height-legible": {"$type": "number", "$value": TYPE_RULES["line-height-legible"]},
                                  "letter-spacing": {"$type": "dimension", "$value": TYPE_RULES["letter-spacing"]}}
    for k, (d, m, w, f, use) in TYPE_SCALE.items():
        out["typography"][k] = {"$type": "typography", "$description": use,
            "desktop": {"$value": {"fontFamily": "{font." + f + "}", "fontSize": f"{d}px", "fontWeight": w, "lineHeight": TYPE_RULES["line-height"], "letterSpacing": TYPE_RULES["letter-spacing"]}},
            "mobile":  {"$value": {"fontFamily": "{font." + f + "}", "fontSize": f"{m}px", "fontWeight": w, "lineHeight": TYPE_RULES["line-height"], "letterSpacing": TYPE_RULES["letter-spacing"]}}}
    for k, (s, w, use) in TAG_SCALE.items():
        out["tag"][k] = {"$type": "typography", "$description": use, "$value": {"fontFamily": "{font.text}", "fontSize": f"{s}px", "fontWeight": w, "lineHeight": TYPE_RULES["tag-line-height"], "letterSpacing": TYPE_RULES["letter-spacing"]}}
    out["tag"]["category"] = {k: {"fill": {"$type": "color", "$value": "{color." + v["fill"] + "}"}, "text": {"$type": "color", "$value": "{color." + v["text"] + "}"},
                                  **({"active-fill": {"$type": "color", "$value": "{color." + v["active-fill"] + "}"}, "active-text": {"$type": "color", "$value": "{color." + v["active-text"] + "}"}} if "active-fill" in v else {}),
                                  "$description": v["rule"], "$extensions": {"com.ecoy": {"examples": v["examples"], "source": "spec §01"}}} for k, v in TAG_CATEGORIES.items()}
    out["tag"]["padding"] = {k: {"$type": "dimension", "$value": v} for k, v in TAG_PADDING.items()}
    for k, v in RADIUS.items():
        out["radius"][k] = {"$type": "dimension", "$value": v}
    for k, v in SPACE.items():
        out["space"][k] = {"$type": "dimension", "$value": v}
    for k, v in MOTION.items():
        out["motion"][k] = {"$type": "duration" if "duration" in k else "cubicBezier", "$value": v, "$extensions": {"com.ecoy": {"status": "tbc", "source": "guide p33 gives principles, not numbers"}}}
    for p in PAIRINGS:
        out["pairing"][p["id"]] = {"ground": {"$type": "color", "$value": "{color." + p["ground"] + "}"}, "accents": [{"$type": "color", "$value": "{color." + a + "}"} for a in p["accents"]], "$extensions": {"com.ecoy": {"source": "guide p18"}}}
    return json.dumps(out, indent=2, ensure_ascii=False) + "\n"

if __name__ == "__main__":
    (ROOT / "css").mkdir(exist_ok=True)
    (ROOT / "css" / "tokens.css").write_text(css())
    (ROOT / "tokens.json").write_text(w3c())
    print("wrote css/tokens.css and tokens.json")
