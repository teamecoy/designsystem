#!/usr/bin/env python3
"""Turn a Judge.me "all published reviews" export into the tagged VoC library.

    python3 voc/build_voc.py ~/Downloads/<judgeme-export>.csv

Writes voc/reviews.jsonl, voc/reviews.csv, voc/tags.json and voc/INSIGHTS.md.
The raw export is never committed: it holds emails and IP addresses. This script
drops both and shortens names to "First L." before anything is written.

Tags are rules, not a model: survey answers where the reviewer gave them, plus
regex over title + body. Every tag's pattern lives in TAGS below, so a miss is
fixed here and the library rebuilt. Read VOC.md for what each field means.
"""
import csv, json, re, sys, collections, statistics
from pathlib import Path

HERE = Path(__file__).resolve().parent

# ---------------------------------------------------------------- products
# product_handle -> (category, fabric). Order matters: first match wins.
PRODUCT_RULES = [
    (r"fur-friendly.*quilt", "quilt_cover", "bamboo_fur_friendly"),
    (r"fur-friendly", "sheet_set", "bamboo_fur_friendly"),
    (r"flannelette-quilt", "quilt_cover", "flannelette"),
    (r"flannelette-fitted", "fitted_sheet", "flannelette"),
    (r"flannelette-pillow", "pillowcase", "flannelette"),
    (r"flannelette", "sheet_set", "flannelette"),
    (r"corduroy", "quilt_cover", "corduroy"),
    (r"linen-bamboo-blanket", "blanket", "linen_bamboo"),
    (r"flip-quilt-cover|quilt-cover", "quilt_cover", "bamboo_sateen"),
    (r"bundle|dream-box", "bundle", "bamboo_sateen"),
    (r"fitted-sheet", "fitted_sheet", "bamboo_sateen"),
    (r"flat-sheet", "flat_sheet", "bamboo_sateen"),
    (r"sheet-set", "sheet_set", "bamboo_sateen"),
    (r"pillowcase", "pillowcase", "bamboo_sateen"),
    (r"mattress-protector", "mattress_protector", "bamboo"),
    (r"mattress-topper", "mattress_topper", "bamboo"),
    (r"cloud-quilt", "quilt", "cloud"),
    (r"(all-seasons|summer|midseason)-bamboo-quilt", "quilt", "bamboo_fill"),
    (r"pillow", "pillow", "bamboo"),
    (r"sleep-mask|linen-spray|linen-care", "sleep_accessory", ""),
    (r"shipping-insurance", "non_product", ""),
    (r"toothbrush|straws|cutlery|cotton-buds|hair-brush|floss|water-bottle", "eco_lifestyle", ""),
]
BEDDING = {"sheet_set", "quilt_cover", "fitted_sheet", "flat_sheet", "pillowcase", "bundle", "blanket"}

# Live + retired colourways (assets/colour-status.json) plus older names seen in reviews.
COLOURS = {
    "Forest Green": r"forest(?:\s*green)?", "Burnt Orange": r"burnt\s*orange", "Ocean": r"ocean",
    "Charcoal": r"charcoal", "Sage": r"sage", "Oatmeal": r"oatmeal", "White": r"\bwhite\b",
    "Black": r"\bblack\b", "Burgundy": r"burgundy", "Butter": r"\bbutter\b", "Caramel": r"caramel",
    "Chocolate": r"chocolate", "Dune": r"\bdune\b", "Dusk": r"\bdusk\b", "Eggplant": r"eggplant",
    "Iceberg": r"iceberg", "Jacaranda": r"jacaranda", "Lagoon": r"lagoon", "Matcha": r"matcha",
    "Merlot": r"merlot", "Midnight Pine": r"midnight\s*pine", "Mulberry": r"mulberry",
    "Reef Teal": r"reef(?:\s*teal)?", "Sky": r"\bsky\b", "Storm Blue": r"storm\s*blue",
    "Byron": r"\bbyron\b", "Canyon": r"\bcanyon\b", "Eucalyptus Green": r"eucalyptus",
    "Grey Gum": r"grey\s*gum", "Honeycomb": r"honeycomb", "Moss": r"\bmoss\b",
    "Paprika": r"paprika", "Rockmelon": r"rockmelon", "Taupe": r"taupe", "Wildberry": r"wildberry",
    "Dusty Pink": r"dusty\s*pink", "Polka": r"polka", "Stripe": r"stripe",
}
RETIRED = {"Byron", "Canyon", "Eucalyptus Green", "Grey Gum", "Honeycomb", "Moss", "Paprika",
           "Rockmelon", "Taupe", "Wildberry", "Dusty Pink"}

# ---------------------------------------------------------------- tags
# themes: what the review is about. complaints: what went wrong.
# Patterns run case-insensitive over "title. body".
TAGS = {
  "themes": {
    "cooling": r"\bcool(?:er|est|ing|s)?\b|hot sleeper|run(?:s|ning)? hot|night sweats?|sweat(?:y|ing|s)?\b|temperature|breathab|\bheat\b|humid|stay(?:s|ed)? cool|\bclammy|hot (?:nights?|summer|weather)|aussie summer|menopaus|hot flush",
    "pet": r"\b(?:dogs?|cats?|pets?|pupp(?:y|ies)|pups?|kittens?|kitty|doggo|pooch|fur ?bab(?:y|ies)|furr(?:y|ies)|fur\b|shed(?:s|ding|der)?\b|pet hair|dog hair|cat hair|paws?|claws?|greyhound|labrador|retriever|husky|cavoodle|groodle|spoodle|kelpie|staffy)",
    "style": r"colou?rs?\b|gorgeous|beautiful(?:ly)?|stunning|aesthetic|\bstyl(?:e|ish|ing)|vibrant|rich (?:colou?r|tone)|\bhue|shade\b|look(?:s|ed)? (?:so |really |absolutely )?(?:amazing|great|good|beautiful|lovely|stunning|luxe|luxurious|expensive|fab)|decor|interior|bedroom looks|compliments?|\bpop\b|statement|matches|\bmoody\b|earthy",
    "softness": r"\bsoft(?:er|est|ness)?\b|silky|buttery|smooth|like butter|cloud|\bsilk\b|feels? (?:amazing|incredible|divine|heavenly|luxurious)",
    "luxury": r"luxur(?:y|ious)|hotel|five star|5 star|5-star|resort|expensive (?:feel|look)|high end|premium|decadent|indulgen",
    "quality": r"\bquality\b|well made|well-made|stitching|craftsmanship|sturdy|beautifully made",
    "durability": r"(?:still|months?|years?) (?:later|on)|after (?:many|lots of|countless|several|months|years|\d+) (?:washes|washing)|held up|holding up|lasted|last(?:s)? (?:well|forever)|(?:for|over) (?:\d+|two|three|four|five|many) years|no pilling|hasn'?t pilled|doesn'?t pill|not pilled|wear(?:s)? well|durable|durability",
    "sleep_better": r"(?:sleep(?:ing)?|slept) (?:so )?(?:better|well|soundly|deeply|through)|best sleep|better sleep|sleep quality|deeper sleep|wake (?:up )?(?:less|refreshed)|no longer wak|stopped waking|good night'?s sleep",
    "skin": r"\bskin\b|eczema|psoriasis|dermat|\brash(?:es)?\b|\bitch(?:y|ing|iness)?\b|irritat|\bacne\b|breakouts?|sensitive",
    "allergy": r"allerg|hay ?fever|asthma|dust mite|sneez|hypoallergenic|sinus",
    "hair": r"(?:my|her|his|curly|frizz(?:y)?) hair|frizz|bed ?head|hair (?:breakage|tangle)",
    "eco": r"sustainab|eco\b|eco-friendly|environment|planet|bamboo is|natural fib|biodegrad|organic|plastic|green credentials|ethical|non-?toxic|chemical",
    "value": r"\bvalue\b|worth (?:it|every|the)|price|cheap(?:er)?|afford|bargain|\bsale\b|discount|\bdeal\b(?! with)|money|for the cost|investment",
    "gift": r"\bgift(?:ed|s)?\b|present\b|birthday|christmas|xmas|mother'?s day|father'?s day|wedding|housewarming|bought (?:for|these for) (?:my|our) (?:mum|mom|dad|daughter|son|sister|brother|friend|parents|nan)",
    "vs_cotton": r"cotton|egyptian|thread ?count|percale",
    "vs_linen": r"\blinen\b",
    "vs_other_brand": r"sheridan|ettitude|bed threads|bedthreads|adairs|kmart|target|bamboo village|sleep republic|koala|eva\b|ecosa|cultiver|dusk store|myer|david jones|canningvale|other bamboo|other brands?|tried (?:many|lots of|so many|heaps of|other)|compared to (?:other|my old|previous)|previous (?:sheets|bamboo|brand)",
    "wash_care": r"\bwash(?:es|ed|ing)?\b|dryer|tumble|laundry|iron(?:ing)?|line dry|cold wash",
    "fit": r"deep pockets?|pocket depth|fits? (?:perfectly|well|snug|our|my|the)|fitted (?:well|perfectly)|elastic|stay(?:s)? (?:on|put|in place)|mattress (?:depth|height|is deep)|tall mattress|\bfit\b",
    "customer_service": r"customer service|customer care|support team|the team|responsive|replied|refund|exchange|replace(?:d|ment)|helpful|reached out|emailed|contacted",
    "delivery": r"deliver(?:y|ed)|shipping|shipped|arrived|postage|dispatch|courier|parcel|express|fast (?:delivery|shipping|postage)",
    "packaging": r"packag|\bbox\b|wrapped|presentation|unbox|bag it came",
    "repeat_buyer": r"(?:second|third|fourth|fifth|2nd|3rd|4th|5th|another|more) (?:set|sets|pair|purchase|order|colou?r|quilt cover)|bought (?:more|another|again)|ordered (?:more|another|again)|back for more|will be buying (?:more|again)|already ordered|buying (?:another|more)|repeat (?:customer|purchase|buyer)|every (?:bed|room)|whole house|collection",
    "recommend": r"recommend|tell(?:ing)? (?:all )?(?:my |everyone|friends)|telling everyone|10/10|10 out of 10|highly rate|must have|must-have|can'?t (?:fault|recommend)",
    "couple": r"\bhusband|\bwife\b|partner|boyfriend|girlfriend|hubby|fianc|\bwe both\b|both of us|my other half",
    "kids": r"\bkids?\b|children|child|son'?s|daughter'?s|toddler|baby|teen(?:ager)?s?|kid'?s room|bunk",
    "winter_warmth": r"winter|warm(?:th|er)? in (?:winter|the cold)|cosy|cozy|toasty|cold (?:nights?|weather|months)|all year|year round|all seasons",
    "sceptic_converted": r"sceptic|skeptic|hesita|unsure|wasn'?t sure|didn'?t believe|doubt|took a (?:chance|punt|gamble)|on the fence|was worried|wary|not convinced|didn'?t think|didn'?t expect|exceeded (?:my )?expectations|believe the hype|lives? up to the hype|worth the hype",
    "superlative": r"best (?:sheets|bedding|purchase|quilt|investment|thing)|ever (?:owned|had|slept|bought)|never (?:going|go) back|life ?chang|game ?changer|obsessed|in love|absolutely love|can'?t live without|holy grail|10/10",
  },
  "complaints": {
    "pilling": r"(?<!every )(?<!sleeping )\bpill(?:ing|ed|s|y)?\b(?! possible)|bobbl|fuzz",
    "fading_colour": r"\bfad(?:e|ed|es|ing)\b|discolou?r|colou?r (?:ran\b|bleed|bled|wash(?:ed)? out)|lost (?:its|their) colou?r|dye (?:came|ran|bled)",
    "staining": r"\bstain(?:s|ed|ing)?\b|marks? (?:from|on)|oil(?:y)? (?:marks|patches|stains)|sweat (?:marks|stains|patches)",
    "colour_mismatch": r"(?:different|not the same|darker|lighter|brighter|duller) (?:colou?r|shade|than (?:the )?(?:picture|photo|website|online|image))|colou?r (?:is|was) (?:off|different|not)|doesn'?t match|don'?t match|didn'?t match",
    "too_hot": r"too (?:hot|warm)|not (?:as )?cool(?:ing)?|didn'?t (?:keep me )?cool|still (?:hot|sweat)|sleep hot in them|hotter than",
    "shrinkage": r"shr[iu]nk|shrank|shrinkage|smaller after",
    "thin_tear": r"\bthin\b|see.?through|\btear(?:s|ing)?\b(?! (?:of joy|up))|\btore\b|\btorn\b|\brip(?:ped|s)?\b(?! ?off)|\b(?:a|small|tiny|little|big) holes?\b|snag|ladder|threadbare|worn through|seam (?:came|split|undone)",
    "wrinkles": r"wrinkl|crease|crinkl|crumpl",
    "fit_issue": r"too (?:small|big|short|tight|loose)|(?:doesn'?t|didn'?t|won'?t|does not) (?:fit|stay)|pops? off|slid(?:es?|ing)? off|elastic (?:broke|gone|went|failed)|not deep enough|too shallow",
    "delivery_issue": r"late|delay|never (?:arrived|received)|lost (?:in the post|parcel)|wrong (?:item|size|colou?r|order)|missing|took (?:ages|forever|weeks)",
    "static_lint": r"\bstatic\b|lint|cling",
    "smell": r"smell|odou?r|chemical",
  },
}

# Survey persona answers -> naming-sheet Persona vocab (ads/ad-naming.json).
SURVEY_PERSONA = {
    "I'm a hot sleeper": "HotSleeper", "I have pets that shed": "PetHair",
    "I love styling my space": "HomeInterior", "I have sensitive skin or allergies": "SensitiveSkin",
    "I'm focused on recovery": "FitnessRecovery",
}
# Text themes -> Persona vocab, used when the reviewer skipped the survey.
THEME_PERSONA = {"cooling": "HotSleeper", "pet": "PetHair", "style": "HomeInterior",
                 "skin": "SensitiveSkin", "allergy": "Allergies", "couple": "Couple",
                 "eco": "Eco", "hair": "Hair"}
# Themes -> naming-sheet Angle vocab a quote could carry.
THEME_ANGLE = {"vs_cotton": "ComparisonClaim", "vs_linen": "ComparisonClaim", "vs_other_brand": "ComparisonClaim",
               "value": "PriceLed", "sceptic_converted": "SocialProof", "superlative": "SocialProof",
               "recommend": "SocialProof", "repeat_buyer": "SocialProof", "cooling": "ProblemHighlight",
               "pet": "ProblemHighlight", "skin": "ProblemHighlight", "allergy": "ProblemHighlight",
               "sleep_better": "Aspiration", "luxury": "Aspiration", "style": "Aspiration",
               "eco": "Origin", "durability": "Trust", "customer_service": "Trust"}

STATES = {"New South Wales": "NSW", "Victoria": "VIC", "Queensland": "QLD", "Western Australia": "WA",
          "South Australia": "SA", "Tasmania": "TAS", "Australian Capital Territory": "ACT", "Northern Territory": "NT"}

def rx(p): return re.compile(p, re.I)
THEME_RX = {k: rx(v) for k, v in TAGS["themes"].items()}
COMPLAINT_RX = {k: rx(v) for k, v in TAGS["complaints"].items()}
COLOUR_RX = {k: rx(v) for k, v in COLOURS.items()}
NEG_GUARD = rx(r"\b(?:no|not|never|zero|without|hasn'?t|haven'?t|doesn'?t|don'?t|didn'?t|isn'?t|wasn'?t|won'?t|minimal|any)\b[^.!?]{0,35}$")

def norm(s): return s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"').strip()

def split_multi(v): return [x.strip() for x in v.split(",") if x.strip()] if v else []

def short_name(n):
    parts = n.strip().split()
    if not parts: return ""
    return parts[0].title() + (f" {parts[-1][0].upper()}." if len(parts) > 1 else "")

def product_of(handle):
    for pat, cat, fab in PRODUCT_RULES:
        if re.search(pat, handle or ""): return cat, fab
    return ("unknown", "")

def complaints_of(text, rating):
    found = []
    for k, r in COMPLAINT_RX.items():
        for m in r.finditer(text):
            # "no pilling", "hasn't faded" are praise, not complaints.
            if NEG_GUARD.search(text[max(0, m.start() - 45):m.start()]): continue
            found.append(k); break
    # Only trust soft complaint words when the rating backs them up.
    if rating >= 4: found = [c for c in found if c in ("pilling", "fading_colour", "staining", "shrinkage", "thin_tear", "fit_issue")]
    # Five-star "it just slides off" is pet hair, not the sheet.
    if rating == 5: found = [c for c in found if c != "fit_issue"]
    return found

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+|\n+")
def pull_quote(title, body, themes):
    """Best single sentence for an ad: themed, 25-160 chars, no complaint words."""
    sents = [s.strip() for s in SENT_SPLIT.split(body) if s.strip()]
    best, score = "", -1
    for s in sents:
        L = len(s)
        if L < 20 or L > 180: continue
        sc = sum(2 for t in themes if THEME_RX[t].search(s)) + (1 if 40 <= L <= 120 else 0)
        sc -= 3 * any(r.search(s) for r in COMPLAINT_RX.values())
        if sc > score: best, score = s, sc
    if not best and 15 <= len(title) <= 90 and not re.fullmatch(r"(?i)(great|good|love(?:ly)?|amazing|excellent)( \w+)?[.!]*", title.strip()):
        best = title.strip()
    return best

def theme_quotes(body, themes):
    """Best sentence per theme: mentions that theme, 20-180 chars, no complaint words."""
    sents = [x.strip() for x in SENT_SPLIT.split(body) if 20 <= len(x.strip()) <= 180]
    sents = [x for x in sents if not any(r.search(x) for r in COMPLAINT_RX.values())]
    out = {}
    for t in themes:
        hits = [x for x in sents if THEME_RX[t].search(x)]
        if hits: out[t] = min(hits, key=lambda x: abs(len(x) - 90))
    return out

def ad_score(rating, body, themes, complaints, quote):
    """0-10. High = 5 stars, specific, themed, a clean quotable line, no complaints."""
    if rating < 5 or complaints: return 0
    s = 2
    s += min(len(themes), 4)
    s += 2 if quote else 0
    s += 1 if 60 <= len(body) <= 600 else 0
    s += 1 if THEME_RX["superlative"].search(body) or THEME_RX["sceptic_converted"].search(body) else 0
    return min(s, 10)

def main(src):
    rows = list(csv.reader(open(src, encoding="utf-8-sig")))
    head, data = rows[0], rows[1:]
    idx = collections.defaultdict(list)
    for i, h in enumerate(head): idx[h].append(i)
    first = lambda r, h: next((r[i] for i in idx[h] if r[i]), "")
    out = []
    for r in data:
        title, body = norm(r[0]), norm(r[1])
        text = f"{title}. {body}"
        rating = int(r[2])
        cat, fab = product_of(r[9])
        themes = [k for k, rgx in THEME_RX.items() if rgx.search(text)]
        survey_personas = [SURVEY_PERSONA[x] for x in split_multi(first(r, "What describes you best?")) if x in SURVEY_PERSONA]
        favs = split_multi(first(r, "Favourite features?")) or split_multi(first(r, "Favourite feature"))
        # Survey answers count as theme evidence too.
        if "HotSleeper" in survey_personas and "cooling" not in themes and "Temperature regulation" in favs: themes.append("cooling")
        if "PetHair" in survey_personas and "pet" not in themes and "Pet hair friendly" in favs: themes.append("pet")
        complaints = complaints_of(text, rating)
        personas = list(dict.fromkeys(survey_personas + [THEME_PERSONA[t] for t in themes if t in THEME_PERSONA]))
        colours = list(dict.fromkeys(split_multi(first(r, "Colour(s) purchased")) + [c for c, rgx in COLOUR_RX.items() if rgx.search(text) or rgx.search(r[9].replace("-", " "))]))
        loc = r[14]
        lp = [p.strip() for p in loc.split(",")] if loc else []
        country = lp[-1] if lp else ""
        state = STATES.get(lp[-2], lp[-2]) if len(lp) >= 2 else ""
        quote = pull_quote(title, body, themes)
        sleep = first(r, "Has your sleep quality improved since using Ecoy?")
        rec = {
            "id": r[15] or f"row-{len(out)+1}",
            "date": r[3][:10],
            "rating": rating,
            "sentiment": "positive" if rating >= 4 else "neutral" if rating == 3 else "negative",
            "title": title,
            "body": body,
            "pull_quote": quote,
            "theme_quotes": theme_quotes(body, themes),
            "ad_score": ad_score(rating, body, themes, complaints, quote),
            "reviewer": short_name(r[6]),
            "city": lp[0] if lp else "",
            "state": state,
            "country": country,
            "product_handle": r[9],
            "product_category": cat,
            "fabric": fab,
            "is_bedding": cat in BEDDING,
            "colours": colours,
            "retired_colour": any(c in RETIRED for c in colours),
            "themes": themes,
            "complaints": complaints,
            "personas": personas,
            "angles": list(dict.fromkeys(THEME_ANGLE[t] for t in themes if t in THEME_ANGLE)),
            "survey": {k: v for k, v in {
                "age": first(r, "Age"),
                "describes_me": split_multi(first(r, "What describes you best?")),
                "sleep_improved": {"Yes": True, "No": False}.get(sleep),
                "previous_material": first(r, "Previous bedding material").strip(),
                "favourite_features": favs,
                "reason_for_purchase": split_multi(first(r, "Reason for purchase")),
                "sleep_position": split_multi(first(r, "Sleep position")),
                "previous_pillow": first(r, "Previous pillow"),
                "previous_quilt_filling": first(r, "Previous quilt/duvet filling"),
            }.items() if v not in ("", [], None)},
            "has_photos": bool(r[12]),
            "photo_urls": split_multi(r[12]),
            "source": r[4],
        }
        out.append(rec)
    out.sort(key=lambda x: x["date"], reverse=True)

    with open(HERE / "reviews.jsonl", "w") as f:
        for o in out: f.write(json.dumps(o, ensure_ascii=False) + "\n")
    flat_cols = ["id", "date", "rating", "sentiment", "ad_score", "product_category", "fabric", "product_handle",
                 "colours", "themes", "complaints", "personas", "angles", "pull_quote", "title", "body",
                 "reviewer", "city", "state", "country", "has_photos", "photo_urls"]
    with open(HERE / "reviews.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(flat_cols + ["survey_age", "survey_sleep_improved", "survey_previous_material", "survey_favourite_features"])
        for o in out:
            w.writerow([("|".join(o[c]) if isinstance(o[c], list) else o[c]) for c in flat_cols] + [
                o["survey"].get("age", ""), o["survey"].get("sleep_improved", ""),
                o["survey"].get("previous_material", ""), "|".join(o["survey"].get("favourite_features", []))])

    write_tags_and_insights(out)
    print(f"{len(out)} reviews -> {HERE}")

def write_tags_and_insights(out):
    C = collections.Counter
    n = len(out)
    theme_n = C(t for o in out for t in o["themes"])
    comp_n = C(t for o in out for t in o["complaints"])
    pers_n = C(p for o in out for p in o["personas"])
    json.dump({"$comment": "Tag dictionary for voc/reviews.jsonl. Patterns are case-insensitive regex over 'title. body'. Edit them in build_voc.py, not here.",
               "themes": {k: {"pattern": v, "count": theme_n[k]} for k, v in TAGS["themes"].items()},
               "complaints": {k: {"pattern": v, "count": comp_n[k]} for k, v in TAGS["complaints"].items()},
               "personaMap": {"survey": SURVEY_PERSONA, "fromTheme": THEME_PERSONA},
               "angleMap": THEME_ANGLE, "products": [{"pattern": p, "category": c, "fabric": f} for p, c, f in PRODUCT_RULES]},
              open(HERE / "tags.json", "w"), indent=1)

    ratings = [o["rating"] for o in out]
    bed = [o for o in out if o["is_bedding"]]
    sl = [o["survey"]["sleep_improved"] for o in out if "sleep_improved" in o["survey"]]
    prev = C(o["survey"]["previous_material"] for o in out if o["survey"].get("previous_material"))
    age = C(o["survey"]["age"] for o in out if o["survey"].get("age") and "," not in o["survey"]["age"])
    favs = C(f for o in out for f in o["survey"].get("favourite_features", []))
    fav_n = sum(1 for o in out if o["survey"].get("favourite_features"))
    pct = lambda a, b: f"{100*a/b:.0f}%" if b else "–"
    L = []
    L.append("# Voice of customer: what the reviews say\n")
    L.append(f"Generated by `build_voc.py` from the Judge.me export. {n:,} published reviews, {out[-1]['date']} to {out[0]['date']}. Numbers below are counts of reviews, not claims. Check VOC.md before putting any of them in an ad.\n")
    L.append("## Headline numbers\n")
    L.append("| Measure | Value | Base |\n|---|---|---|")
    L.append(f"| Average rating, all products | {statistics.mean(ratings):.2f} ★ | {n:,} reviews |")
    L.append(f"| Average rating, bedding only | {statistics.mean(o['rating'] for o in bed):.2f} ★ | {len(bed):,} reviews |")
    L.append(f"| 5-star share | {pct(sum(1 for x in ratings if x == 5), n)} | {n:,} |")
    L.append(f"| 4 or 5 stars | {pct(sum(1 for x in ratings if x >= 4), n)} | {n:,} |")
    L.append(f"| Said sleep improved (survey) | {pct(sum(sl), len(sl))} | {len(sl):,} who answered |")
    L.append(f"| Switched from cotton (survey) | {pct(prev['Cotton'], sum(prev.values()))} | {sum(prev.values()):,} who answered |")
    L.append(f"| Reviews with customer photos | {sum(o['has_photos'] for o in out):,} | {n:,} |\n")
    L.append("## Themes\n")
    L.append("| Theme | Reviews | Share | Avg ★ |\n|---|---|---|---|")
    for t, c in theme_n.most_common():
        L.append(f"| `{t}` | {c:,} | {pct(c, n)} | {statistics.mean(o['rating'] for o in out if t in o['themes']):.2f} |")
    L.append("\n## Complaints (what to avoid claiming, and what to pre-empt)\n")
    L.append("| Complaint | Reviews | Share of 1–3★ reviews |\n|---|---|---|")
    low = sum(1 for o in out if o["rating"] <= 3)
    for t, c in comp_n.most_common():
        L.append(f"| `{t}` | {c:,} | {pct(sum(1 for o in out if t in o['complaints'] and o['rating'] <= 3), low)} |")
    L.append("\n## Who reviews (survey)\n")
    L.append("**Persona tags** (survey answer, or inferred from the text when skipped): " + ", ".join(f"{p} {c:,}" for p, c in pers_n.most_common()) + "\n")
    L.append("**Age:** " + ", ".join(f"{a} {pct(c, sum(age.values()))}" for a, c in sorted(age.items())) + f" (base {sum(age.values()):,})\n")
    L.append("**Previous bedding:** " + ", ".join(f"{a} {pct(c, sum(prev.values()))}" for a, c in prev.most_common()) + "\n")
    L.append(f"**Favourite features** (tick all that apply, base {fav_n:,}): " + ", ".join(f"{a} {pct(c, fav_n)}" for a, c in favs.most_common()) + "\n")
    L.append("## Best quotes by theme\n")
    L.append("Top 8 per theme by `ad_score`, then most recent. Bedding only, live colours only, each review used once across all themes. Attribute as written (first name + initial). Read the full review before using one. For more, query `reviews.jsonl` (see VOC.md).\n")
    used = set()
    for t in ["cooling", "pet", "style", "softness", "sleep_better", "luxury", "durability", "skin", "allergy",
              "vs_cotton", "vs_linen", "vs_other_brand", "sceptic_converted", "repeat_buyer", "value", "gift",
              "couple", "eco", "winter_warmth", "superlative"]:
        pool = [o for o in out if t in o["themes"] and o["is_bedding"] and not o["retired_colour"]
                and o["ad_score"] >= 6 and o["id"] not in used and THEME_RX[t].search(o["pull_quote"])]
        pool.sort(key=lambda o: (o["ad_score"], o["date"]), reverse=True)
        if not pool: continue
        L.append(f"### `{t}` ({theme_n[t]:,} reviews)\n")
        for o in pool[:8]:
            used.add(o["id"])
            L.append(f"- \"{o['pull_quote']}\" — {o['reviewer']}, {o['state'] or o['country']} · {o['product_category'].replace('_', ' ')} · {o['date'][:7]} · `{o['id']}`")
        L.append("")
    (HERE / "INSIGHTS.md").write_text("\n".join(L))

if __name__ == "__main__":
    if len(sys.argv) != 2: sys.exit(__doc__)
    main(sys.argv[1])
