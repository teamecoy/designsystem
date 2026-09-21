#!/usr/bin/env python3
"""Select a production-grade photography set from the library index.

The curated shortlist proved the pipeline but is too thin to build an email
from: a single EDM consumes ~17 images. This selects systematically instead,
so every live colour on every core product has a frame, plus enough depth in
detail, cutout, flat-lay and talent shots to compose with.

Retired colourways and unparseable filenames are excluded, as in the shortlist.
High45 is preferred, then Low45, Side, Overhead.

    python3 assets/build_production_set.py [--max-edge 1200] [--quality 80]
"""
import json, os, pathlib, re, shutil, sys
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / "library"
WEB = pathlib.Path(os.path.expanduser(
    "~/Library/CloudStorage/GoogleDrive-sam@ecoy.com.au/Shared drives/Ecoy shared drive/Photography - Web"))
SHORTLIST = pathlib.Path(os.path.expanduser(
    "~/Library/CloudStorage/GoogleDrive-sam@ecoy.com.au/Shared drives/Ecoy shared drive"
    "/Photography - Web/Claude Photos"))
CORE = ["BambooSheetSet", "BambooQuiltCover", "FlannelSheetSet", "FlannelQuiltCover", "CordQuiltCover"]
PREF = ["High45", "Low45", "Side", "Overhead"]
CAPS = {"fabric-detail": 60, "flat-lay": 30, "talent": 60}


# Emilie's folder names and the generated slot names mean the same things;
# collapse them so the artifact sees one slot per job, not two.
SLOT_ALIASES = {"cutouts-deepetch": "cutout", "fabric-detail-closeup": "fabric-detail",
                "flat-lay-overhead": "flat-lay", "solid-colour-range": "product-colour",
                "stripe-colour-range": "stripe", "wide-lifestyle": "lifestyle"}


def slug(n):
    s = re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", n.lower())).strip("-")
    return SLOT_ALIASES.get(s, s)


def rank(r):
    return (PREF.index(r["angle"]) if r.get("angle") in PREF else 9, r.get("seq") or "99")


def main():
    max_edge = int(sys.argv[sys.argv.index("--max-edge") + 1]) if "--max-edge" in sys.argv else 1200
    quality = int(sys.argv[sys.argv.index("--quality") + 1]) if "--quality" in sys.argv else 80
    idx = json.loads((ROOT / "library-index.json").read_text())
    st = json.loads((ROOT / "colour-status.json").read_text())
    nm = json.loads((ROOT / "naming.json").read_text())
    live, stripe = set(st["live"]), {c["token"] for c in nm["colours"]["stripe"]}
    retired = set(st["retired"])

    img = [r for r in idx["files"] if r.get("kind") != "video"
           and r.get("valid") is not False and r.get("source") == "Real"
           and r.get("colour") not in retired]

    picked, seen = [], set()
    curated = set()

    def take(r, slot):
        if r["path"] in seen:
            return
        seen.add(r["path"])
        picked.append((r, slot))

    # Emilie's hand-picked shortlist comes first and keeps its editorial slot.
    # A human eye is the only thing that judges whether a frame is actually good,
    # so these are seeded before any rule-based selection and flagged as curated.
    # A curated pick is trusted whatever its source: Emilie chose it deliberately,
    # AI cutouts included. The Real-only rule below applies to machine selection.
    by_stem = {pathlib.Path(r["path"]).stem: r for r in idx["files"]
               if r.get("kind") != "video" and r.get("valid") is not False
               and r.get("colour") not in retired}
    if SHORTLIST.exists():
        for f in sorted(SHORTLIST.rglob("*.webp")):
            r = by_stem.get(f.stem)
            if r is None:
                continue
            curated.add(r["path"])
            take(r, slug(f.relative_to(SHORTLIST).parts[0]))

    # one frame per core product x live colour, best angle, no talent
    for p in CORE:
        for c in sorted(live):
            cand = [r for r in img if r.get("product") == p and r.get("colour") == c
                    and r.get("people") == "NoTalent" and r.get("angle") in PREF]
            if cand:
                take(min(cand, key=rank), "product-colour")

    # every stripe colourway on every product that has one
    for c in sorted(stripe):
        for p in sorted({r.get("product") for r in img if r.get("colour") == c}):
            cand = [r for r in img if r.get("product") == p and r.get("colour") == c
                    and r.get("angle") in PREF]
            if cand:
                take(min(cand, key=rank), "stripe")

    # Depth, spread across distinct SHOTS. Grouping only by product let one
    # setup swallow a third of the budget: 21 consecutive frames of the same
    # Dune overhead are a contact sheet, not a library. Bucket by the full
    # combination and take at most PER_SHOT frames from any one of them.
    PER_SHOT = 2

    def spread(pool, cap, slot):
        buckets = {}
        for r in sorted(pool, key=lambda r: (str(r.get("product")), str(r.get("colour")),
                                             str(r.get("angle")), r.get("seq") or "99")):
            key = (r.get("product"), r.get("colour"), r.get("angle"), r.get("people"))
            buckets.setdefault(key, []).append(r)
        for k in buckets:
            buckets[k] = buckets[k][:PER_SHOT]
        order = sorted(buckets, key=lambda k: tuple(str(x) for x in k))
        n = lambda: sum(1 for _, s in picked if s == slot)
        depth = 0
        while n() < cap and depth < PER_SHOT:
            for k in order:
                if depth < len(buckets[k]) and n() < cap:
                    take(buckets[k][depth], slot)
            depth += 1

    spread([r for r in img if r.get("angle") == "CloseUp"], CAPS["fabric-detail"], "fabric-detail")
    spread([r for r in img if r.get("angle") == "Deepetch"], 999, "cutout")
    spread([r for r in img if r.get("angle") == "Overhead"], CAPS["flat-lay"], "flat-lay")
    # Talent draws from any angle, Freestyle included: a person in a styled bed is
    # what ad creative wants, and almost all talent shots are filed as Freestyle.
    spread([r for r in img if r.get("people") == "Talent"
            and r.get("angle") not in ("Deepetch", "CloseUp")],
           CAPS["talent"], "talent")

    if OUT.exists():
        shutil.rmtree(OUT)
    kept, missing = [], 0
    for r, slot in picked:
        src = WEB / pathlib.Path(r["path"]).with_suffix(".webp")
        if not src.exists():
            missing += 1; continue
        dst = OUT / slug(slot) / pathlib.Path(r["path"]).with_suffix(".webp").name
        dst.parent.mkdir(parents=True, exist_ok=True)
        try:
            with Image.open(src) as im:
                im.thumbnail((max_edge, max_edge), Image.LANCZOS)
                im.save(dst, "WEBP", quality=quality, method=6)
                w, h = im.size
        except Exception:
            missing += 1; continue
        e = {"file": f"library/{slug(slot)}/{dst.name}", "slot": slot, "master": r["path"],
             "width": w, "height": h, "bytes": dst.stat().st_size}
        if r["path"] in curated:
            e["curated"] = True
        for k in ("product", "pattern", "colour", "angle", "people", "source"):
            if r.get(k):
                e[k] = r[k]
        kept.append(e)

    total = sum(e["bytes"] for e in kept)
    doc = {"$comment": ("GENERATED by assets/build_production_set.py from library-index.json. "
                        "Retired colourways and unparseable filenames are excluded. "
                        "These are the only photographs in this repository."),
           "maxEdge": max_edge, "quality": quality,
           "counts": {"kept": len(kept), "curated": sum(1 for e in kept if e.get("curated")),
                      "unreadable": missing, "megabytes": round(total / 1e6, 2)},
           "slots": {s: sum(1 for e in kept if e["slot"] == s) for s in sorted({e["slot"] for e in kept})},
           "files": kept}
    (ROOT / "library-shortlist.json").write_text(json.dumps(doc, indent=1) + "\n")
    print(f"kept {len(kept)} images ({doc['counts']['curated']} hand-picked), "
          f"{total/1e6:.1f} MB at {max_edge}px ({missing} unreadable)")
    for s, n in doc["slots"].items():
        print(f"   {s:18s} {n}")


if __name__ == "__main__":
    main()
