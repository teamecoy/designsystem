#!/usr/bin/env python3
"""Read an Ecoy Meta ad name into structured fields.

Handles the three naming styles in real use:
  v2       2026-September-Static-EmilieCS-Untested-Problemaware-HomeInterior-USP-...
  legacy   2026-Feb-Video-AMBI-AlexCS-Untested-Newrelease-Sheets-MixedColours-Greg-V1-JOB-1843
  creator  2026_July_@emcombsfitness_Productaware_Lifestyle_CP-UGC_Bamboo_Sheets_CherryBlossom_9x16

Anything else comes back as "unparsed", with any recognisable words kept as hints.
Words are matched against the vocabulary in ad-naming.json rather than by position,
because real names drop fields and add spaces. Unknown words are kept, never dropped.

    python3 ads/parse_ad_name.py "2026-September-Static-..."     # one or more names
    python3 ads/parse_ad_name.py --report names.txt              # one name per line
"""
import json, pathlib, re, sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent
N = json.loads((ROOT / "ad-naming.json").read_text())
ORDER = [f for f in N["filename"]["order"] if f not in ("Year", "Month")]
MONTHS = N["vocab"]["Month"]
CREATOR_MOMENTS = {"CollabPost", "PartneredAd", "Seeding"}


def norm(s):
    return re.sub(r"[\s&]", "", s).lower()


# normalised token -> list of (field, canonical value, needs_space)
INDEX = {}
for field, values in N["vocab"].items():
    for v in values:
        INDEX.setdefault(norm(v), []).append((field, v, " " in v))


def clean(name):
    name = re.split(r"trybe=", name)[0]
    name = re.sub(r"\s*[–-]\s*Copy(\s*\d+)?\s*$", "", name)
    return name.strip(" _-")


def month_of(tok):
    t = tok.lower().rstrip(".")
    if re.fullmatch(r"0?[1-9]|1[0-2]", t):
        return MONTHS[int(t) - 1]
    for m in MONTHS:
        if t == m.lower() or (len(t) >= 3 and m.lower().startswith(t)):
            return m
    return None


def tokens(name, creator):
    name = name.replace("CP-UGC", "CPUGC")
    parts = name.split("_") if (creator and "_" in name) else name.split("-")
    parts = [p.strip() for p in parts if p.strip()]
    out, i = [], 0
    while i < len(parts):
        if parts[i].upper() == "JOB" and i + 1 < len(parts) and parts[i + 1].isdigit():
            out.append(f"JOB-{parts[i + 1]}"); i += 2
        else:
            out.append(parts[i]); i += 1
    return out


def match(tok, allowed):
    """Fields in `allowed` (in order) whose vocab contains tok."""
    hits = [(f, v) for f, v, needs_space in INDEX.get(norm(tok), [])
            if not needs_space or " " in tok]
    return [(f, v) for f, v in sorted(hits, key=lambda h: allowed.index(h[0]) if h[0] in allowed else 99)
            if f in allowed]


def hints(name):
    """Recognisable words in a free-form name, e.g. Shopify collection ads."""
    parts = [p for p in re.split(r"[\s_\-–—]+", name) if p]
    found, i = {}, 0
    while i < len(parts):
        pair = parts[i] + parts[i + 1] if i + 1 < len(parts) else None
        if pair and norm(pair) in INDEX:
            field, value, _ = INDEX[norm(pair)][0]; i += 2
        elif norm(parts[i]) in INDEX:
            field, value, _ = INDEX[norm(parts[i])][0]; i += 1
        else:
            i += 1; continue
        found.setdefault(field, value)
    return found


def parse(raw):
    name = clean(raw)
    # Creator-program ads carry an @handle; CP-UGC (creator partnership) is the
    # second signal, for the odd one named without the handle.
    creator = "@" in name or "CP-UGC" in name.upper()
    out = {"raw": raw, "convention": None, "fields": {}, "creator": None,
           "extra": [], "unknown": [], "missing": []}
    f = out["fields"]
    pos = 0  # index into ORDER: fields before it are behind us
    for tok in tokens(name, creator):
        if "Year" not in f and re.fullmatch(r"20\d\d", tok):
            f["Year"] = tok; continue
        if "Month" not in f and month_of(tok):
            f["Month"] = month_of(tok); continue
        if tok.startswith("@"):
            out["creator"] = tok; continue
        if tok.upper() == "CPUGC":
            f.setdefault("Vehicle", "UGC"); continue
        if re.fullmatch(r"V\d+", tok, re.I):
            f["Variation"] = tok.upper(); continue
        if re.fullmatch(r"JOB-\d+", tok, re.I):
            f["JobID"] = tok.upper(); continue
        if re.fullmatch(r"\d+x\d+", tok):
            f["Dimensions"] = tok; continue
        ahead = match(tok, ORDER[pos:])
        if ahead:
            field, value = ahead[0]
            if field not in f:
                f[field] = value
                pos = ORDER.index(field) + 1
                continue
        if ("Designer" not in f and norm(tok + "Designer") in INDEX):
            f["Designer"] = INDEX[norm(tok + "Designer")][0][1]; continue
        anywhere = match(tok, ORDER)
        if anywhere:
            out["extra"].append({anywhere[0][0]: anywhere[0][1]})
        else:
            out["unknown"].append(tok)

    dated = "Year" in f and "Month" in f
    if "@" in name:
        out["convention"] = "creator"
    elif dated and (int(f["Year"]), MONTHS.index(f["Month"])) >= (2026, 4) and \
            {"AwarenessStage", "Persona", "Vehicle"} & f.keys():
        out["convention"] = "v2"
        # Dimensions is left blank at ad level when one ad serves several ratios.
        out["missing"] = [x for x in N["filename"]["required"] if x not in f and x != "Dimensions"]
    elif dated:
        out["convention"] = "legacy"
    else:
        out["convention"] = "unparsed"
        out["hints"] = hints(name)

    moment = f.get("CampaignMoment")
    out["momentType"] = N["momentType"].get(moment, "unknown") if moment else None
    out["adType"] = ("creator" if creator or moment in CREATOR_MOMENTS
                     or f.get("Vehicle") == "Collab" else "designed")
    colour = f.get("Colour")
    out["photoColour"] = N["colourToPhoto"].get(colour, {}).get("photo") if colour else None
    return out


def report(names):
    rows = [parse(n) for n in names if n.strip()]
    conv = Counter(r["convention"] for r in rows)
    unknown = Counter(t for r in rows for t in r["unknown"])
    missing = Counter(m for r in rows for m in r["missing"])
    print(f"{len(rows)} names: " + ", ".join(f"{k} {v}" for k, v in conv.most_common()))
    print("moment types: " + ", ".join(f"{k} {v}" for k, v in
                                        Counter(str(r["momentType"]) for r in rows).most_common()))
    print("ad types: " + ", ".join(f"{k} {v}" for k, v in Counter(r["adType"] for r in rows).most_common()))
    if missing:
        print("v2 names missing a required field: " + ", ".join(f"{k} {v}" for k, v in missing.most_common()))
    if unknown:
        print("unrecognised words: " + ", ".join(f"{k} ({v})" for k, v in unknown.most_common(25)))


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); return 1
    if args[0] == "--report":
        report(pathlib.Path(args[1]).read_text().splitlines()); return 0
    for a in args:
        print(json.dumps(parse(a), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
