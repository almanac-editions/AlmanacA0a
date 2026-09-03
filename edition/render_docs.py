#!/usr/bin/env python3
"""Render the edition's markdown guides to HTML, so a browser shows a page and not a text file.

WHY. A web server hands `.md` to a browser as plain text; on the published site the guides arrived
as an unstyled wall. The Overseer asked for HTML and this is it. The markdown files STAY — they are
what an unzipped copy and an AI agent read, and `AGENTS.md` routes to one of them by name.

WHEN IT RUNS. Inside the build, AFTER the build-class banner is stamped into the markdown and
BEFORE checksums are taken. That ordering is not cosmetic: this build has already learned twice
that a transform applied after hashing puts a file on the reader's disk that the integrity record
does not describe.

DEPENDENCY: `markdown` (BSD-3-Clause), installed for the interpreter that runs this. It refuses
rather than degrading — a guide silently shipped as raw markup inside an .html file would look like
a rendering failure to every reader and like a success to the build.
"""
import html
import os
import re
import sys

try:
    import markdown
except ImportError:
    sys.exit("render_docs: needs the `markdown` package:  python3 -m pip install --user markdown")

DOCS = ["FOR_A_HUMAN.md", "FOR_AN_AI_AGENT.md", "EDITION.md",
        "EMBEDDING_NOTE.md", "AUTHORSHIP.md", "ANCESTRY.md",
        # markdown that lives deeper than the root but is still something a reader is sent to
        "source/informal/proofv0a.ledger.cas_receipts.md",
        "source/informal/REFEREE_REPORT_PROOFv0a.md"]

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__ — Almanac A0a</title>
<style>
:root{--paper:#fbfbfa;--ink:#16181a;--dim:#585f66;--rule:#e3e6e8;--link:#2a78d6;--code:#f2f4f5}
@media (prefers-color-scheme:dark){
 :root{--paper:#14171a;--ink:#e9edf0;--dim:#9aa4ac;--rule:#2a3036;--link:#7cb2f2;--code:#1c2126}}
*{box-sizing:border-box}
body{background:var(--paper);color:var(--ink);margin:0;
 font:16.5px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
main{max-width:47rem;margin:0 auto;padding:2.6rem 1.2rem 5rem}
h1,h2,h3{line-height:1.25;margin:2.2rem 0 .7rem}
h1{font-size:1.8rem;margin-top:0} h2{font-size:1.28rem;border-bottom:1px solid var(--rule);padding-bottom:.3rem}
h3{font-size:1.06rem}
a{color:var(--link)} p,li{overflow-wrap:anywhere}
code{background:var(--code);padding:.12em .35em;border-radius:3px;font-size:.9em}
pre{background:var(--code);padding:.85rem 1rem;border-radius:5px;overflow-x:auto}
pre code{background:none;padding:0}
table{border-collapse:collapse;width:100%;margin:1rem 0;font-size:.94em;display:block;overflow-x:auto}
th,td{border:1px solid var(--rule);padding:.42rem .6rem;text-align:left;vertical-align:top}
blockquote{margin:1rem 0;padding:.1rem 1rem;border-left:3px solid var(--rule);color:var(--dim)}
hr{border:0;border-top:1px solid var(--rule);margin:2rem 0}
.back{display:inline-block;margin-bottom:1.6rem;font-size:.92em}
img{max-width:100%;height:auto}
</style>
</head>
<body><main>
<a class="back" href="__ROOT__index.html">&larr; the almanac</a>
__BODY__
</main></body></html>
"""


def convert(directory):
    made = []
    present = {d for d in DOCS if os.path.exists(os.path.join(directory, d))}
    for name in sorted(present):
        src = os.path.join(directory, name)
        text = open(src, encoding="utf-8").read()
        body = markdown.markdown(
            text, extensions=["extra", "sane_lists", "toc"], output_format="html5")
        # A link to a sibling guide should land on the guide's PAGE, not on its source. Only the
        # ones actually rendered here are rewritten - a link to a markdown file that stays markdown
        # must keep pointing at the file that exists.
        for other in present:
            body = body.replace(f'href="{other}"', f'href="{other[:-3]}.html"')
        title = next((re.sub(r"<[^>]+>", "", m) for m in re.findall(r"<h1[^>]*>(.*?)</h1>", body)),
                     name[:-3].replace("_", " ").title())
        out = os.path.join(directory, name[:-3] + ".html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        depth = name.count("/")
        open(out, "w", encoding="utf-8").write(
            PAGE.replace("__TITLE__", html.escape(title)).replace("__BODY__", body)
                .replace("__ROOT__", "../" * depth))
        made.append(os.path.relpath(out, directory))
    return made


if __name__ == "__main__":
    d = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    for f in convert(d):
        print(f"  rendered {f}")
