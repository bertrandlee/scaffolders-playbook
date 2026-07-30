# SHARD MANIFEST v19 — canonical pointer for The Scaffolder's Playbook

**AS OF** Thu 30 Jul 2026, 08:26 SST (2026-07-30T00:26:57Z; clock probed immediately before this write)

**Supersedes MANIFEST v18** (`1TYYYHp_AexbirH1z0m6sUIvptfBZwN9b`, 5,843 B). One row superseded: frontmatter. **v18's control total of 127,752 is wrong for a reason that matters — see §2.**

---

## 1 · CANONICAL SHARDS — read in this order

| # | File | fileId | Bytes |
|---|---|---|---|
| 1 | `scaffolders_manifesto_shard_00_frontmatter_20260729_v29.md` | `1WAXH3UrEfLPF4Ck2FxcFN6EqwkRVFx0C` | 25,595 |
| 2 | `scaffolders_manifesto_shard_01_beginner_20260729_v8.md` | `1zPEreh24uUrQbhcCtEgMBHt54O5dwknk` | 11,840 |
| 3 | `scaffolders_manifesto_shard_02_intermediate_20260729_v10.md` | `1V-ifCb6ztss7-lE7W95BwEw-Eb91Af-w` | 27,885 |
| 4 | `scaffolders_manifesto_shard_03_advanced_20260729_v9.md` | `1fmyHSJUzqEDvzXeReBzxuJ5JGqoHxNdJ` | 24,172 |
| 5 | `scaffolders_manifesto_shard_04_elite_20260729_v13.md` | `1mJVxesdwn_g-fnUkm0igcJldEzZnNvMj` | 22,398 |
| 6 | `scaffolders_manifesto_shard_99_appendices_20260729_v7.md` | `1tpEcFUBELDYAeI0dTIVreeD4xUhl8lJP` | 19,768 |

**Control total: 131,658 bytes.** Previous (v18): 127,752 B. Delta: **+3,906 B**, frontmatter v28→v29 only.

**50 patterns.** ONR 5 · PRAC 11 · ARC 9 · SCF 14 · GOV 7 · SAFE 4.

Frontmatter v29 owner-uploaded, reconciled at exactly 25,595 B, `parentId` confirmed. **SIZE-VERIFIED plus content probes, not byte-verified** — Drive's bytes were not round-tripped and hash-compared. The chain is "a file of the correct length containing the expected strings," not "identical to the container copy."

---

## 2 · WHY THIS REVISION EXISTS — the control total was measuring a subset

**3,565 bytes of the book had no home in any canonical shard.** Found 30 Jul 2026 while applying a one-paragraph licence edit. All six shards returned zero occurrences of `Creative Commons`, `irrevocable` and `Copyright ©`.

What was missing:

- the copyright line and publisher statement
- the ISBN placeholder
- **the entire CC BY-NC 4.0 grant**, including the irrevocability clause
- five disclaimers: non-affiliation, honest-opinion on platform criticism, no professional advice, as-is warranty, liability limitation

It existed **only in the assembled build file** — which the operating brief explicitly calls "a disposable output of a render step," held in a container that does not persist between sessions. Had the container reset, the published book would have had **no licence page at all**, and "free, forkable" on the back cover would have reverted to a claim with nothing behind it.

**The verification failure is the part worth recording.** The shard control total reconciled perfectly throughout — 127,752 checked out against six shards every time, and always would have, because the missing content was never in its scope. A green reconciliation reported "the manuscript is intact" while roughly a twentieth of the book sat outside the check. **The build gate inherited the same blind spot:** test `S02` asserts the shard total, so it would have passed indefinitely with the licence page absent.

**Control total now means something different and stronger.** From v19 it covers the legal front matter as well as the body. A pointer that reconciles is now a pointer to a complete book.

**Root cause: there is no assembler.** "The shards are the sole source of truth" has been aspirational for as long as nothing turned shards into a build source. The assembled file has been the real source; the shards a partial copy of it. That single cause produced two symptoms — the 29 Jul appendix divergence of 21 bytes, cosmetic; and this, legal. A draft assembler exists (`assemble_20260730_v1.py`, Process/) but is **not yet faithful**: the hand-maintained assembly carries 15 OOXML section breaks against the assembler's 6, and content differs by −1,013 bytes. **Do not build from it yet.**

---

## 3 · WHAT CHANGED IN THE MANUSCRIPT (v18 → v19)

**Legal front matter back-ported into shard_00**, verbatim from the assembled file, 3,565 B.

**Plus one owner-directed addition, 339 B** — an explicit internal-use grant, because the NonCommercial term is genuinely contested for staff training at a for-profit company and a cautious corporate legal reviewer would block adoption on the ambiguity alone:

> *Internal use within organisations is expressly permitted: you may copy, circulate and use this book for training, onboarding and reference inside your organisation — commercial or otherwise — at no charge and without seeking permission. What the NonCommercial term withholds is selling this book, or selling a work derived from it.*

This adds a permission rather than altering the licence. CC allows it, and the asymmetry is deliberate: permissions can be widened later, never narrowed.

---

## 4 · BUILD STATUS

**Reviewer build remains `scaffolders_playbook_REVIEW_v47_20260730`** — 138 pp, gate 23/23, in Book Review. Philip Su and Huey Siah hold it, target Tue 12 Aug 2026.

**v47 predates this shard revision.** It contains the legal front matter (it was built from the assembled file, which had it) but not the internal-use clause. **No re-send** — the difference is one paragraph and R3 must not be disturbed again. It lands in the post-review build.

**Pending, not yet done:** a gate check asserting the licence and disclaimer text is present in the built PDF. Until it exists, the class of defect described in §2 remains undetectable by the suite.

---

*Authored fresh by Book thread, Thu 30 Jul 2026, 08:26 SST. Every fileId from a Drive metadata response this session; the +3,906 B delta predicted before the write and confirmed after; the absent-from-shards finding established by grepping all six shards, not inferred.*
