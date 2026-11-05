"""Build a chapter's MCQ Sheet (PDF + Word) from its source/mcq_data.py.

Usage: python3 build_mcq.py "<chapter folder>"

Writes into the chapter folder:
  MCQ Sheet.pdf / .docx               questions only
  MCQ Sheet - Solutions.pdf / .docx   answer grid + worked solutions
Prints every question whose answer differs from the book's key.
"""
import html
import re
import runpy
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import pypandoc

TOOLS = Path(__file__).resolve().parent
BUILD = TOOLS.parent / "_build"  # inside the workspace: snap Chromium can't read /tmp or dot-folders
KATEX_DIST = Path.home() / ".local/share/hsc-tools/node_modules/katex/dist"
PANDOC = pypandoc.get_pandoc_path()
# Noto Serif Bengali (OFL), from github.com/google/fonts; installed to ~/.local/share/fonts on 2026-11-05
BANGLA_FONT = Path.home() / ".local/share/fonts/NotoSerifBengali[wdth,wght].ttf"
BANGLA_FONT_NAME = "Noto Serif Bengali"

LABELS = ["ক", "খ", "গ", "ঘ"]
TYPE_NAMES = {
    "simple": "সাধারণ বহুনির্বাচনি প্রশ্ন",
    "multi": "বহুপদী সমাপ্তিসূচক বহুনির্বাচনি প্রশ্ন",
    "stimulus": "অভিন্ন তথ্যভিত্তিক বহুনির্বাচনি প্রশ্ন",
}
ROMAN = ["i", "ii", "iii", "iv"]


def esc_brackets(s):
    return s.replace("[", r"\[").replace("]", r"\]")


def wide(opts):
    return any("matrix" in o or len(o) > 22 for o in opts) or sum(map(len, opts)) > 30


def opts_md(opts, fmt):
    if fmt == "html":
        cls = "c2" if wide(opts) else "c4"
        body = "\n\n".join(f"[({l})]{{.ol}} {o}" for l, o in zip(LABELS, opts))
        return f"::: {{.opts .{cls}}}\n{body}\n:::\n"
    # Word: one line of four, or two lines of two when the options are tall
    cells = [f"**({l})** {o}" for l, o in zip(LABELS, opts)]
    gap = "  "
    if wide(opts):
        return gap.join(cells[:2]) + "\n\n" + gap.join(cells[2:]) + "\n"
    return gap.join(cells) + "\n"


def question_md(n, q, fmt):
    tag = f"[{esc_brackets('[' + q['tag'] + ']')}]{{.tag}}" if fmt == "html" else esc_brackets(f"[{q['tag']}]")
    lines = [f"::: {{.q}}", f"**{n}.** {tag} {q['stem']}" if fmt == "html" else f"**{n}.** {q['stem']} {tag}", ""]
    if q.get("items"):
        items = "\n\n".join(f"{r}. {t}" for r, t in zip(ROMAN, q["items"]))
        lines += ["::: {.items}", items, ":::", "", "নিচের কোনটি সঠিক?", ""]
    lines += [opts_md(q["opts"], fmt), ":::", ""]
    return "\n".join(lines)


def walk(data):
    """Yield (event, payload) in sheet order, numbering questions 1..N."""
    n = 0
    for sec in data["SECTIONS"]:
        yield "section", sec["name"]
        for topic in sec["topics"]:
            yield "topic", topic["name"]
            for g in topic["groups"]:
                yield "type", TYPE_NAMES[g["type"]]
                if g["type"] == "stimulus":
                    for st in g["stimuli"]:
                        nums = list(range(n + 1, n + 1 + len(st["questions"])))
                        yield "stimulus", (st["text"], nums)
                        for q in st["questions"]:
                            n += 1
                            yield "q", (n, q)
                else:
                    for q in g["questions"]:
                        n += 1
                        yield "q", (n, q)


def questions_md(data, fmt):
    out = []
    for ev, p in walk(data):
        if ev == "section":
            out.append(f"# {p}\n")
        elif ev == "topic":
            out.append(f"## {p}\n")
        elif ev == "type":
            out.append(f"### {p}\n")
        elif ev == "stimulus":
            text, nums = p
            rng = " ও ".join(map(str, nums)) if len(nums) <= 2 else f"{nums[0]}–{nums[-1]}"
            out.append(f"::: {{.stim}}\nনিচের উদ্দীপকের আলোকে {rng} নং প্রশ্নের উত্তর দাও:\n\n{text}\n:::\n")
        elif ev == "q":
            out.append(question_md(*p, fmt))
    return "\n".join(out)


def solutions_md(data):
    qs = [p for ev, p in walk(data) if ev == "q"]
    grid = " ".join(f"**{n}.** {q['ans']}" for n, q in qs)
    out = ["::: {.key}", "**উত্তরমালা:** " + grid, ":::", ""]
    for ev, p in walk(data):
        if ev == "section":
            out.append(f"# {p}\n")
        elif ev == "topic":
            out.append(f"## {p}\n")
        elif ev == "q":
            n, q = p
            out += ["::: {.s}", f"**{n}.** {esc_brackets('[' + q['tag'] + ']')} — উত্তর: **({q['ans']})**", "", q["sol"], ""]
            if q.get("book") and q["book"] != q["ans"]:
                out += ["::: {.flag}",
                        f"⚠ বইয়ের উত্তরমালায় ({q['book']}) দেওয়া আছে। আমাদের হিসাবে সঠিক উত্তর ({q['ans']})।",
                        ":::", ""]
            out += [":::", ""]
    return "\n".join(out)


def header(data):
    return (f'<div class="title"><div class="t1">{data["TITLE"]}</div>'
            f'<div class="t2">{data["CHAPTER"]}</div><div class="t3">{{sub}}</div></div>')


def render_pdf(md, data, sub, pdf_path, two_cols):
    frag = pypandoc.convert_text(md, "html", format="markdown", extra_args=["--katex"])
    frag = subprocess.run(["node", str(TOOLS / "katex_render.mjs")], input=frag, capture_output=True, text=True)
    if frag.returncode:
        sys.exit(frag.stderr)
    body = frag.stdout
    page = f"""<!doctype html><html lang="bn"><head><meta charset="utf-8">
<link rel="stylesheet" href="katex/katex.min.css"><link rel="stylesheet" href="mcq.css"></head>
<body>{header(data).replace('{sub}', html.escape(sub))}<div class="{'cols' if two_cols else ''}">{body}</div></body></html>"""
    BUILD.mkdir(exist_ok=True)
    if not (BUILD / "katex").exists():
        shutil.copytree(KATEX_DIST, BUILD / "katex")
    shutil.copy(TOOLS / "mcq.css", BUILD / "mcq.css")
    (BUILD / "fonts").mkdir(exist_ok=True)
    shutil.copy(BANGLA_FONT, BUILD / "fonts" / "NotoSerifBengali.ttf")
    page_path = BUILD / (pdf_path.stem + ".html")
    page_path.write_text(page, encoding="utf-8")
    tmp_pdf = BUILD / (pdf_path.stem + ".pdf")
    subprocess.run(["chromium", "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={tmp_pdf}", page_path.as_uri()],
                   check=True, capture_output=True)
    shutil.move(tmp_pdf, pdf_path)


def reference_docx():
    """pandoc's default Word template, with the Bangla (complex-script) font set to Noto Serif Bengali."""
    ref = BUILD / "reference.docx"
    BUILD.mkdir(exist_ok=True)
    default = subprocess.run([PANDOC, "--print-default-data-file", "reference.docx"], capture_output=True, check=True).stdout
    src = BUILD / "reference-default.docx"
    src.write_bytes(default)
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(ref, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            buf = zin.read(item.filename)
            if item.filename == "word/styles.xml":
                xml = buf.decode("utf-8")
                # every rFonts element gets w:cs (the font Word uses for Bangla) plus a Bangla language tag
                xml = re.sub(r"<w:rFonts\b([^>]*?)\s*/>",
                             lambda m: "<w:rFonts" + re.sub(r'\sw:cs(theme)?="[^"]*"', "", m.group(1))
                             + f' w:cs="{BANGLA_FONT_NAME}" />', xml)
                xml = re.sub(r"<w:lang\b[^>]*/>", '<w:lang w:val="en-US" w:bidi="bn-BD" />', xml)
                buf = xml.encode("utf-8")
            zout.writestr(item, buf)
    return ref


def render_docx(md, data, sub, docx_path, ref):
    pypandoc.convert_text(md, "docx", format="markdown", outputfile=str(docx_path),
                          extra_args=["--reference-doc", str(ref),
                                      "-M", f"title={data['TITLE']}", "-M", f"subtitle={data['CHAPTER']} — {sub}"])


def main():
    chapter = Path(sys.argv[1]).resolve()
    data = runpy.run_path(str(chapter / "source" / "mcq_data.py"))

    for q in (p[1] for ev, p in walk(data) if ev == "q"):
        if len(q["opts"]) != 4 or q["ans"] not in LABELS:
            sys.exit(f"Bad question {q['tag']}: needs 4 options and ans in ক/খ/গ/ঘ")

    qs_sub = data["SUBTITLE"]
    sol_sub = data["SUBTITLE"] + " — সমাধান"
    render_pdf(questions_md(data, "html"), data, qs_sub, chapter / "MCQ Sheet.pdf", two_cols=True)
    render_pdf(solutions_md(data), data, sol_sub, chapter / "MCQ Sheet - Solutions.pdf", two_cols=False)
    ref = reference_docx()
    render_docx(questions_md(data, "docx"), data, qs_sub, chapter / "MCQ Sheet.docx", ref)
    render_docx(solutions_md(data), data, sol_sub, chapter / "MCQ Sheet - Solutions.docx", ref)

    flags = [(n, q) for ev, (n, q) in ((e, p) for e, p in walk(data) if e == "q") if q.get("book") and q["book"] != q["ans"]]
    total = sum(1 for ev, _ in walk(data) if ev == "q")
    print(f"Built {total} questions into {chapter}")
    for n, q in flags:
        print(f"  FLAG Q{n} [{q['tag']}]: book says {q['book']}, worked answer {q['ans']}")


if __name__ == "__main__":
    main()
