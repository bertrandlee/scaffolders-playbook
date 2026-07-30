#!/usr/bin/env python3
"""
EPUB accessibility post-processor for The Scaffolder's Playbook.

pandoc does NOT emit EPUB Accessibility metadata, and --epub-metadata silently
accepts only a Dublin Core subset - schema.org <meta property=...> elements
passed there are dropped without warning. This script adds them after the fact,
and gives the cover image a text alternative.

Run as the LAST step of the EPUB build, after pandoc.

    python3 epub_a11y_postprocess_20260730_v1.py in.epub out.epub

WHY THIS EXISTS: [ONR-05] Multi-Modal Equity argues against excluding readers by
input modality. An EPUB with no accessibility metadata and an unlabelled cover
contradicts that in the artifact itself. Found 30 Jul 2026 by audit, not by a
reader complaint.

DELIBERATELY NOT CLAIMED: no conformsTo / certifiedBy property is written. Those
assert a WCAG conformance level, which has not been audited. Per [GOV-06], state
the ceiling rather than the comfort - the summary says what the file provides and
says plainly that it is unaudited.
"""
import os, re, shutil, subprocess, sys, tempfile, zipfile

A11Y = '''    <meta property="schema:accessMode">textual</meta>
    <meta property="schema:accessMode">visual</meta>
    <meta property="schema:accessModeSufficient">textual</meta>
    <meta property="schema:accessibilityFeature">structuralNavigation</meta>
    <meta property="schema:accessibilityFeature">tableOfContents</meta>
    <meta property="schema:accessibilityFeature">readingOrder</meta>
    <meta property="schema:accessibilityFeature">alternativeText</meta>
    <meta property="schema:accessibilityHazard">none</meta>
    <meta property="schema:accessibilitySummary">Reflowable text with a navigable table of contents to three heading levels; each pattern is a separate document in the reading order. All substantive content is text. The only images are the covers, which carry text alternatives; no information is conveyed by image alone. No audio, video or flashing content. This states what the file provides and has NOT been audited against a WCAG conformance level.</meta>
'''

COVER_ALT = ("Cover of The Scaffolder&#39;s Playbook by Bertrand Lee: "
             "Beyond Prompt Engineering to Workflow Architecture")


def main(src, out):
    work = tempfile.mkdtemp(prefix="epuba11y_")
    subprocess.run(f"cd {work} && unzip -qo {src}", shell=True, check=True)

    opf = None
    for root, _, files in os.walk(work):
        for f in files:
            if f.endswith(".opf"):
                opf = os.path.join(root, f)
    if not opf:
        print("FAIL: no .opf found"); return 2

    o = open(opf, encoding="utf-8").read()
    if "schema:accessMode" in o:
        print("note: accessibility metadata already present, not duplicating")
    else:
        if "</metadata>" not in o:
            print("FAIL: no </metadata> in OPF"); return 2
        o = o.replace("</metadata>", A11Y + "  </metadata>", 1)
        open(opf, "w", encoding="utf-8").write(o)

    fixed = 0
    for root, _, files in os.walk(work):
        for f in files:
            if f.endswith(".xhtml"):
                p = os.path.join(root, f)
                c = open(p, encoding="utf-8").read()
                new = re.sub(r"<img(?![^>]*\balt=)([^>]*)>",
                             lambda m: f'<img{m.group(1)} alt="{COVER_ALT}">', c)
                if new != c:
                    open(p, "w", encoding="utf-8").write(new); fixed += 1

    if os.path.exists(out):
        os.remove(out)
    # mimetype MUST be the first entry and stored uncompressed
    subprocess.run(f"cd {work} && zip -q -X -0 {out} mimetype", shell=True, check=True)
    subprocess.run(f"cd {work} && zip -q -X -r {out} . -x mimetype", shell=True, check=True)
    shutil.rmtree(work, ignore_errors=True)

    z = zipfile.ZipFile(out)
    first_ok = z.namelist()[0] == "mimetype"
    op = [n for n in z.namelist() if n.endswith(".opf")][0]
    o2 = z.read(op).decode()
    need = ["accessMode", "accessModeSufficient", "accessibilityFeature",
            "accessibilityHazard", "accessibilitySummary"]
    missing = [k for k in need if k not in o2]
    noalt = 0
    for n in z.namelist():
        if n.endswith(".xhtml"):
            for m in re.finditer(r"<img[^>]*>", z.read(n).decode("utf-8", "replace")):
                noalt += ("alt=" not in m.group())

    print(f"alt text added to {fixed} file(s)")
    print(f"mimetype first + stored : {first_ok}")
    print(f"a11y properties missing : {missing if missing else 'none'}")
    print(f"images without alt      : {noalt}")
    ok = first_ok and not missing and noalt == 0
    print("OK" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2]))
