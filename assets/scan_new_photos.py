#!/usr/bin/env python3
"""What's new in the Drive photography library, and what won't reach the CDN.

Run after assets/build_library_index.py. Lists every image added or moved since
a date (default: the manifest's last update), split into:

  queued      eligible and in shopify-upload-manifest.json (or will be once
              build_upload_manifest.py runs)
  skipped     new but won't upload, with the reason, so a misnamed file is
              caught instead of silently left behind

    python3 assets/scan_new_photos.py                 # since the manifest's last update
    python3 assets/scan_new_photos.py --since 2026-09-29
"""
import json, os, pathlib, sys, time
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from check_filenames import check  # noqa: E402

LIB = pathlib.Path.home() / ("Library/CloudStorage/GoogleDrive-sam@ecoy.com.au/"
                             "Shared drives/Ecoy shared drive/Photography")
N = json.loads((ROOT / "naming.json").read_text())
SOURCE_EXT = set(N["library"]["web"]["sourceExtensions"])
EXCLUDED = N["library"]["web"]["excludedFolders"]
RETIRED = set(json.loads((ROOT / "colour-status.json").read_text())["retired"])


def main():
    manifest = json.loads((ROOT / "shopify-upload-manifest.json").read_text())
    since = (sys.argv[sys.argv.index("--since") + 1] if "--since" in sys.argv
             else manifest.get("updated", "2026-09-22"))
    cutoff = time.mktime(time.strptime(since, "%Y-%m-%d"))
    listed = {f["name"].rsplit(".", 1)[0] for f in manifest["files"]}
    stems = Counter()
    for _, _, fs in os.walk(LIB):
        stems.update(pathlib.Path(f).stem for f in fs)

    queued, skipped = Counter(), defaultdict(list)
    for d, dirs, fs in os.walk(LIB):
        dirs[:] = [x for x in dirs if not x.startswith(".")]
        for f in fs:
            if f.startswith(".") or f == "Icon\r":
                continue
            p = pathlib.Path(d) / f
            try:
                st = p.stat()
            except OSError:
                continue
            if max(st.st_mtime, getattr(st, "st_birthtime", 0)) < cutoff:
                continue
            rel = p.relative_to(LIB)
            where = " / ".join(rel.parts[:3])
            stem, ext = p.stem, p.suffix.lower()
            problems = check(f)
            colour = next((t for t in stem.split("-") if t in RETIRED), None)
            if stem in listed:
                queued[where] += 1
            elif ext not in SOURCE_EXT:
                skipped[where].append((f, f"{ext or 'no extension'} isn't converted to web"))
            elif any(x in str(rel) for x in EXCLUDED):
                skipped[where].append((f, "excluded folder (left alone on purpose)"))
            elif problems:
                skipped[where].append((f, problems[0]))
            elif colour:
                skipped[where].append((f, f"retired colour {colour}"))
            elif stems[stem] > 1:
                skipped[where].append((f, "the same name exists elsewhere in the library"))
            else:
                queued[where] += 1   # valid; build_upload_manifest.py will add it

    print(f"New or moved since {since}:")
    print(f"\n  QUEUED ({sum(queued.values())})")
    for k, v in sorted(queued.items()):
        print(f"    {v:5}  {k}")
    n = sum(len(v) for v in skipped.values())
    print(f"\n  SKIPPED ({n}) - these won't reach the CDN until fixed")
    for k, v in sorted(skipped.items()):
        print(f"    {len(v):5}  {k}")
        for f, why in v[:3]:
            print(f"             {f}  ({why})")
    return 1 if n else 0


if __name__ == "__main__":
    sys.exit(main())
