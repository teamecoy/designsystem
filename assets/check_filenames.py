#!/usr/bin/env python3
"""Check Ecoy photography filenames against the naming convention.

    python3 assets/check_filenames.py "/path/to/folder"     # check a folder
    python3 assets/check_filenames.py BambooSheetSet-Solid-Dusk-High45-NoTalent-Real-01.jpg

Prints OK for good names and, for bad ones, says exactly which part is wrong.
Vocabulary comes from naming.json, which is generated from the VA's spreadsheet.
"""
import json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent
N = json.loads((ROOT / "naming.json").read_text())

PRODUCTS = {p["token"] for p in N["products"]}
PATTERNS = {p["token"] for p in N["patterns"]}
COLOURS = {c["token"] for c in N["colours"]["solid"]} | {c["token"] for c in N["colours"]["stripe"]}
ANGLES, PEOPLE, SOURCES = set(N["angles"]), set(N["people"]), set(N["sources"])
EXTS = set(N["extensions"])
IMAGE_EXTS = EXTS | {".jpeg", ".webp", ".tif", ".tiff", ".heic"}


def check(name):
    """Return a list of problems. Empty list means the name is valid."""
    p = pathlib.Path(name)
    stem, ext = p.stem, p.suffix.lower()
    bad = []

    if ext not in EXTS:
        shown = ext or "(none)"
        allowed = ", ".join(sorted(EXTS))
        bad.append("extension '%s' should be one of %s" % (shown, allowed))

    parts = stem.split("-")
    if len(parts) < 5:
        return bad + [f"only {len(parts)} parts; expected Product-[Pattern]-[Colour]-Angle-People-Source-NN"]

    # Anchor from the right: seq, source, people, angle are always the last four.
    seq, source, people, angle = parts[-1], parts[-2], parts[-3], parts[-4]
    head = parts[:-4]

    if not re.fullmatch(r"\d{2}", seq):
        bad.append(f"sequence '{seq}' should be two digits, e.g. 01 (not {seq})")
    if source not in SOURCES:
        bad.append("source '%s' should be %s" % (source, " or ".join(sorted(SOURCES))))
    if people not in PEOPLE:
        extra = "  (note: use NoTalent, not Solo)" if people.lower() == "solo" else ""
        bad.append("people '%s' should be %s%s" % (people, " or ".join(sorted(PEOPLE)), extra))
    if angle not in ANGLES:
        bad.append("angle '%s' should be one of %s" % (angle, ", ".join(sorted(ANGLES))))

    if not head:
        return bad + ["missing product"]
    if head[0] not in PRODUCTS:
        bad.append(f"product '{head[0]}' is not a known product token")

    rest = head[1:]
    if rest and rest[0] in PATTERNS:
        rest = rest[1:]
    for token in rest:
        if token in COLOURS:
            continue
        if "x" in token:  # combo colour, e.g. BurntOrangexWhite
            halves = [h for h in re.split(r"(?<=[a-z])x(?=[A-Z])", token) if h]
            if len(halves) == 2 and all(h in COLOURS for h in halves):
                continue
            bad.append(f"combo colour '{token}' should join two known colours, e.g. BurntOrangexWhite")
        else:
            bad.append(f"colour '{token}' is not a known colour token")
    return bad


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    target = pathlib.Path(sys.argv[1])
    names = ([f for f in sorted(target.iterdir()) if f.suffix.lower() in IMAGE_EXTS]
             if target.is_dir() else [target])
    if not names:
        print("No image files found.")
        return 0

    good = 0
    for f in names:
        problems = check(f.name)
        if problems:
            print(f"\n✗ {f.name}")
            for p in problems:
                print(f"    {p}")
        else:
            good += 1
    print(f"\n{good} of {len(names)} filenames OK.")
    return 0 if good == len(names) else 1


if __name__ == "__main__":
    sys.exit(main())
