#!/usr/bin/env python3
"""Fold vision descriptions into the library index.

Each described_N.json holds one object per thumbnail: what is actually in the
frame, which colours are visible, the setting, whether a person appears, whether
it looks dated against the current wordmark, and a quality grade. This merges
them onto the matching rows of library-index.json under a "seen" key.

    python3 assets/merge_descriptions.py
"""
import json, os, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent
THUMBS = pathlib.Path(os.path.expanduser("~/Library/Caches/ecoy-design-system/thumbs"))
FIELDS = ("subject", "colours", "setting", "people", "dated", "quality", "note")


def load_described():
    out = {}
    for p in sorted(THUMBS.glob("described_*.json")):
        raw = p.read_text().strip()
        raw = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw)      # tolerate fenced output
        start, end = raw.find("["), raw.rfind("]")
        if start == -1 or end == -1:
            print(f"  skipped {p.name}: no JSON array found", file=sys.stderr)
            continue
        try:
            rows = json.loads(raw[start:end + 1])
        except json.JSONDecodeError as e:
            print(f"  skipped {p.name}: {e}", file=sys.stderr)
            continue
        for r in rows:
            if r.get("thumb"):
                out[pathlib.Path(r["thumb"]).stem] = r
        print(f"  {p.name}: {len(rows)} rows", file=sys.stderr)
    return out


def main():
    described = load_described()
    if not described:
        sys.exit("No described_*.json files found.")

    idx = json.loads((ROOT / "library-index.json").read_text())
    matched = 0
    for row in idx["files"]:
        stem = pathlib.Path(row["path"]).stem
        d = described.get(stem)
        if not d:
            continue
        seen = {k: d[k] for k in FIELDS if k in d and d[k] not in (None, "", [])}
        if seen:
            row["seen"] = seen
            matched += 1

    idx["counts"]["described"] = matched
    idx["$comment"] = (idx["$comment"].split(" Rows omit")[0] +
                       " Rows with a \"seen\" object have been looked at: that describes what is "
                       "actually in the frame, which can differ from the filename. "
                       "Rows omit fields that are null.")
    (ROOT / "library-index.json").write_text(
        json.dumps(idx, separators=(",", ":"), ensure_ascii=False) + "\n")

    dated = [r for r in idx["files"] if r.get("seen", {}).get("dated")]
    weak = [r for r in idx["files"] if r.get("seen", {}).get("quality") == "weak"]
    hero = [r for r in idx["files"] if r.get("seen", {}).get("quality") == "hero"]
    print(f"\nmerged {matched} descriptions of {len(described)} available")
    print(f"  hero {len(hero)}   weak {len(weak)}   dated {len(dated)}")
    if dated:
        print("\ndated (old wordmark or old packaging):")
        for r in dated:
            print(f"   {pathlib.Path(r['path']).name}")


if __name__ == "__main__":
    main()
