#!/usr/bin/env python3
"""Map a master photograph to its web-optimised copy.

The web mirror is a parallel tree: same relative path, same filename stem, only
the root folder and extension change. A missing .webp means "not generated yet",
so this falls back to the master rather than failing.

    python3 assets/resolve_web.py "Bamboo Sheet Set/Solid/Dusk/No Talent/BambooSheetSet-Solid-Dusk-High45-NoTalent-Real-01.jpg"
    python3 assets/resolve_web.py --coverage        # how much of the mirror exists so far
"""
import json, os, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent
DRIVE = pathlib.Path(os.path.expanduser(
    "~/Library/CloudStorage/GoogleDrive-sam@ecoy.com.au/Shared drives/Ecoy shared drive"))
MASTERS, WEB = DRIVE / "Photography", DRIVE / "Photography - Web"
WEB_SOURCE_EXT = {".jpg", ".jpeg", ".png", ".tif", ".tiff"}
EXCLUDED = ("NEW IMAGERY", "Archive", "Founder BTS & OLD Content")


def resolve(rel):
    """Return (path_to_use, which) for a library-relative master path.

    which is "web" when the optimised copy exists, "master" when it does not or
    could never exist. Paths are returned as-is, spaces and all; quote them.
    """
    rel = pathlib.Path(str(rel).lstrip("/"))
    master = MASTERS / rel
    if rel.suffix.lower() not in WEB_SOURCE_EXT:
        return master, "master"                      # e.g. .heic and video have no web copy
    if any(str(rel).startswith(e) for e in EXCLUDED):
        return master, "master"                      # deliberately excluded from the mirror
    web = WEB / rel.with_suffix(".webp")
    return (web, "web") if web.exists() else (master, "master")


def coverage():
    idx = json.loads((ROOT / "library-index.json").read_text())
    eligible = [r for r in idx["files"]
                if pathlib.Path(r["path"]).suffix.lower() in WEB_SOURCE_EXT
                and not any(r["path"].startswith(e) for e in EXCLUDED)]
    have = sum(1 for r in eligible if resolve(r["path"])[1] == "web")
    skipped = len(idx["files"]) - len(eligible)
    print(f"eligible for a web copy : {len(eligible)}")
    print(f"web copy exists now     : {have}  ({have / max(len(eligible), 1) * 100:.1f}%)")
    print(f"never eligible          : {skipped}  (video, .heic, or an excluded folder)")


if __name__ == "__main__":
    if "--coverage" in sys.argv:
        coverage()
    elif len(sys.argv) > 1:
        path, which = resolve(sys.argv[1])
        print(f"{which}: {path}")
    else:
        print(__doc__)
