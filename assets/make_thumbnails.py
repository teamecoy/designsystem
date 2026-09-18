#!/usr/bin/env python3
"""Generate small thumbnails for a representative slice of the library.

Prefers the web-optimised copy (~237 KB) over the master (~24 MB) wherever the
mirror has generated one, which is roughly fifty times faster to read. Where it
has not, it falls back to the master. By default it takes one frame per unique
combination of product, pattern, colour, angle and talent; pass --all to do the
whole library, which only makes sense once the mirror is complete.
Resumable: existing thumbnails are skipped.

    python3 assets/make_thumbnails.py [--limit N]
"""
import json, os, pathlib, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from resolve_web import resolve

ROOT = pathlib.Path(__file__).resolve().parent
LIB = pathlib.Path(os.path.expanduser(
    "~/Library/CloudStorage/GoogleDrive-sam@ecoy.com.au/Shared drives/Ecoy shared drive/Photography"))
OUT = pathlib.Path(os.path.expanduser(
    "~/Library/Caches/ecoy-design-system/thumbs"))


def subset(index, everything=False):
    seen, picked = set(), []
    for r in sorted(index["files"], key=lambda r: r["path"]):
        if r.get("kind") == "video" or r.get("valid") is False:
            continue
        if everything:
            picked.append(r)
            continue
        if r.get("source") != "Real":
            continue
        key = (r["product"], r["pattern"], r["colour"], r["angle"], r["people"])
        if key in seen:
            continue
        seen.add(key)
        picked.append(r)
    return picked


def main():
    limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else None
    OUT.mkdir(parents=True, exist_ok=True)
    index = json.loads((ROOT / "library-index.json").read_text())
    picked = subset(index, everything="--all" in sys.argv)
    if limit:
        picked = picked[:limit]
    print(f"{len(picked)} images to thumbnail into {OUT}", flush=True)

    done, made, web = 0, 0, 0
    for i, r in enumerate(picked, 1):
        dst = OUT / (pathlib.Path(r["filename"]).stem + ".jpg")
        if dst.exists() and dst.stat().st_size > 0:
            done += 1
            continue
        src, which = resolve(r["path"])
        if which == "web":
            web += 1
        subprocess.run(["sips", "-s", "format", "jpeg", "-Z", "420",
                        "-s", "formatOptions", "55",
                        str(src), "--out", str(dst)],
                       capture_output=True)
        made += 1
        if made % 25 == 0:
            print(f"  {i}/{len(picked)}  ({made} new, {done} cached)", flush=True)

    json.dump([{"thumb": pathlib.Path(r["filename"]).stem + ".jpg", "path": r["path"],
                **{k: r[k] for k in ("product", "pattern", "colour", "angle", "people", "source", "seq")}}
               for r in picked], open(OUT / "manifest.json", "w"), indent=1)
    print(f"done: {made} new ({web} from the web mirror, {made - web} from masters), "
          f"{done} already cached, manifest at {OUT/'manifest.json'}")


if __name__ == "__main__":
    main()
