#!/usr/bin/env python3
"""Walk the mounted Photography library and build a structured index.

Phase 1: no image is opened. Every field is parsed from the filename using the
grammar in naming.json, so this costs nothing but a directory walk. The result
lets any tool answer "give me every High45 NoTalent Real shot of the Bamboo
Sheet Set in Dusk" without touching Drive.

    python3 assets/build_library_index.py            # full walk
    python3 assets/build_library_index.py --limit 50 # quick sample

Writes assets/library-index.json and prints progress to stderr.
"""
import json, os, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent
LIB = pathlib.Path(os.path.expanduser(
    "~/Library/CloudStorage/GoogleDrive-sam@ecoy.com.au/Shared drives/Ecoy shared drive/Photography"))
N = json.loads((ROOT / "naming.json").read_text())

PRODUCTS = {p["token"] for p in N["products"]}
PATTERNS = {p["token"] for p in N["patterns"]}
COLOURS = ({c["token"] for c in N["colours"]["solid"]}
           | {c["token"] for c in N["colours"]["stripe"]}
           | {c["token"] for c in N["colours"].get("polka", [])})
ANGLES, PEOPLE, SOURCES = set(N["angles"]), set(N["people"]), set(N["sources"])
ORIENTATIONS = set(N.get("orientations", [])) or {"Vertical", "Horizontal"}
# Orientation was added to the spreadsheet 2026-09-23 for new shoots only;
# every file indexed before that has no orientation segment, which is
# expected, not invalid (see naming.json knownGaps).
IMAGE_EXT = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff", ".heic"}
VIDEO_EXT = {".mov", ".mp4", ".m4v"}


def parse(stem):
    """Parse a filename stem into fields. Unknown tokens are kept, not dropped."""
    out = {"product": None, "pattern": None, "colour": None, "angle": None,
           "people": None, "source": None, "orientation": None, "seq": None,
           "unknown": [], "valid": False}
    parts = stem.split("-")
    if len(parts) < 4:
        out["unknown"] = parts
        return out

    if re.fullmatch(r"\d{1,3}", parts[-1]):
        out["seq"] = parts[-1].zfill(2)
        parts = parts[:-1]

    for p in list(parts):
        if p in SOURCES and not out["source"]:
            out["source"] = p; parts.remove(p)
        elif p in PEOPLE and not out["people"]:
            out["people"] = p; parts.remove(p)
        elif p in ANGLES and not out["angle"]:
            out["angle"] = p; parts.remove(p)
        elif p in ORIENTATIONS and not out["orientation"]:
            out["orientation"] = p; parts.remove(p)
        elif p in PATTERNS and not out["pattern"]:
            out["pattern"] = p; parts.remove(p)
        elif p in PRODUCTS and not out["product"]:
            out["product"] = p; parts.remove(p)

    for p in list(parts):
        if p in COLOURS and not out["colour"]:
            out["colour"] = p; parts.remove(p)
        elif "x" in p:
            halves = [h for h in re.split(r"(?<=[a-z])x(?=[A-Z])", p) if h]
            if len(halves) == 2 and all(h in COLOURS for h in halves) and not out["colour"]:
                out["colour"] = p; out["colourPair"] = halves; parts.remove(p)

    out["unknown"] = parts
    out["valid"] = bool(out["product"] and out["angle"] and out["people"]
                        and out["source"] and out["seq"] and not parts)
    return out


def reparse():
    """Re-derive fields for an existing index after the vocabulary changes."""
    path = ROOT / "library-index.json"
    doc = json.loads(path.read_text())
    for r in doc["files"]:
        fn = pathlib.Path(r["path"]).name
        for k in ("product", "pattern", "colour", "angle", "people",
                  "source", "orientation", "seq", "colourPair", "unknown", "valid"):
            r.pop(k, None)
        parsed = parse(pathlib.Path(fn).stem)
        for k, v in parsed.items():
            if k == "valid":
                if not v:
                    r["valid"] = False
            elif v:
                r[k] = v
    imgs = [r for r in doc["files"] if r.get("kind") != "video"]
    doc["counts"] = {"total": len(doc["files"]), "images": len(imgs),
                     "videos": len(doc["files"]) - len(imgs),
                     "validNames": sum(1 for r in doc["files"] if r.get("valid") is not False)}
    path.write_text(json.dumps(doc, separators=(",", ":"), ensure_ascii=False) + "\n")
    print(f"reparsed {doc['counts']['total']} rows; "
          f"{doc['counts']['validNames']} names now parse cleanly", file=sys.stderr)


def main():
    if "--reparse" in sys.argv:
        return reparse()
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    if not LIB.exists():
        sys.exit(f"Library not mounted at {LIB}")

    rows, n = [], 0
    for dirpath, dirnames, filenames in os.walk(LIB):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in filenames:
            ext = pathlib.Path(fn).suffix.lower()
            if ext not in IMAGE_EXT and ext not in VIDEO_EXT:
                continue
            full = pathlib.Path(dirpath) / fn
            rel = full.relative_to(LIB)
            row = {"path": str(rel), "filename": fn,
                   "kind": "video" if ext in VIDEO_EXT else "image",
                   "folders": list(rel.parts[:-1])}
            row.update(parse(pathlib.Path(fn).stem))
            try:
                row["bytes"] = full.stat().st_size
            except OSError:
                row["bytes"] = None
            rows.append(row)
            n += 1
            if n % 250 == 0:
                print(f"  {n} files…", file=sys.stderr, flush=True)
            if limit and n >= limit:
                break
        if limit and n >= limit:
            break

    images = [r for r in rows if r["kind"] == "image"]
    doc = {
        "$comment": "GENERATED by assets/build_library_index.py from the mounted Drive library. Filename-parsed only; no image was opened.",
        "library": N["library"],
        "counts": {
            "total": len(rows),
            "images": len(images),
            "videos": len(rows) - len(images),
            "validNames": sum(1 for r in rows if r["valid"]),
        },
        "files": sorted(rows, key=lambda r: r["path"]),
    }
    # compact: omit null/empty fields so the file stays small enough to live in git
    slim = []
    for r in doc["files"]:
        row = {"path": r["path"]}
        for k in ("product", "pattern", "colour", "angle", "people", "source", "orientation", "seq"):
            if r.get(k):
                row[k] = r[k]
        if r.get("colourPair"):
            row["colourPair"] = r["colourPair"]
        if r["kind"] != "image":
            row["kind"] = r["kind"]
        if not r["valid"]:
            row["valid"] = False
        if r.get("unknown"):
            row["unknown"] = r["unknown"]
        if r.get("bytes"):
            row["bytes"] = r["bytes"]
        slim.append(row)
    doc["files"] = slim
    (ROOT / "library-index.json").write_text(json.dumps(doc, separators=(",", ":"), ensure_ascii=False) + "\n")
    c = doc["counts"]
    print(f"\nindexed {c['total']} files ({c['images']} images, {c['videos']} videos); "
          f"{c['validNames']} names parse cleanly", file=sys.stderr)


if __name__ == "__main__":
    main()
