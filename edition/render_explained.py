#!/usr/bin/env python3
"""Render almanac.explained.html from dist_src/explained_src.html.

WHY A GENERATOR EXISTS FOR THIS PAGE (2026-08-29): the explained page was the last hand-written
face in the edition — everything else is generated precisely so the presentation cannot drift
from the edition it presents. When the Overseer asked for properly typeset mathematics, the page
got a template and this renderer at the same time, so it now has a regeneration path like the rest.

THE MATHEMATICS IS AUTHORED AS TeX IN THE TEMPLATE — \\( .. \\) inline, \\[ .. \\] display —
QUOTED from the informal proof of record, never retyped from a rendered view (transcription is
where this pilot's errors entered):

    ../../informal/proofv0a.tex
    sha256 bbd6f055bd5aff614d1a6575b24949d8fd2b805ebda20e33e5c706f28713bbae  (at authoring)

with the proof's own macros expanded: \\At = A_t, \\Ft = F_t, \\Nev = \\mathcal N^{ev},
\\Yc = \\check Y. One deliberate divergence class: instantiations the proof itself licenses
(e.g. nu_1 = (X-1)/(q-1) is the r=1 case of the quoted definition) and the page's worked table
values, which were CAS-checked against the definition when the page was written and re-derived
by hand at templating.

THE TeX IS PRE-RENDERED TO MathML AT BUILD TIME (latex2mathml — a BUILD-time dependency only;
the reader needs nothing). The output keeps the renderer-family promise LITERALLY: no external
CSS, JS, fonts or images, and no JavaScript at all — MathML is markup and the browser's own
engine typesets it. A CDN MathJax/KaTeX would have put a network service behind an artifact
whose whole claim is that it needs none.
"""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render_docs import WARRANT_VARS, wordmark  # one mark, defined once

HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(HERE, "almanac.explained.html")

# THE TEMPLATE LIVES IN THIS FILE, like render_almanac.py's and render_index.py's page skeletons —
# one source of truth that SHIPS with the almanac, so an unzipped copy can regenerate the page.
# A COMPLETE DOCUMENT, NOT A FRAGMENT. This page began at <title> — no doctype, no <html>,
# no <head>, and so NO CHARSET AND NO VIEWPORT. Two consequences, both found by serving the
# built almanac over the tailnet and looking at it on a phone (2026-09-03): a browser with no
# charset falls back to Latin-1 and every em dash arrives as \u00e2\u20ac\u201d, and with no
# viewport the page renders at desktop width on a handset. index.html and almanac.html always
# had these; these two never did.
TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Multiplicative Grid</title>
<style>
:root{
  --paper:#f4f6f7; --panel:#e8edef; --ink:#131a1e; --dim:#4e5b63; --faint:#7b878e;
  --rule:#c9d4d9; --hair:#dde5e8;
  --struct:#2f4a6b; --kern:#1f5f5b; --comp:#7a5a18; --caution:#8c3a2e;
  --measure:66ch;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --paper:#0e1215; --panel:#171d21; --ink:#e7ecef; --dim:#a3aeb4; --faint:#77838a;
  --rule:#283138; --hair:#1e262b;
  --struct:#8fb2d6; --kern:#74bcb4; --comp:#cba765; --caution:#e2968a;
}}
:root[data-theme="dark"]{
  --paper:#0e1215; --panel:#171d21; --ink:#e7ecef; --dim:#a3aeb4; --faint:#77838a;
  --rule:#283138; --hair:#1e262b;
  --struct:#8fb2d6; --kern:#74bcb4; --comp:#cba765; --caution:#e2968a;
}
*{box-sizing:border-box}
body{
  margin:0; background:var(--paper); color:var(--ink);
  font:400 18px/1.72 "Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;
  -webkit-font-smoothing:antialiased;
  padding-inline:clamp(1.1rem,5vw,2rem);
}
.wrap{max-width:var(--measure); margin-inline:auto; padding-block:clamp(3rem,9vw,6rem) 6rem}
p,li,dd,dt{max-width:var(--measure)}
p{margin:0 0 1.15rem; text-wrap:pretty}

.eyebrow{font-family:ui-sans-serif,-apple-system,"Segoe UI",system-ui,sans-serif;
  font-size:.68rem; font-weight:650; letter-spacing:.19em; text-transform:uppercase;
  color:var(--faint); margin:0 0 1.1rem}
h1{font-size:clamp(2.4rem,8vw,3.6rem); line-height:1.02; letter-spacing:-.028em;
  font-weight:600; margin:0 0 1.3rem; text-wrap:balance}
h2{font-size:1.5rem; line-height:1.2; letter-spacing:-.014em; font-weight:600;
  margin:4.2rem 0 1.2rem; text-wrap:balance}
h2::before{content:""; display:block; width:2.4rem; height:2px;
  background:var(--ink); margin-bottom:1.1rem}
h3{font-size:1.06rem; font-weight:650; margin:2.4rem 0 .5rem; letter-spacing:-.004em}
.lede{font-size:1.24rem; line-height:1.55; color:var(--dim); margin-bottom:2rem}
strong{font-weight:650}
code,.mono{font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace; font-size:.86em;
  font-variant-ligatures:none}
code{background:var(--panel); padding:.08em .32em; border-radius:2px}
a{color:var(--struct); text-underline-offset:3px}
a:focus-visible{outline:2px solid var(--struct); outline-offset:3px; border-radius:2px}

/* full-width figure bands */
.band{margin:2.4rem calc(50% - 50vw); padding:2.2rem calc(50vw - 50%);
  background:var(--panel); border-block:1px solid var(--hair)}
.band > *{max-width:var(--measure); margin-inline:auto}
.cap{font-family:ui-sans-serif,-apple-system,system-ui,sans-serif; font-size:.78rem;
  line-height:1.5; color:var(--dim); margin:1.1rem auto 0}

.display{font-family:ui-monospace,"SF Mono",Menlo,Consolas,monospace;
  font-size:1.02rem; line-height:1.9; margin:1.6rem 0; padding:1.2rem 0;
  border-block:1px solid var(--rule); text-align:center; overflow-x:auto}
.display .big{font-size:1.18rem}

/* the grid figure */
.gridfig{overflow-x:auto; padding-bottom:.4rem}
.grid{border-collapse:collapse; margin:0 auto; font-variant-numeric:tabular-nums}
.grid th,.grid td{padding:.55rem .85rem; text-align:center; white-space:nowrap;
  font-family:ui-monospace,Menlo,monospace; font-size:.86rem}
.grid th{font-family:ui-sans-serif,system-ui,sans-serif; font-size:.66rem;
  letter-spacing:.13em; text-transform:uppercase; color:var(--faint); font-weight:650;
  border-bottom:1px solid var(--rule); padding-bottom:.5rem}
.grid td.node{color:var(--struct); font-weight:600}
.grid td.val{color:var(--ink)}
.grid tr.off td{color:var(--caution)}
.grid tr.off td.node{color:var(--caution); font-weight:600}
.grid .tag{font-family:ui-sans-serif,system-ui,sans-serif; font-size:.62rem;
  letter-spacing:.12em; text-transform:uppercase; color:var(--faint)}

/* witnesses */
.wit{border-left:2px solid var(--rule); padding:.1rem 0 .1rem 1.3rem; margin:1.8rem 0}
.wit .edge{font-family:ui-sans-serif,-apple-system,system-ui,sans-serif;
  font-size:.7rem; font-weight:650; letter-spacing:.13em; text-transform:uppercase;
  color:var(--caution); display:block; margin-bottom:.45rem}
.wit p:last-child{margin-bottom:0}

/* grade chips */
.grades{display:grid; gap:0; margin:1.6rem 0}
.grade{display:grid; grid-template-columns:5.2rem 1fr; gap:.2rem 1.3rem; align-items:baseline;
  padding:1rem 0; border-top:1px solid var(--hair)}
.grade:last-child{border-bottom:1px solid var(--hair)}
.grade .n{font-family:ui-monospace,Menlo,monospace; font-size:1.5rem; font-weight:600;
  font-variant-numeric:tabular-nums; line-height:1}
.grade .nm{font-family:ui-sans-serif,-apple-system,system-ui,sans-serif; font-size:.7rem;
  font-weight:700; letter-spacing:.12em; text-transform:uppercase}
.grade .wh{grid-column:2; font-size:.95rem; color:var(--dim)}
.g-k .n,.g-k .nm{color:var(--kern)} .g-c .n,.g-c .nm{color:var(--comp)}
.g-n .n,.g-n .nm{color:var(--faint)}
@media(max-width:520px){.grade{grid-template-columns:1fr} .grade .wh{grid-column:1}}

/* descent steps */
.steps{list-style:none; margin:1.6rem 0; padding:0; display:grid; gap:1.9rem}
.steps li{display:grid; grid-template-columns:5.6rem 1fr; gap:0 1.4rem; max-width:none}
.steps .yr{font-family:ui-sans-serif,-apple-system,system-ui,sans-serif; font-size:.72rem;
  font-weight:700; letter-spacing:.1em; color:var(--faint); padding-top:.35rem;
  font-variant-numeric:tabular-nums}
.steps .bd{max-width:var(--measure)}
.steps h3{margin-top:0}
@media(max-width:560px){.steps li{grid-template-columns:1fr; gap:.3rem}}

dl.defs{display:grid; grid-template-columns:auto 1fr; gap:.6rem 1.4rem; margin:1.5rem 0;
  align-items:baseline}
dl.defs dt{font-family:ui-monospace,Menlo,monospace; font-size:.88rem; color:var(--struct);
  white-space:nowrap}
dl.defs dd{margin:0; color:var(--dim); font-size:.97rem}
@media(max-width:520px){dl.defs{grid-template-columns:1fr; gap:.15rem}
  dl.defs dt{margin-top:.7rem}}

math{font-size:1.05em}
.display math[display="block"]{font-size:1.25rem; margin:.15rem 0}
.note{font-size:.95rem; color:var(--dim)}
.colophon{margin-top:5rem; padding-top:1.4rem; border-top:2px solid var(--ink);
  font-size:.86rem; line-height:1.6; color:var(--dim)}
.colophon p{max-width:none}

/* THE MARK, on every html face of the almanac (Overseer, 2026-09-04). Horizontal cut here,
   because it sits in a masthead and the square cut is for a margin beside prose. */
.wordmark{display:block;margin:0 0 .7rem;height:38px;width:126px}
__WARRANT_VARS__
</style>

<div class="wrap">

__WORDMARK__
<p class="eyebrow">Project Sandbox · almanacA0a · a reader's companion</p>
<h1>The multiplicative&nbsp;grid</h1>

<p class="lede">A polynomial can take whole-number values everywhere you look and still not have
whole-number coefficients. This is the story of one small theorem that says exactly which
polynomials do that on a geometric grid — and of how far that theorem has been checked.</p>

<p>The result below was proved, machine-verified, and then edited into a form a stranger can
check. It is a small, easy theorem, and the page says so plainly further down. What is unusual is
that every claim on it carries a record of what warrants it.</p>

<h2>The oldest version of the question</h2>

<p>Take the polynomial \(x(x-1)/2\). Its coefficients are halves — not whole numbers —
yet at every integer it returns an integer: 0, 0, 1, 3, 6, 10. The halving always cancels,
because among any two consecutive integers one is even.</p>

<p>So "has integer coefficients" and "takes integer values" are different properties, and the
second is strictly weaker. <strong>Pólya's theorem</strong> (1915) says exactly how much weaker:
the polynomials taking integer values at every integer are precisely the integer combinations of
the binomial polynomials \(\binom{x}{k}\). The failure of integrality in the coefficients
is entirely accounted for by changing basis. Everything below is a deformation of that sentence.</p>

<h2>What this record proves</h2>

<p>Replace the grid. Instead of asking for integrality at <code>0, 1, 2, 3, …</code>, ask for it
along a <strong>geometric</strong> progression — at \(1,\,q,\,q^2,\,q^3,\,\dots\), and in both
directions, at negative powers too. Replace the coefficients as well: they are no longer numbers
but expressions in two independent variables.</p>

<div class="display">\[\mathcal N^{\mathrm{ev}}\;=\;\sum_{u\in\mathbb Z}\,\sum_{r\ge 0} A_t\,\check Y^{\,u}\,\nu_r(\check Y)\]</div>

<p>In words: <strong>the Laurent polynomials taking values in \(A_t\) at every point of
the multiplicative grid are exactly the \(A_t\)-span of the divided classes.</strong>
Same shape as Pólya, one deformation further out.</p>

<h3>Reading the symbols</h3>

<dl class="defs">
  <dt>\(v,\ t\)</dt><dd>two independent variables, and \(q=v^2\). The variable \(t\)
    is a free parameter that rides through the whole argument without ever being constrained.</dd>
  <dt>\(A_t=\mathbb Z[v^{\pm1},t^{\pm1}]\)</dt><dd>the coefficients we want values to land in —
    whole-number combinations of powers of \(v\) and \(t\), positive or negative.</dd>
  <dt>\(F_t=\mathbb Q(v)[t^{\pm1}]\)</dt><dd>the larger ring the polynomials are actually written in.
    Fractions are allowed here. This gap is the whole theorem.</dd>
  <dt>\(\check Y\)</dt><dd>the grid coordinate. The grid is the set of points \(\check Y=q^{\chi}\)
    for every whole number \(\chi\), positive and negative.</dd>
  <dt>\(\nu_r\)</dt><dd>the <em>divided classes</em>: \(\nu_0=1\), and
    \(\nu_r(X)=\prod_{s=0}^{r-1}\frac{X-q^s}{q^r-q^s}\).
    These play the part the binomial polynomials play in Pólya's theorem.</dd>
  <dt>\(\mathcal N^{\mathrm{ev}}\)</dt><dd>the even Newton lattice — everything grid-integral.</dd>
</dl>

<h2>Where the difficulty lives</h2>

<p><strong>The polynomials have coefficients in \(F_t\); what is required to lie in
\(A_t\) are their values.</strong> If the coefficients were already in \(A_t\)
there would be nothing to prove — the values would follow for free. The content is that a
polynomial can fail the coefficient test and pass the value test, and that the divided classes
account for every way this can happen.</p>

<p>One element shows the gap is real. Take the first divided class:</p>

<div class="display">\[\nu_1(\check Y)=\frac{\check Y-1}{q-1}\]</div>

<p>Its single coefficient is \(1/(q-1)\), which is not in \(A_t\) —
\(q-1\) is not invertible there. But watch what it does on the grid:</p>

<div class="band">
  <div class="gridfig">
    <table class="grid">
      <thead>
        <tr><th>node <span class="tag">\(\check Y=q^{\chi}\)</span></th><th>\(\nu_1\) evaluated there</th><th></th></tr>
      </thead>
      <tbody>
        <tr><td class="node">\(q^{-2}\)</td><td class="val">\(-q^{-1}-q^{-2}\)</td><td class="tag">integral</td></tr>
        <tr><td class="node">\(q^{-1}\)</td><td class="val">\(-q^{-1}\)</td><td class="tag">integral</td></tr>
        <tr><td class="node">\(q^{0}\)</td><td class="val">\(0\)</td><td class="tag">integral</td></tr>
        <tr><td class="node">\(q^{1}\)</td><td class="val">\(1\)</td><td class="tag">integral</td></tr>
        <tr><td class="node">\(q^{2}\)</td><td class="val">\(1+q\)</td><td class="tag">integral</td></tr>
        <tr><td class="node">\(q^{3}\)</td><td class="val">\(1+q+q^2\)</td><td class="tag">integral</td></tr>
        <tr class="off"><td class="node">\(v^{3}\)</td><td class="val">\(\frac{v^2+v+1}{v+1}\)</td><td class="tag">off the grid — not integral</td></tr>
      </tbody>
    </table>
  </div>
  <p class="cap">The first six rows are the grid. The fraction always cancels, in both directions —
  which is why \(\nu_1\) belongs to \(\mathcal N^{\mathrm{ev}}\) despite its coefficient. The
  last row is not a grid point, and there the cancellation fails; that row is the subject of the
  third witness below. All seven values were recomputed on the project's computer-algebra oracle
  while this page was written.</p>
</div>

<h2>Three ways the statement is tight</h2>

<p>Every clause in the statement is doing work, and one value each shows it. These are the sharp
edges of the result: what it delivers, what it stops short of, and the hypothesis it cannot do
without.</p>

<div class="wit">
  <span class="edge">The divided classes are genuinely needed</span>
  <p><strong>\(\nu_1\) is grid-integral and its coefficient is not integral.</strong> It lies
  in \(\mathcal N^{\mathrm{ev}}\) — the table above shows it landing in \(A_t\) at every
  node — while its single coefficient \((q-1)^{-1}\) lies outside
  \(A_t\). So \(\mathcal N^{\mathrm{ev}}\) is <em>strictly</em> larger than
  \(A_t[\check Y^{\pm1}]\), and the theorem says something the coefficients alone do
  not.</p>
</div>

<div class="wit">
  <span class="edge">It spans, and stops there</span>
  <p><strong>The generating family satisfies a relation:
  \((q-1)\,\nu_1(\check Y)-\check Y+1=0\) over \(A_t\).</strong> So the divided classes
  span \(\mathcal N^{\mathrm{ev}}\) without being independent, and this is a <em>spanning</em>
  theorem — a basis theorem would be a stronger result and is not this one. Whether
  \(\mathcal N^{\mathrm{ev}}\) is free over \(A_t\) on some other family is
  <strong>open</strong>.</p>
</div>

<div class="wit">
  <span class="edge">The grid must be even</span>
  <p><strong>At the odd node \(v^{3}\) the value leaves \(A_t\):</strong>
  \(\nu_1(v^3)=\frac{v^3-1}{v^2-1}=\frac{v^2+v+1}{v+1}\). Since \(q=v^2\), the grid is the
  <em>even</em> powers \(v^{2\chi}\), and \(\nu_1\) is integral at every one of
  them — but refine the grid to all powers of \(v\) and integrality breaks at the first
  new node. <strong>The word <em>even</em> in the statement is a hypothesis, not a
  convenience.</strong></p>
</div>

<p class="note">Each of these is settled by a single value, which is worth saying plainly: one
value is a complete proof of a statement of this shape, not evidence for it. Nothing here rests on
a sample.</p>

<h2>Where the statement came from</h2>

<p>Every mathematical statement here is a known result, reached along a line worth setting
out, because each step changed what the question was about.</p>

<ol class="steps">
  <li><span class="yr">1915</span><div class="bd">
    <h3>Pólya — the additive origin</h3>
    <p>Integer-valued polynomials on the integers are the \(\mathbb Z\)-span of the binomial
    polynomials. The template for everything that follows.</p>
  </div></li>
  <li><span class="yr">1933 · 1990</span><div class="bd">
    <h3>Gel'fond, then Gramain — moving the grid</h3>
    <p>Ask for integrality along \(1,\,q,\,q^2,\,\dots\) instead. For entire functions that is
    Gel'fond, 1933 — the <em>multiplicative analogue</em> of Pólya's problem. For polynomials it is
    Gramain's Proposition 2.2: for an integer \(q\ge 2\), the polynomials integral at every
    \(q^{k}\) are generated by the Gauss binomial polynomials — <strong>which are
    exactly the divided classes of this record.</strong></p>
  </div></li>
  <li><span class="yr">2016</span><div class="bd">
    <h3>Harman and Hopkins — deforming the coefficients</h3>
    <p>Which \(P\in\mathbb Q(q)[x]\) satisfy \(P([n]_q)\in\mathbb Z[q]\)? Their §1 answers it on
    the additive grid of \(q\)-integers; their §4 takes the nodes over all of
    \(\mathbb Z\), which is the <strong>bilateral</strong> form this record needs. Their §4 also
    contains the remark that joins the two lines: setting \(z=1+(q-1)x\) turns
    evaluation at \(x=[n]_q\) into evaluation at \(z=q^{n}\) — the
    additive grid becomes the geometric one, node for node.</p>
  </div></li>
  <li><span class="yr">this record</span><div class="bd">
    <h3>What is added — two routine transports</h3>
    <p>The grid variable is inverted, so the objects are <strong>Laurent</strong> rather than
    polynomial; at a grid of units that is a clearing argument, not a difficulty. And the
    coefficients carry a <strong>free parameter \(t\)</strong>, which arrives from the
    setting the goal was posed in and rides through as a spectator — the integrality test
    decomposes coefficient-wise. No predecessor is located for that parameter, and three
    independent sources record its absence.</p>
  </div></li>
</ol>

<h2>How far it has been checked</h2>

<p>The record exists in three layers — a written proof, a Julia instrument that computes the
objects, and a Lean development the proof kernel accepts. <strong>The grades below are different
kinds of claim, each meaning exactly what it states</strong>, and the edition keeps them
distinct.</p>

__GRADES__

<p class="note">The computed rows are the instrument (acceptance battery 87/87, with the grid
integrality checked for \(r\) in \(0\dots 8\) against \(\chi\) in \(-9\dots 9\), and a negative
control of 249 cases required to fail — which they do) and an independent oracle referee pin
(verdict <code>PROVED_BOUNDED</code>, 60 positive and 5 hostile seeds, 0 disagreements).</p>

<p><strong>The deliverable is the theorem with a clean axiom base.</strong>
No theory of integer-valued polynomials, classical or \(q\)-deformed, exists in Mathlib —
not Pólya's theorem, not a \(q\)-analogue. That absence is why the formal layer had to be
built rather than cited.</p>

<h2>The honest size of the result</h2>

<p><strong>At \(GL_1\) this is the degenerate case, and the edition says so first.</strong>
The root system is empty, so the algebra is commutative and its centre is all of it; the Weyl group
is trivial; the Harish–Chandra projection is the identity map. Two of the three clauses in the
original goal are formalities at this rank. <strong>The value of the record
is that a small true statement was carried end to end</strong>, and that the cost and the failure
modes of doing so were measured. Rank 2 and above are open, and nothing here settles
them.</p>

<p><strong>A tested agreement is not a proof.</strong> The Julia and Lean layers are two independent
implementations joined by a shared naming discipline, not by a checked morphism. Agreement between
them is established by testing, over the bounds printed above, and it licenses nothing beyond them.</p>

<p><strong>The ancestral result is not our result.</strong> The Harman–Hopkins bilateral quantum
Pólya theorem is the ancestor of the transported argument. The reconciliation that would identify
their lattice with this one is <strong>open</strong>.</p>

<h2>What is still open</h2>

<p>Three things, stated because an edition that lists only its results teaches a false boundary:
whether \(\mathcal N^{\mathrm{ev}}\) is <strong>free</strong> over \(A_t\) on some family
other than the dependent one above; the <strong>four-way lattice reconciliation</strong> with the
Harman–Hopkins statement; and the <strong>rank ≥ 2 cases</strong>, where the two clauses that are
formalities here carry real weight and the argument does not obviously transport.</p>

<div class="colophon">
  <p><strong>This page is a companion: it explains, and the record certifies.</strong> The
  record-bearing edition — one row per result, joining all three layers under a stated convention
  frame, with per-row ancestry and a manifest of every shipped file and its hash — is a separate
  document, and where the two ever disagree the record is right and this page is wrong.</p>
  <p>Every mathematical statement here is drawn from that edition's register. The seven grid values
  and the two identities in the witnesses were recomputed fresh on the project's warm
  computer-algebra oracle while this page was written.</p>
  <p>almanacA0a · pilot edition over the closed record <code>SandboxA/sandboxA0a</code> ·
  assembled by the Almanac Editor.</p>
</div>

</div>
"""

try:
    import latex2mathml.converter as l2m
except ImportError:
    sys.exit("latex2mathml is required at BUILD time only:  pip3 install --user latex2mathml")

s = TEMPLATE
counts = {"inline": 0, "display": 0}

def sub(kind, pattern, display):
    def repl(m):
        counts[kind] += 1
        try:
            return l2m.convert(m.group(1), display=display)
        except Exception as e:
            sys.exit(f"TeX failed to convert ({e}): {m.group(1)!r}")
    return pattern, repl

pat, repl = sub("display", re.compile(r"\\\[(.+?)\\\]", re.S), "block")
s = pat.sub(repl, s)
pat, repl = sub("inline", re.compile(r"\\\((.+?)\\\)", re.S), "inline")
s = pat.sub(repl, s)

# fail loudly rather than ship a half-rendered page
for leftover in (r"\\(", r"\\["):
    if leftover in s:
        sys.exit(f"unconverted TeX delimiter {leftover!r} left in output")
# THE GRADES ARE COUNTED, NOT TYPED, AND THEY RUN INK -> ORANGE -> BLUE.
# They were typed as 9/11, 2/11 and 0/11 with an em-dash where ink's description belongs, and had
# been wrong since 2026-08-31, when the twelfth row - the ink one - was added. The Overseer found it
# on the published page: "does not have ink certified statement (only 11 statements are mentioned)".
# FOURTH typed count in this edition to go stale; every other one is a measurement now, and so is
# this. The order is the standing one, ink -> orange -> blue, which this page had backwards too.
import json as _json
_con = _json.load(open(os.path.join(HERE, "CONCORDANCE.json"), encoding="utf-8"))
_w = [r.get("warrant") for r in _con["rows"]]
GRADES = """<div class="grades">
  <div class="grade g-n">
    <div class="n">{ink}<span class="nm" style="font-size:.62rem"> / {tot}</span></div>
    <div class="nm">ink \u2014 a refereed argument</div>
    <div class="wh">An argument written for a human reader and refereed. No kernel certifies it and
      no computation bounds it: the check is a referee reading the proof. The one here is the claim
      every other result rests on \u2014 that the proof proves the statement that was signed.</div>
  </div>
  <div class="grade g-c">
    <div class="n">{orange}<span class="nm" style="font-size:.62rem"> / {tot}</span></div>
    <div class="nm">orange \u2014 computed over a declared range</div>
    <div class="wh">Verified by computation over a stated bound, and over nothing else. The bound
      is part of the claim. Neither of these could ever be kernel-certified: no Lean declaration
      states what a Julia program does.</div>
  </div>
  <div class="grade g-k">
    <div class="n">{blue}<span class="nm" style="font-size:.62rem"> / {tot}</span></div>
    <div class="nm">blue \u2014 kernel-certified</div>
    <div class="wh">A Lean declaration states the claim and its axiom base is exactly
      <code>propext</code>, <code>Classical.choice</code>, <code>Quot.sound</code> \u2014 no
      <code>sorryAx</code>, no custom axiom. Every one of these was measured first-hand
      through the Lean language server.</div>
  </div>
</div>""".format(ink=_w.count("ink"), orange=_w.count("orange"),
                 blue=_w.count("blue"), tot=len(_w))

# The mark goes in BEFORE the no-network check, so the check reads the bytes that ship.
s = s.replace("__WORDMARK__", wordmark()).replace("__WARRANT_VARS__", WARRANT_VARS)
s = s.replace("__GRADES__", GRADES)
if re.search(r"__[A-Z][A-Z0-9_]*__", s):
    sys.exit("render_explained: a placeholder survived into the page")

# The MathML xmlns URI is an identifier, never fetched. A NETWORK reference is something a tag
# would load: script/src/href. Check those.
if re.search(r"<script\b", s) or re.search(r"""\b(?:src|href)\s*=\s*["']https?://""", s):
    sys.exit("output gained a script tag or a network reference — refusing to write")

open(OUT, "w", encoding="utf-8").write(s)
print(f"wrote {os.path.relpath(OUT, HERE)} ({len(s):,} bytes) — "
      f"{counts['display']} display + {counts['inline']} inline TeX runs -> MathML, "
      f"no scripts, no network references")
