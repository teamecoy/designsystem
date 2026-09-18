#!/usr/bin/env python3
"""Generate small thumbnails for a representative slice of the library.

Reading an original streams 20-55 MB from Drive, about 12 seconds each, so this
does NOT thumbnail everything. It takes one frame per unique combination of
product, pattern, colour, angle and talent, which covers the whole library's
variety in a fraction of the files. Resumable: existing thumbnails are skipped.

    python3 assets/make_thumbnails.py [--limit N]
"""
import json, os, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent
LIB = pathlib.Path(os.path.expanduser(
    "~/Library/CloudStorage/GoogleDrive-sam@ecoy.com.au/Shared drives/Ecoy shared drive/Photography"))
OUT = pathlib.Path(os.path.expanduser(
    "~/Library/Caches/ecoy-design-system/thumbs"))


def subset(index):
    seen, picked = set(), []
    for r in sorted(index["files"], key=lambda r: r["path"]):
        if r["kind"] != "image" or not r["valid"] or r["source"] != "Real":
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
    picked = subset(index)
    if limit:
        picked = picked[:limit]
    print(f"{len(picked)} images to thumbnail into {OUT}", flush=True)

    done, made = 0, 0
    for i, r in enumerate(picked, 1):
        dst = OUT / (pathlib.Path(r["filename"]).stem + ".jpg")
        if dst.exists() and dst.stat().st_size > 0:
            done += 1
            continue
        subprocess.run(["sips", "-s", "format", "jpeg", "-Z", "420",
                        "-s", "formatOptions", "55",
                        str(LIB / r["path"]), "--out", str(dst)],
                       capture_output=True)
        made += 1
        if made % 25 == 0:
            print(f"  {i}/{len(picked)}  ({made} new, {done} cached)", flush=True)

    json.dump([{"thumb": pathlib.Path(r["filename"]).stem + ".jpg", "path": r["path"],
                **{k: r[k] for k in ("product", "pattern", "colour", "angle", "people", "source", "seq")}}
               for r in picked], open(OUT / "manifest.json", "w"), indent=1)
    print(f"done: {made} new, {done} already cached, manifest at {OUT/'manifest.json'}")


if __name__ == "__main__":
    main()
