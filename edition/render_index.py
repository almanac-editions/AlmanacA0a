#!/usr/bin/env python3
"""Render index.html — the interactive, offline reader view of the almanac.

DATA IS EMBEDDED, NOT FETCHED. A browser opening a file:// page cannot fetch() a sibling JSON
file (CORS), so a page that loaded its data at runtime would be blank for exactly the least
technical reader — the one this view exists for. Re-run this after changing CONCORDANCE.json.

COLOUR: the two category colours are slots 1 and 2 of the reference categorical palette, used
UNCHANGED (light #2a78d6/#eb6834, dark #3987e5/#d95926); that palette documents its own
adjacent-pair CVD validation. The local validator (node) is NOT installed on this machine, so it
was NOT re-run here — recorded rather than reported as a pass. Every colour is paired with a text
label, so identity never rests on colour alone.
"""
import html, json, os

ED = os.path.dirname(os.path.abspath(__file__))
con = json.load(open(os.path.join(ED, "CONCORDANCE.json")))
man = json.load(open(os.path.join(ED, "MANIFEST.json")))

rows = con["rows"]
n_kernel = sum(1 for r in rows if r["warrant"] == "blue")
n_ink = sum(1 for r in rows if r["warrant"] == "ink")
n_range = sum(1 for r in rows if r["warrant"] == "orange")

DATA = json.dumps({
    "rows": rows,
    "warrantHelp": con["how_to_read_the_warrant_field"],
    "edition": con["edition"],
}, ensure_ascii=False)

TPL = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<style>
  :root {
    color-scheme: light;
    --surface-0:#f6f5f2; --surface-1:#fcfcfb; --surface-2:#efeee9;
    --text-primary:#0b0b0b; --text-secondary:#52514e; --text-muted:#78766f;
    --border:#dedcd5; --border-strong:#c4c2b9;
    --cat-1:#2a78d6; --cat-2:#eb6834;
    --cat-1-soft:#e6effc; --cat-2-soft:#fdeee7;
  }
  :root[data-theme="dark"], :root:not([data-theme="light"]) {
    /* dark values applied below via media query + explicit stamp */
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      color-scheme: dark;
      --surface-0:#131312; --surface-1:#1a1a19; --surface-2:#232322;
      --text-primary:#ffffff; --text-secondary:#c3c2b7; --text-muted:#93918a;
      --border:#333331; --border-strong:#4a4a46;
      --cat-1:#3987e5; --cat-2:#d95926;
      --cat-1-soft:#16273d; --cat-2-soft:#33190f;
    }
  }
  :root[data-theme="dark"] {
    color-scheme: dark;
    --surface-0:#131312; --surface-1:#1a1a19; --surface-2:#232322;
    --text-primary:#ffffff; --text-secondary:#c3c2b7; --text-muted:#93918a;
    --border:#333331; --border-strong:#4a4a46;
    --cat-1:#3987e5; --cat-2:#d95926;
    --cat-1-soft:#16273d; --cat-2-soft:#33190f;
  }
  * { box-sizing:border-box; }
  body {
    margin:0; background:var(--surface-0); color:var(--text-primary);
    font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  }
  .wrap { max-width:1080px; margin:0 auto; padding:0 20px 80px; }
  header { border-bottom:1px solid var(--border); background:var(--surface-1); }
  .hdr { max-width:1080px; margin:0 auto; padding:22px 20px; display:flex; gap:16px;
         align-items:flex-start; justify-content:space-between; }
  h1 { font-size:22px; margin:0 0 4px; letter-spacing:-.01em; }
  .sub { color:var(--text-secondary); font-size:14px; margin:0; }
  button { font:inherit; cursor:pointer; }
  .toggle { background:var(--surface-2); color:var(--text-primary); border:1px solid var(--border-strong);
            border-radius:8px; padding:7px 12px; font-size:13px; white-space:nowrap; }
  .toggle:hover { border-color:var(--text-muted); }
  .hdr-right { display:flex; align-items:center; gap:16px; }
  @media (max-width:640px){ .hdr-right .logo { display:none; } }

  section { margin-top:40px; }
  h2 { font-size:15px; text-transform:uppercase; letter-spacing:.07em; color:var(--text-secondary);
       margin:0 0 14px; font-weight:600; }
  p { color:var(--text-secondary); }
  .lead { color:var(--text-primary); font-size:17px; max-width:70ch; }

  .hero { display:flex; align-items:baseline; gap:14px; flex-wrap:wrap; margin:26px 0 6px; }
  .hero .fig { font-size:52px; font-weight:650; line-height:1; letter-spacing:-.02em; }
  .hero .cap { color:var(--text-secondary); font-size:15px; max-width:44ch; }

  .kpis { display:grid; grid-template-columns:repeat(auto-fit,minmax(158px,1fr)); gap:12px; margin-top:22px; }
  .kpi { background:var(--surface-1); border:1px solid var(--border); border-radius:10px; padding:14px 16px; }
  .kpi .l { font-size:12px; color:var(--text-muted); margin-bottom:6px; }
  .kpi .v { font-size:26px; font-weight:620; line-height:1.1; }
  .kpi .n { font-size:12px; color:var(--text-muted); margin-top:5px; }

  .previewline { margin:22px 0 0; color:var(--text-muted); font-size:13px; font-style:italic; }
  .previewline code { font-style:normal; }
  .note { background:var(--surface-1); border:1px solid var(--border); border-left:3px solid var(--cat-1);
          border-radius:0 10px 10px 0; padding:14px 18px; margin:18px 0; }
  .note p { margin:0; color:var(--text-secondary); font-size:14.5px; }
  .note strong { color:var(--text-primary); }

  .controls { display:flex; gap:8px; flex-wrap:wrap; align-items:center; margin-bottom:14px; }
  .chip { background:var(--surface-1); border:1px solid var(--border-strong); color:var(--text-secondary);
          border-radius:999px; padding:6px 13px; font-size:13px; }
  .chip[aria-pressed="true"] { background:var(--text-primary); color:var(--surface-1);
          border-color:var(--text-primary); }
  input[type=search] { flex:1; min-width:180px; font:inherit; font-size:14px; padding:7px 12px;
          border:1px solid var(--border-strong); border-radius:8px;
          background:var(--surface-1); color:var(--text-primary); }

  .row { background:var(--surface-1); border:1px solid var(--border); border-radius:10px;
         margin-bottom:9px; overflow:hidden; }
  .rowhead { width:100%; text-align:left; background:none; border:0; padding:14px 16px;
             display:flex; gap:13px; align-items:flex-start; color:inherit; }
  .rowhead:hover { background:var(--surface-2); }
  .badge { flex:none; font-size:11px; font-weight:640; padding:3px 8px; border-radius:5px;
           letter-spacing:.02em; white-space:nowrap; margin-top:2px; }
  .b-kernel { background:var(--cat-1-soft); color:var(--cat-1); border:1px solid var(--cat-1); }
  .b-range  { background:var(--cat-2-soft); color:var(--cat-2); border:1px solid var(--cat-2); }
  /* A row carrying NO warrant must not wear a warrant's colour. Orange means a computation
     was checked; blue means a kernel checked a proof. Neutral means neither was done, and it
     has to look like neither. */
  /* INK is a warrant and wears the ink colour — the same colour as the mark's first 'a' and as
     the running text. It is not a lesser blue or a paler orange: the three are KINDS, not levels. */
  .b-ink    { background:var(--surface-2); color:var(--text-primary); border:1px solid var(--text-primary); }
  /* the neutral badge is now ONLY the fallback for a value this page does not know. */
  .b-none   { background:var(--surface-2); color:var(--text-secondary); border:1px solid var(--border-strong); }
  .rowtitle { flex:1; }
  .rowtitle .s { font-size:15px; color:var(--text-primary); }
  .rowtitle .i { font-size:12px; color:var(--text-muted); font-family:ui-monospace,SFMono-Regular,Menlo,monospace; margin-top:3px; }
  .caret { flex:none; color:var(--text-muted); font-size:13px; margin-top:3px; }
  .detail { display:none; padding:4px 16px 18px; border-top:1px solid var(--border); }
  .row.open .detail { display:block; }
  .row.open .caret { transform:rotate(90deg); }
  .caret { display:inline-block; transition:transform .12s; }
  dl { margin:0; display:grid; grid-template-columns:minmax(120px,168px) 1fr; gap:9px 18px; font-size:14px; }
  dt { color:var(--text-muted); font-size:12.5px; padding-top:2px; }
  dd { margin:0; color:var(--text-secondary); }
  code, .mono { font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:12.5px;
                background:var(--surface-2); padding:1.5px 5px; border-radius:4px; color:var(--text-primary); }
  .axioms code { margin-right:5px; display:inline-block; }
  .empty { color:var(--text-muted); font-size:14px; padding:22px; text-align:center; }
  ul.plain { padding-left:19px; color:var(--text-secondary); font-size:14.5px; }
  ul.plain li { margin-bottom:7px; }
  footer { margin-top:56px; padding-top:20px; border-top:1px solid var(--border);
           color:var(--text-muted); font-size:12.5px; }
  a { color:var(--cat-1); }
  @media (max-width:640px){ dl{grid-template-columns:1fr;gap:3px 0;} dt{margin-top:8px;} .hero .fig{font-size:42px;} }
</style></head><body>
<header><div class="hdr">
  <div><h1>__TITLE__</h1><p class="sub">__SUB__</p></div>
  <div class="hdr-right">
    <!-- the ALMANAC family mark (W1, adopted 2026-08-29): the word's three a's are the three
         kinds of warrant - informal (ink), computational (orange), kernel-certified (blue). Inline and
         var()-coloured so it follows the theme toggle; no asset is fetched. -->
    <svg class="logo" width="132" height="40" viewBox="0 0 190 58" role="img" aria-label="almanac"><text x="5" y="43" font-family="Georgia, 'Iowan Old Style', 'Times New Roman', serif" font-size="44" fill="var(--text-primary)" textLength="180" lengthAdjust="spacingAndGlyphs">alm<tspan fill="var(--cat-2)">a</tspan>n<tspan fill="var(--cat-1)">a</tspan>c</text></svg>
    <button class="toggle" id="tt">Light / dark</button>
  </div>
</div></header>

<div class="wrap">
<!--BUILD_CLASS_BANNER-->

<p class="lead" style="margin-top:30px">This is a complete record of one small mathematical result
in three layers &mdash; an informal proof, a computer program, and a machine-checked formal proof
&mdash; together with a per-claim account of <strong>what actually warrants each one</strong>.</p>

<div class="hero">
  <div class="fig">__NKERNEL__ of __NTOTAL__</div>
  <div class="cap">results carry a proof-kernel certificate. Of the rest, __NRANGE__ are verified by
  computation over a stated range and __NINK__ by a refereed written argument &mdash; three different
  kinds of check, kept visibly different.</div>
</div>

<div class="kpis">
  <div class="kpi"><div class="l">Results recorded</div><div class="v">__NTOTAL__</div>
    <div class="n">one row each, joined across three layers</div></div>
  <div class="kpi"><div class="l">Refereed argument</div><div class="v">__NINK__</div>
    <div class="n">read adversarially, recorded per row</div></div>
  <div class="kpi"><div class="l">Computed over a range</div><div class="v">__NRANGE__</div>
    <div class="n">the bound is part of the claim</div></div>
  <div class="kpi"><div class="l">Kernel-certified</div><div class="v">__NKERNEL__</div>
    <div class="n">axioms measured, no gaps admitted</div></div>
  <div class="kpi"><div class="l">Peer review to date</div><div class="v">Internal</div>
    <div class="n">external refereeing is a step still ahead</div></div>
  <div class="kpi"><div class="l">Human minutes</div><div class="v">__HUMANMIN__</div>
    <div class="n">in the assembly itself</div></div>
  <div class="kpi"><div class="l">Machine minutes</div><div class="v">__WALLMIN__</div>
    <div class="n">wall clock, one session</div></div>
</div>

<div class="note"><p><strong>Three kinds of check.</strong> A proof kernel checking a proof, a program
checking ten thousand cases, and a referee reading an argument are not the same evidence, and
this almanac never lets them blur into &ldquo;we showed&rdquo;. Every result below states which one it has &mdash; and a
kernel certifies <em>the formal statement</em>. Whether that statement is faithful to the informal
one can be decided from the warrants and the convention frame carried on every row.</p></div>

<section>
  <h2>The results</h2>
  <div class="controls">
    <button class="chip" data-f="all" aria-pressed="true">All __NTOTAL__</button>
    <button class="chip" data-f="ink" aria-pressed="false">Ink __NINK__</button>
    <button class="chip" data-f="orange" aria-pressed="false">Orange __NRANGE__</button>
    <button class="chip" data-f="blue" aria-pressed="false">Blue __NKERNEL__</button>
    <input type="search" id="q" placeholder="Search statements, declarations, sources&hellip;" aria-label="Search results">
  </div>
  <div id="list"></div>
</section>

<section>

<section>
  <h2>Going further</h2>
  <ul class="plain">
    <li><a href="almanac.explained.html">The mathematics explained</a> &mdash; at length, for a
      general reader. Formulas typeset; no renderer, no network.</li>
    <li><a href="formal.html">The formal layer</a> &mdash; what the proof kernel actually certified,
      row by row, with the axioms measured for each and the sources beside them.</li>
    <li><a href="source/informal/proofv0a.pdf">The informal proof</a> (PDF), which proves
      <a href="source/informal/goalv0a.pdf">the signed goal</a> (PDF) &mdash; and
      <a href="source/informal/REFEREE_REPORT_PROOFv0a.html">the referee&rsquo;s report on it</a>,
      which is what the one ink-warranted row rests on.</li>
    <li><a href="source/informal/proofv0a.ledger.cas_receipts.html">The proof ledger</a> &mdash;
      which computation backs which step, receipt by receipt. Not a Lean blueprint, and this edition
      has none: its formal layer is seven files, not a dependency graph.</li>
    <li><a href="almanac.html">The edition as one page</a>, the
      <a href="almanac.artifact.html">reader&rsquo;s edition</a>, and
      <a href="EDITION.html">the edition&rsquo;s own front matter</a>.</li>
    <li><a href="FOR_A_HUMAN.html">Checking any of it yourself</a> &mdash; including how to install
      every piece of software from scratch.</li>
  </ul>
</section>

<footer>
  __EDITION__<br>
  Generated by <code>render_index.py</code> from <code>CONCORDANCE.json</code> and
  the edition&rsquo;s own records. This page works fully offline: all its data is embedded at render time.
</footer>
</div>

<script>
const DATA = __DATA__;
const root = document.documentElement;
document.getElementById('tt').onclick = () => {
  const cur = root.getAttribute('data-theme')
    || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  root.setAttribute('data-theme', cur === 'dark' ? 'light' : 'dark');
};
const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c =>
  ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const LABEL = { ink:'Ink — refereed argument', orange:'Orange — computed over a range',
                blue:'Blue — kernel-certified' };
// The three warrants, each in its own colour: ink, orange, blue. 'neither' is gone — the
// Overseer ruled a refereed informal proof is a warrant and not the lack of one, so naming it
// for what it lacked understated the record. An UNKNOWN value still falls back to neutral,
// because a value this page does not know must not borrow a warrant's colour.
const CLS = { ink:'b-ink', orange:'b-range', blue:'b-kernel' };
let filter = 'all', query = '';

function detail(r){
  const d = [];
  const push = (k,v) => { if (v) d.push('<dt>'+esc(k)+'</dt><dd>'+v+'</dd>'); };
  push('What it says', esc(r.informal && r.informal.statement));
  push('Warrant', esc(DATA.warrantHelp[r.warrant] || r.warrant));
  if (r.axioms && r.axioms.length)
    push('Axioms measured', '<span class="axioms">' +
      r.axioms.map(a => '<code>'+esc(a)+'</code>').join('') + '</span>');
  if (r.lean && r.lean.declaration)
    push('Formal declaration', '<code>'+esc(r.lean.declaration)+'</code>' +
      (r.lean.file ? '<br><span class="mono" style="background:none;padding:0">'+esc(r.lean.file)+'</span>' : ''));
  if (r.informal && r.informal.file)
    push('In the manuscript', '<span class="mono" style="background:none;padding:0">' +
      esc(r.informal.file) + (r.informal.label ? ' &mdash; '+esc(r.informal.label) : '') + '</span>');
  if (r.cas && r.cas.object) push('Computational object', esc(r.cas.object));
  push('Reading the names', esc(r.convention_frame));
  if (r.literature && r.literature.length)
    push('Sources', r.literature.map(esc).join('<br>'));
  push('Ancestry', esc(r.ancestry));
  push('Evidence', esc(r.evidence_anchor));
  push('Notes', esc(r.notes));
  return '<div class="detail"><dl>' + d.join('') + '</dl></div>';
}

function render(){
  const q = query.trim().toLowerCase();
  const rows = DATA.rows.filter(r => {
    if (filter !== 'all' && r.warrant !== filter) return false;
    if (!q) return true;
    return JSON.stringify(r).toLowerCase().includes(q);
  });
  const list = document.getElementById('list');
  if (!rows.length){ list.innerHTML = '<div class="empty">0 of the rows match &mdash; clear the search or choose All to see everything.</div>'; return; }
  list.innerHTML = rows.map(r => `
    <div class="row">
      <button class="rowhead" aria-expanded="false">
        <span class="badge ${CLS[r.warrant]||'b-none'}">${esc(LABEL[r.warrant]||r.warrant)}</span>
        <span class="rowtitle">
          <span class="s">${esc((r.informal&&r.informal.statement) || (r.lean&&r.lean.declaration) || r.id)}</span>
          <span class="i">${esc(r.id)}</span>
        </span>
        <span class="caret">&#9656;</span>
      </button>${detail(r)}
    </div>`).join('');
  list.querySelectorAll('.rowhead').forEach(b => b.onclick = () => {
    const row = b.parentElement, open = row.classList.toggle('open');
    b.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
}
document.querySelectorAll('.chip').forEach(c => c.onclick = () => {
  filter = c.dataset.f;
  document.querySelectorAll('.chip').forEach(x =>
    x.setAttribute('aria-pressed', x === c ? 'true' : 'false'));
  render();
});
document.getElementById('q').oninput = e => { query = e.target.value; render(); };
render();
</script>
</body></html>
"""

out = (TPL
       .replace("__TITLE__", "Almanac A0a — the centre of the even hybrid family quantum GL(1)")
       .replace("__SUB__", "The pilot edition · a closed record in three layers")
       .replace("__NTOTAL__", str(len(rows)))
       .replace("__NKERNEL__", str(n_kernel))
       .replace("__NRANGE__", str(n_range))
       .replace("__NINK__", str(n_ink))
       .replace("__HUMANMIN__", str(man["cost"]["human_minutes_total"]))
       .replace("__WALLMIN__", str(man["cost"]["wall_clock_minutes_total"]))
       .replace("__EDITION__", html.escape(con["edition"]))
       .replace("__DATA__", DATA))

# In the SOURCE TREE the page is staged in dist_src/ and the assembler copies it in.
# Inside an UNZIPPED ALMANAC there is no dist_src/, and the page belongs beside this script.
# Getting this wrong is silent: the command succeeds and the page the reader opens is stale.
staging = os.path.join(ED, "dist_src")
dest = os.path.join(staging, "index.html") if os.path.isdir(staging) else os.path.join(ED, "index.html")
with open(dest, "w", encoding="utf-8") as f:
    f.write(out)
print(f"wrote {os.path.relpath(dest, ED)} ({len(out):,} bytes) — {len(rows)} rows embedded, no network calls")
