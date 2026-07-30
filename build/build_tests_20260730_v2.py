#!/usr/bin/env python3
"""
Build regression tests for The Scaffolder's Playbook.

Asserts the three built artifacts against build_expectations.json.
The expectations file is the reference; this script never edits it.

Usage:
    python3 build_tests.py <docx> <pdf> <epub> [--expect build_expectations.json]

Exit 0 = all pass. Exit 1 = at least one FAIL. Exit 2 = could not run.

WHAT THIS CANNOT CATCH (state it, don't imply coverage):
  - prose quality, tone, argument, factual correctness
  - wrong-but-plausible content that is well-formed
  - anything not declared in the expectations file
  - visual layout beyond what OCR and text extraction expose
A green run means "no declared invariant is violated", not "the book is correct".
"""

import json, os, re, subprocess, sys, zipfile, glob, tempfile

TR = str.maketrans({'\u2019': "'", '\u2018': "'", '\u201c': '"', '\u201d': '"',
                    '\u2014': '-', '\u2013': '-'})
norm = lambda t: re.sub(r'\s+', ' ', t.translate(TR)).strip()

results = []


def check(tid, name, ok, detail=""):
    results.append((tid, name, bool(ok), detail))


def sh(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout


# ---------------------------------------------------------------- docx tests

def test_docx(path, E):
    d = E["docx"]
    try:
        z = zipfile.ZipFile(path)
    except Exception as e:
        check("D00", "docx opens", False, str(e)); return
    check("D00", "docx opens", True)

    styles = z.read('word/styles.xml').decode()
    h3 = re.search(r'<w:style[^>]*w:styleId="Heading3"[^>]*>.*?</w:style>', styles, re.S)
    if not h3:
        check("D01", "Heading3 style exists", False)
    else:
        g = h3.group()
        check("D01", "Heading3 style exists", True)
        check("D02", "Heading3 pageBreakBefore (every pattern starts a page)",
              ('pageBreakBefore' in g) == d["heading3_pagebreak_before"],
              f"found={'pageBreakBefore' in g} expected={d['heading3_pagebreak_before']}")
        check("D03", "Heading3 keepNext",
              ('keepNext' in g) == d["heading3_keepnext"])

    doc = z.read('word/document.xml').decode()

    n_valign = doc.count('w:vAlign')
    check("D04", "centered opener sections",
          n_valign >= d["centered_opener_sections"],
          f"found={n_valign} expected>={d['centered_opener_sections']}")

    n_cons = doc.count('w:ascii="Consolas"')
    check("D05", "Consolas quote runs",
          n_cons >= d["consolas_quote_replacements"],
          f"found={n_cons} expected>={d['consolas_quote_replacements']}")

    ct = z.read('[Content_Types].xml').decode()
    parts = re.findall(r'PartName="([^"]+)"', ct)
    dupes = sorted({p for p in parts if parts.count(p) > 1})
    check("D06", "Content_Types has no duplicate PartName",
          len(dupes) == d["content_types_duplicates"], f"dupes={dupes}")

    try:
        from lxml import etree
        etree.fromstring(doc.encode())
        check("D07", "document.xml well-formed", True)
    except Exception as e:
        check("D07", "document.xml well-formed", False, str(e)[:120])

    check("D08", "cover image extent",
          f'cx="{d["cover_extent_cx"]}"' in doc and f'cy="{d["cover_extent_cy"]}"' in doc)

    check("D09", "no unreplaced TOC placeholder", 'TOC_FIELD_PLACEHOLDER' not in doc)


# ----------------------------------------------------------------- pdf tests

def test_pdf(path, E):
    p = E["pdf"]
    info = sh(["pdfinfo", path])
    m = re.search(r'Pages:\s+(\d+)', info)
    if not m:
        check("P00", "pdf readable", False); return
    n = int(m.group(1))
    check("P00", "pdf readable", True)
    check("P01", "page count in range",
          p["page_count_min"] <= n <= p["page_count_max"],
          f"pages={n} range={p['page_count_min']}-{p['page_count_max']}")

    pages = [norm(sh(["pdftotext", "-f", str(i), "-l", str(i), path, "-"]))
             for i in range(1, n + 1)]
    full = "\n".join(pages)

    # forbidden / required strings in the text layer
    bad = [s for s in E["text_layer_forbidden"] if norm(s) in full]
    check("P02", "no forbidden strings in text layer", not bad, f"found={bad}")

    missing = [s for s in E["text_layer_required"] if norm(s) not in full]
    check("P03", "required strings present", not missing, f"missing={missing}")

    # TOC: any entry rendered with '?' means an unresolved page number
    toc_pages = [t for t in pages if 'TABLE OF CONTENTS' in t]
    q = sum(t.count('. ?') + t.count('.?') for t in toc_pages)
    check("P04", "TOC has no unresolved page numbers",
          q == p["toc_unresolved_entries"], f"unresolved={q}")

    # every sampled pattern heading must start a page.
    # offset 0 only - a mid-page hit is either a real regression or a cross-reference,
    # so we require at least one page where the heading is the first text on it.
    body = next((i for i, t in enumerate(pages, 1)
                 if 'There is a colleague available to you now' in t), 1)
    not_top = []
    for title in E["pattern_headings_sample"]:
        nt = norm(title)
        found_top = any(pages[i - 1].startswith(nt) for i in range(body, n + 1))
        if not found_top:
            not_top.append(title)
    check("P05", "every sampled pattern heading starts a page",
          not not_top, f"not_at_top={not_top}")

    # back cover: baked image, needs OCR. This is the check that was missing.
    word = p["back_cover_count_word"]
    if not sh(["which", "tesseract"]).strip():
        check("P06", f"back cover OCR says '{word}'", False, "tesseract not installed")
    else:
        with tempfile.TemporaryDirectory() as td:
            subprocess.run(["pdftoppm", "-f", str(n), "-l", str(n), "-r", "110",
                            "-png", path, f"{td}/bc"], capture_output=True)
            imgs = sorted(glob.glob(f"{td}/bc*.png"))
            if not imgs:
                check("P06", f"back cover OCR says '{word}'", False, "rasterise failed")
            else:
                txt = sh(["tesseract", imgs[-1], "-"])
                line = [l for l in txt.split('\n') if 'tested patterns' in l]
                ok = any(word.lower() in l.lower() for l in line)
                check("P06", f"back cover OCR says '{word}'", ok,
                      f"ocr={line[0].strip()[:70] if line else 'no match'}")

    return full


# ------------------------------------------------------- legal front matter

def rnorm(t):
    """Renderer-tolerant normalise. The PDF exporter drops hyphens at break points -
    'non-commercial' comes out as 'noncommercial' - so comparison ignores hyphens."""
    t = t.translate(TR).replace('-', '')
    return re.sub(r'\s+', ' ', t).strip()


def test_legal(pdf_text, E, shard_dir):
    """The licence page and disclaimers must survive into the BUILT artifact.

    Exists because 3,565 B of legal front matter - copyright, the full CC BY-NC
    grant, five disclaimers - lived only in the disposable assembled file and was in
    NO canonical shard. The shard control total reconciled perfectly throughout,
    because that content was never in its scope; S02 would have passed indefinitely
    with the licence page absent. Build v26 (25 Jul 2026) shipped with none of it.

    Probes are anchors into the canonical frontmatter shard, never typed from memory:
    on 30 Jul two of three hand-written probes were wrong about their own wording.
    L01 asserts the probes still exist in the source. L02 asserts they reached the
    reader. Both are needed - L02 alone would silently pass if a probe drifted into
    something the source never said.
    """
    probes = E.get("legal_required_in_pdf", [])
    if not probes:
        check("L00", "legal probes declared", False, "legal_required_in_pdf is empty")
        return

    if shard_dir and os.path.isdir(shard_dir):
        fm = glob.glob(os.path.join(shard_dir, "*frontmatter*.md"))
        if fm:
            source = open(sorted(fm)[-1], encoding="utf-8").read()
            drift = [p for p in probes if p not in source]
            check("L01", "every legal probe is anchored in the frontmatter shard",
                  not drift, f"not_in_source={drift}")

    missing = [p for p in probes if rnorm(p) not in rnorm(pdf_text)]
    check("L02", "licence and disclaimers present in built PDF",
          not missing, f"missing={missing}")


# ---------------------------------------------------------------- epub tests

def test_epub(path, E):
    e = E["epub"]
    try:
        z = zipfile.ZipFile(path)
    except Exception as ex:
        check("E00", "epub opens", False, str(ex)); return
    check("E00", "epub opens", True)
    names = z.namelist()
    content = [x for x in names if x.endswith('.xhtml') and 'nav' not in x]
    check("E01", "epub split per pattern",
          len(content) >= e["content_files_min"],
          f"content_files={len(content)} expected>={e['content_files_min']}")
    check("E02", "epub cover present",
          any('cover' in x.lower() for x in names) == e["cover_present"])
    bad = []
    joined = "\n".join(z.read(x).decode('utf-8', 'replace') for x in content[:40])
    for s in E["text_layer_forbidden"]:
        if norm(s) in norm(joined):
            bad.append(s)
    check("E03", "no forbidden strings in epub content", not bad, f"found={bad}")


# ------------------------------------------------------------ shard totals

def test_shards(E, shard_dir):
    m = E["manuscript"]
    if not shard_dir or not os.path.isdir(shard_dir):
        print("  [SKIP] S01-S02  shard totals (no --shards given)\n")
        return
    files = sorted(glob.glob(os.path.join(shard_dir, "*shard_*.md")))
    files = [f for f in files if 'MANIFEST' not in f]
    total = sum(os.path.getsize(f) for f in files)
    check("S01", "shard count", len(files) == m["shard_count"],
          f"found={len(files)} expected={m['shard_count']}")
    check("S02", "shard control total",
          total == m["shard_control_total_bytes"],
          f"found={total} expected={m['shard_control_total_bytes']}")


# ---------------------------------------------------------------------- main

def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    exp = "build_expectations.json"
    if '--expect' in sys.argv:
        exp = sys.argv[sys.argv.index('--expect') + 1]
    shard_dir = None
    if '--shards' in sys.argv:
        shard_dir = sys.argv[sys.argv.index('--shards') + 1]

    if len(args) < 3:
        print(__doc__); return 2
    docx, pdf, epub = args[0], args[1], args[2]

    with open(exp) as f:
        E = json.load(f)

    print(f"expectations: {exp} (v{E.get('_version')}, {E.get('_as_of')})\n")

    test_shards(E, shard_dir)
    test_docx(docx, E)
    pdf_text = test_pdf(pdf, E)
    test_epub(epub, E)
    if pdf_text:
        test_legal(pdf_text, E, shard_dir)

    fails = [r for r in results if not r[2]]
    for tid, name, ok, detail in results:
        mark = "PASS" if ok else "FAIL"
        line = f"  [{mark}] {tid}  {name}"
        if detail and not ok:
            line += f"\n              -> {detail}"
        print(line)

    print(f"\n{len(results) - len(fails)}/{len(results)} passed")
    if fails:
        print("\nFAILED:")
        for tid, name, _, detail in fails:
            print(f"  {tid}  {name}  {detail}")
        print("\nA failure means EITHER the build regressed OR build_expectations.json")
        print("is stale. Decide which. Never edit expectations to match a broken build.")
        return 1
    print("\nAll declared invariants hold. This does NOT mean the book is correct -")
    print("see the docstring for what this suite cannot catch.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
