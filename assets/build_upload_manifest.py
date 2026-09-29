#!/usr/bin/env python3
"""Add newly shot photography to shopify-upload-manifest.json.

The manifest is the uploader notebook's to-do list. Entries already in it are
kept exactly as they are (most are on the CDN already, and their web paths were
hand-repaired); this only appends library files that are eligible and not yet
listed. Run after assets/build_library_index.py:

    python3 assets/build_upload_manifest.py            # update the repo copy
    python3 assets/build_upload_manifest.py --drive    # ...and the Drive copy the notebook reads

A file is eligible when its name parses cleanly, it's an image the web mirror
covers, it sits outside the excluded folders, its colour isn't retired, its
name is unique in the library, and it isn't on HOLD below.
"""
import json, pathlib, shutil, sys, time
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parent
MANIFEST = ROOT / "shopify-upload-manifest.json"
DRIVE = pathlib.Path.home() / ("Library/CloudStorage/GoogleDrive-sam@ecoy.com.au/"
                               "Shared drives/Ecoy shared drive/Photography - Web")
N = json.loads((ROOT / "naming.json").read_text())
RETIRED = set(json.loads((ROOT / "colour-status.json").read_text())["retired"])
SOURCE_EXT = set(N["library"]["web"]["sourceExtensions"])
EXCLUDED = N["library"]["web"]["excludedFolders"]

# Held back until their naming is settled, so a wrong name never reaches the
# CDN (a CDN file can't be renamed, only replaced). Clear an entry to release it.
HOLD = {
    "pattern:Polka": "2026-09-29: colour names disagree with the vocabulary "
                     "(BloomingPinkEggplantPolka etc.) and Malt Caramel is named MaltCaramelStripe.",
}


def held(row):
    return next((why for key, why in HOLD.items()
                 if row.get(key.split(":")[0]) == key.split(":")[1]), None)


def main():
    doc = json.loads(MANIFEST.read_text())
    listed = {f["name"].rsplit(".", 1)[0] for f in doc["files"]}
    rows = json.loads((ROOT / "library-index.json").read_text())["files"]
    stems = Counter(pathlib.Path(r["path"]).stem for r in rows)

    added, skipped = [], Counter()
    for r in rows:
        path = pathlib.Path(r["path"])
        stem, ext = path.stem, path.suffix.lower()
        if stem in listed:
            continue
        why = (("not an image the mirror covers" if r.get("kind") == "video" or ext not in SOURCE_EXT else None)
               or ("excluded folder" if any(x in r["path"] for x in EXCLUDED) else None)
               or ("name doesn't parse" if r.get("valid") is False else None)
               or ("retired colour" if r.get("colour") in RETIRED
                   or RETIRED & set(r.get("colourPair") or []) else None)
               or ("name not unique" if stems[stem] > 1 else None)
               or (f"on hold: {held(r)}" if held(r) else None))
        if why:
            skipped[why] += 1
            continue
        entry = {"web": str(path.with_suffix(".webp")), "name": stem + ".webp", "master": r["path"]}
        entry.update({k: r[k] for k in ("product", "pattern", "colour", "angle", "orientation",
                                        "people", "source") if r.get(k)})
        added.append(entry)
        listed.add(stem)

    doc["files"].extend(added)
    doc["count"] = len(doc["files"])
    doc["updated"] = time.strftime("%Y-%m-%d")
    MANIFEST.write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")

    print(f"added {len(added)}; manifest now {doc['count']} files")
    for k, v in Counter(f"{a['product']} / {a.get('colour', '-')}" for a in added).most_common():
        print(f"   {v:4}  {k}")
    print("not added (already-listed files not counted):")
    for k, v in skipped.most_common():
        print(f"   {v:5}  {k}")

    if "--drive" in sys.argv:
        target = DRIVE / MANIFEST.name
        if target.exists():
            shutil.copy2(target, target.with_name(f"shopify-upload-manifest.{time.strftime('%Y%m%d-%H%M')}.bak.json"))
        shutil.copy2(MANIFEST, target)
        print(f"copied to Drive: {target}")


if __name__ == "__main__":
    main()
