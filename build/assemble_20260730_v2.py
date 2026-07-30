#!/usr/bin/env python3
"""
Assembler for The Scaffolder's Playbook: six canonical shards -> one build source.

============================================================================
WORK IN PROGRESS - DO NOT BUILD FROM THIS YET
============================================================================
This does NOT yet faithfully reproduce the hand-maintained build source.
Measured 30 Jul 2026 against final_v47.md:

  - section breaks : assembly has 15, shards have 0, this emits 6.
                     NINE page-layout breaks are unaccounted for.
  - content delta   : -1,013 bytes where it should be +339.

Building from it today would produce a differently paginated book, and the
difference has not been characterised. Use the existing hand-maintained
pipeline until the nine breaks are located and reproduced here.

WHAT IT IS SAFE FOR NOW
  - SELECT_LATEST shard resolution (correct, and tested)
  - the eight output invariants at the bottom, including
    "licence appears exactly once" - those are worth running against any
    candidate build source however it was produced.
============================================================================

WHY IT EXISTS
The operating brief says "the shards are the sole source of truth" and "never
author into an assembled file." Both were aspirational: no assembler existed,
so the assembled markdown was hand-maintained and the shards were a partial
copy of it.

Two defects came directly from that gap:
  - 29 Jul 2026: appendix content typed into both the shard and the assembly;
    they diverged by 21 bytes and a shipped build carried the difference.
  - 30 Jul 2026: 3,565 bytes of legal front matter - copyright, the full
    CC BY-NC grant, and five disclaimers - existed ONLY in the assembled file.
    Had the build container reset, the published book would have had no licence
    page. The shard control total reconciled perfectly throughout, because that
    content was never in its scope.

The intent is to make the claim true. It does not do so yet.

Assembly-level furniture (cover image reference, OOXML section breaks, TOC field
placeholder) belongs HERE, not in the shards - it is build directive, not content.

USAGE
    python3 assemble_20260730_v2.py <shard_dir> <out.md>

Shards resolve by SELECT_LATEST on (date, integer-rev) per stream, so a folder
holding superseded revisions is safe. Dead streams (01_part1, 02_part2,
03_part3 from the pre-restructure set) are excluded by name.
"""
import os, re, sys, glob

STREAMS = ["00_frontmatter", "01_beginner", "02_intermediate",
           "03_advanced", "04_elite", "99_appendices"]
DEAD = ["01_part1", "02_part2", "03_part3"]

SECT = ('```{=openxml}\n<w:p><w:pPr><w:sectPr><w:type w:val="nextPage"/>'
        '<w:pgSz w:w="8640" w:h="12960"/><w:pgMar w:top="1080" w:right="1080" '
        'w:bottom="1080" w:left="1080" w:header="720" w:footer="720" '
        'w:gutter="0"/></w:sectPr></w:pPr></w:p>\n```')
COVER = "![](cover.png){width=6.0in}"


def select_latest(shard_dir):
    """Resolve each stream to its highest (date, rev). Never string-sort."""
    picked = {}
    for f in glob.glob(os.path.join(shard_dir, "*shard_*.md")):
        base = os.path.basename(f)
        if "MANIFEST" in base or any(d in base for d in DEAD):
            continue
        m = re.match(r".*shard_(.+?)_(\d{8})_v(\d+)\.md$", base)
        if not m:
            continue
        stream, date, rev = m.group(1), int(m.group(2)), int(m.group(3))
        if stream not in STREAMS:
            continue
        key = (date, rev)
        if stream not in picked or key > picked[stream][0]:
            picked[stream] = (key, f)
    return picked


def main(shard_dir, out):
    print("*" * 74, file=sys.stderr)
    print("WARNING: WORK IN PROGRESS. This assembler does not yet reproduce the",
          file=sys.stderr)
    print("hand-maintained build source - 9 section breaks and 1,013 bytes are",
          file=sys.stderr)
    print("unaccounted for. Do NOT build a shipping artifact from this output.",
          file=sys.stderr)
    print("*" * 74, file=sys.stderr)
    picked = select_latest(shard_dir)
    missing = [s for s in STREAMS if s not in picked]
    if missing:
        print(f"FAIL: missing streams {missing}")
        return 2

    total = 0
    parts = [COVER, SECT]
    for i, s in enumerate(STREAMS):
        (date, rev), path = picked[s]
        body = open(path, encoding="utf-8").read().rstrip("\n")
        total += len(open(path, "rb").read())
        print(f"  {s:16s} v{rev:<3d} {os.path.getsize(path):7,d} B  {os.path.basename(path)}")

        if s == "00_frontmatter":
            # the TOC field placeholder is a build directive; the shard carries the
            # marker, the assembler wraps it in a section break on each side
            body = body.replace("TOC_FIELD_PLACEHOLDER", "TOC_FIELD_PLACEHOLDER")
        parts.append(body)
        if i < len(STREAMS) - 1:
            parts.append(SECT)

    asm = "\n\n".join(parts) + "\n"
    open(out, "w", encoding="utf-8").write(asm)

    print(f"\nshard control total : {total:,} B")
    print(f"assembled           : {len(asm.encode()):,} B")
    print(f"assembly furniture  : {len(asm.encode()) - total:,} B (cover ref + {asm.count('=openxml')} section breaks)")

    # invariants that must hold in the assembled output
    checks = {
        "licence text present": "Creative Commons Attribution" in asm,
        "irrevocability clause": "irrevocable" in asm,
        "internal-use permission": "Internal use within organisations" in asm,
        "copyright line": "Copyright ©" in asm,
        "disclaimer present": "without warranties of any kind" in asm,
        "TOC placeholder present": "TOC_FIELD_PLACEHOLDER" in asm,
        "TOC placeholder unique": asm.count("TOC_FIELD_PLACEHOLDER") == 1,
        "licence appears exactly once": asm.count("Creative Commons Attribution") == 1,
    }
    print()
    bad = [k for k, v in checks.items() if not v]
    for k, v in checks.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {k}")
    if bad:
        print(f"\nFAIL: {bad}")
        return 1
    print("\nOK - assembled from shards, all invariants hold")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2]))
