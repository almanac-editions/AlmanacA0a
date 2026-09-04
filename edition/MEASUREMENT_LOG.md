<picture>
  <source media="(prefers-color-scheme: dark)" srcset="almanac-mark-dark.svg">
  <img src="almanac-mark.svg" align="right" width="110"
       alt="almanac — the word's three a's carry the three kinds of warrant: informal, computational, kernel-certified">
</picture>

# MEASUREMENT LOG — the pilot almanac edition over sandboxA0a

**Seat:** the root-sandbox EDITOR (AD-27). **Campaign:** the A0a pilot.
**Rule this file obeys (charter §4):** entries are written **as the work happens**, never
reconstructed at the end. Reconstruction is the failure mode this log exists to prevent —
*a number remembered is a number invented.* Where a quantity was not measured, this log says
"not measured" rather than estimating it.

**Why this file is the campaign's product, not its paperwork.** The pilot exists to answer
"what does producing an almanac edition actually cost, and what does the form catch?" — for the
Almanac Editor post to be defensible as a human act rather than a line item. The edition is the
artifact; this log is the finding.

---

## Session 1 — 2026-08-13, first Editor summon

**Channel:** Claude (Fable-5 seat, in-session). **Agent assistance:** three subagents (below).
**Human involvement this session: ZERO minutes.** The Overseer's only act was the summon itself;
no human read, wrote, reviewed, or decided anything recorded below. This is a measurement, and it
is the single most important number in this log — see "The human/agent split" at the end.

### Activity ledger (elapsed, by activity)

| # | activity | start (UTC) | elapsed | agent/human | what it produced |
|---|---|---|---|---|---|
| A1 | Seat orientation: charter read in full, SEATS.json row, announce, phonebook | 10:32 | 2 min | agent | seat bound; address `sandboxa1-2d` live |
| A2 | Mail: inbox read, architect NOTICE acked | 10:33 | 1 min | agent | 1 message, no reply owed |
| A3 | Substrate verification: CLOSURE_SIGNATURE.json, APPROVAL_STATE, tree survey | 10:33 | 2 min | agent | campaign confirmed CLOSED (Approval-5, 2026-08-13) |
| A4 | Manifest consumed (`ALMANAC_EDITION_MANIFEST_2026-08-13.md`, 190 lines) | 10:33 | 2 min | agent | the ten items and the §0 layout |
| A5 | Inventory Q1 — GL1Newton adopt/supersede/alongside | 10:33 | 3 min | agent | provisional ADOPT on the package's own provenance block |
| A6 | Mail out: REQUEST to hypervisorA, NOTICE to dashboard, both rings owed and paid | 10:34 | 3 min | agent | `…103402Z`, `…103420Z`; both rung, both delivered |
| A7 | **Certification-evidence audit** (the release log vs the closure signature's claim) | 10:36 | 6 min | agent | **FINDING F-E1** (below) — the load-bearing finding of the session |
| A8 | hypervisorA REPORT received, read on arrival, acked | 10:36 | 1 min | agent | ADOPT **CONFIRMED**; extra provenance; warrant-discipline note |
| A9 | Authorship scheme located (settled 2026-08-05, ERC PoC minutes) | 10:38 | 2 min | agent | §8 block scheme + the one field the Editor may not fill |
| A10 | Toolchain/commit pins measured for the §7 recipe | 10:39 | 1 min | agent | Lean v4.30.0, Mathlib `c5ea0035`, estate commit `a4c04990` |
| A11 | Parallel extraction (3 subagents: Lean decls / Julia API+ranges / ancestry+cards) | 10:37 | dispatched | agent | raw material for the concordance |

| A12 | `AUTHORSHIP.md` + `EMBEDDING_NOTE.md` drafted | 10:40 | 12 min | agent | 2 of the 5 manifest-specified items |
| A13 | **Gates run**: `manuscript_gate.py` on both manuscripts | 10:47 | 4 min | agent | proof 9/9 ENFORCED; **goal → publication BLOCKED (F-E5)** |
| A14 | Ledger mined for per-claim declared ranges | 10:44 | 5 min | agent | 18 claims / 6 controls / 14 steps — the concordance's range data |
| A15 | **Instrument battery re-run** under `job_gate.py medium` | 10:41 | 9 min wall (4 min precompile, 3.2 s tests) | agent | **87/87 PASS** — settles F-E4 by measurement |
| A16 | `ANCESTRY.md` written from the Librarian extraction | 10:52 | 10 min | agent | §6 delivered, 3 findings |
| A17 | `gaps/GAPS.md` written | 11:00 | 8 min | agent | 10 findings/gaps, none smoothed |
| A18 | **Axioms measured first-hand** (`lean_verify`, 5 decls by the Editor + 11 by agent) | 11:05 | 3 min | agent | clean triple on every headline declaration |
| A19 | `CONCORDANCE.json` assembled — 11 rows | 11:08 | 14 min | agent | **the spine** |
| A20 | `EDITION.md` front matter | 11:14 | 9 min | agent | the human-facing entry point |
| A21 | `MANIFEST.json` generated (36 artifacts, hashes computed not transcribed) | 11:18 | 5 min | agent | the checkable set + the recipe |
| A22 | Deposit door researched; deposit routed with its blocker stated | 11:20 | 6 min | agent | the publication gate exercised |
| A23 | Reports to hypervisorA / Architect / Librarian; journal + state | 11:24 | 12 min | agent | findings routed to their owners |

**Session-1 total: ~2 h 15 min wall-clock, of which ~9 min was compute the Editor waited on.**
Three subagents ran concurrently for part of it (one opus Lean inventory, one sonnet Julia
extraction, one opus Librarian ancestry pass), so agent-time exceeds wall-clock time; the
comparable "one worker, no parallelism" figure would be roughly 3 h 30 min.

### Compute per deliverable — final

| deliverable | compute actually spent |
|---|---|
| `CONCORDANCE.json` (11 rows) | 16 `lean_verify` calls; 1 opus subagent (39 tool uses, 135k tokens) |
| `ANCESTRY.md` | 1 opus Librarian subagent (21 tool uses, 76k tokens) |
| `EMBEDDING_NOTE.md` + instrument rows | 1 sonnet subagent (16 tool uses, 93k tokens) + **1 gated Julia run** |
| instrument battery | `job_gate.py medium`, 242 s precompile (106 deps) + 3.2 s tests, rc=0 |
| everything else | the Editor's own session |
| **`release_verify.sh --source`** | **0 — blocked, F-E2** |

Heavy compute was invoked **once**, deliberately, to settle a number the record could not
substantiate. No Sage, Singular, Magma or worker pool. Nothing was backgrounded outside the gate.

### The certification split — measured, per row

| grade | rows | of 11 |
|---|---:|---|
| kernel-certified (clean triple, measured 2026-08-13) | 9 | 82% |
| computed over a declared range | 2 | 18% |
| neither | 0 | 0% |

**Every one of the 9 was verified first-hand**, not quoted from the closure record — which is the
only reason F-E1 is a finding about *evidence retention* rather than an unresolved doubt about the
mathematics. The 2 computed rows are the instrument and the oracle referee pin, and **neither can
ever be kernel-certified**: no Lean declaration states what a Julia program does.

### Was every concordance row fillable? (charter §4.4)

**Yes. 11 rows, 0 dropped, 9 fully filled, 2 with a named `null`.** The nulls are all "this layer
has nothing to say about this result" — two formal-side guarantees with no manuscript environment,
two results with no computational claim. Each is named *in the row*. No row was dropped, and no
field was invented to fill a column.

### Did the deposit gate operate? (charter §4.6) — YES, and it refused

**This is the pilot's most useful single result.** The publication gate operated, before deposit,
and **refused**: `manuscript_gate.py` on `goalv0a.tex` returns the rule *"An edition may not be
published while any of its manuscripts still lacks the [criterion-13] declaration."* The edition is
assembled and correct and **cannot ship**.

What the door required, measured: the deposit route for closed-sandbox material takes **graded**
material from the producing sandbox, with the Librarian curating and never grading — *"a ledger
arrives graded or it does not arrive"*. This edition arrives graded (per-row warrants, first-hand
axioms, declared ranges). It is the *manuscript-form* precondition, not the grading precondition,
that stops it. Deposit was therefore **routed with its blocker stated** rather than attempted as if
clean, and rather than quietly deferred.

**No retrofit was performed** (AD-21 §3.5). The one-line repair — adding `% criterion-13: adopted`
to a signed, locked manuscript — was available, obvious, and **not the Editor's to make**.

### Compute per deliverable (never as a pool — the standing resource rule)

| deliverable | compute | note |
|---|---|---|
| Inventory + gap list | 1 Fable-5 seat session, no heavy compute | all reads; no Lean build, no CAS, no Julia run |
| Lean declaration inventory | 1 opus subagent (read-only + `lean_verify` LSP calls) | no `lake build` triggered by the Editor |
| Julia API + declared ranges | 1 sonnet subagent (source reading only) | **test battery NOT re-run** — heavy-compute gate not invoked; ranges read from source |
| Ancestry + cards | 1 opus Librarian subagent (Library MCP) | shelf queries only |
| **Certification re-run** | **NOT RUN — blocked, see F-E2** | this is a finding, not an omission |

**Heavy-compute gate: never invoked this session.** No Sage, Singular, Magma, worker pool, or
large Julia/Python run. The 70/70 battery was **read, not executed**; its numbers below are the
record's, attributed to the record, not re-measured by this seat. Recording that distinction is
the point — an edition that re-states a number it did not measure, without saying so, is exactly
the overclaim the concordance's warrant field exists to prevent.

### The certification split (charter §4.3) — kernel / computed-over-declared-range / neither

Established this session at the level of the *evidence*, not the *claim*; per-row figures live in
`CONCORDANCE.json` and are summarised in `EDITION.md`. The headline is F-E1: the sandbox's
closure evidence and the sandbox's closure claim are not the same size.

### What broke, and what the gates caught

**F-E1 — the closure signature claims 13 certified declarations; its cited log evidences 5.**
`CLOSURE_SIGNATURE.json` records `certification.decls: 13` with the clean triple, citing
`formal/RELEASE_20260721_source_all_clean.log`. That log is **6 lines / 544 bytes** and contains
**5 PASS lines, all in the `KzBridge` namespace**. The endpoint the signature itself names —
`HybridQuantumLean.A1.GL1Newton.GOALv0a` — **does not appear in the log at all**. The most likely
innocent reading is that only the tail of the run's output was retained; the log's own final line
("ALL CLEAN") is a summary line consistent with a longer run. But *retained evidence is the
evidence*: as it stands, a third party re-checking the closure cannot see 8 of the 13
declarations, including the one the goal is about. Measured 2026-08-13T10:36Z.

**A third number then appeared.** `APPROVAL_STATE.json` records the same run as *"on all 8 decls"*.
So the record carries **13** (closure signature, source manifest, ledger honesty note), **8**
(approval state) and **5** (the log itself). All three cannot be right. The log's sha256 matches the
hash pinned for it in `TERMINAL_CONSISTENCY_RECORD.json` on 2026-08-12, so the artifact has not been
truncated since the closure was assembled — this 5-line file *is* the evidence the closure rests on.

**The reassuring half, and the reason this is a records finding rather than a mathematical one.**
The Editor verified the endpoint directly: `HybridQuantumLean.A1.GL1Newton.GOALv0a` returns exactly
`{propext, Classical.choice, Quot.sound}`, and so do `clause_i`, `clause_ii`, `clause_iii`,
`Nev_eq_span`, the five `KzBridge` declarations and the six non-degeneracy declarations — **16
first-hand measurements, all clean**. The mathematics is sound. What is defective is the *retained
evidence*: a third party running the public re-verification sees 5 of the 13 declarations the
signature asserts. Reported to hypervisorA; **not** repaired by this seat (the record is not the
Editor's to edit).

**F-E2 — the manifest instructs the Editor to run a gate the Editor may not run.**
Manifest §5 step 3 and charter §5.3 require `release_verify.sh --source`. That script writes its
artifact to `programme_path RELEASE_DIR`, defaulting to `SandboxA/sandboxA0/scratch/release/` —
**outside the Editor's chartered write surface** (`<sandbox>/almanac/edition/**`) and inside a
*different, closed* sandbox's tree. The path is not env-overridable; it is fixed by
`.sandbox-programme` at the root, which is likewise not the Editor's file. So the Editor cannot
discharge its own step 3 without violating its own §0 boundary. **Not worked around**: charter §0
says a record change that seems necessary is a finding to report, and this is the same shape.
Routed to the Architect (form defect: the two documents are individually right and jointly
unsatisfiable). Axioms were instead measured **read-only** via the Lean LSP, which writes nothing.

**F-E3 — `formal/SOURCE_MANIFEST.json` is internally contradictory and stale in four ways.**
Dated 2026-07-21. (a) Its `generated_by` says "post release_verify --source ALL CLEAN 13 decls"
while its own `kernel_certified_basis` says "release_verify.sh --source has **NEVER** been run for
this cone", with `kernel_certified: false`. (b) Its `version_control_gap` says `Sandbox/A1/GL1/` is
untracked in git with 0 commits — **it is tracked today** (all 7 files in `git ls-files`, measured
10:37Z). (c) Its open finding F7 says the non-degeneracy witnesses live only in a scratch tree
`/tmp/v0averify/` and not in the delivered cone — but `Sandbox/A1/GL1/NonDegeneracy.lean` exists
on disk today (15,662 bytes). (d) It describes a **5-file** cone; there are **7** files.
None of this is necessarily a defect in the *closure* — the closure rests on
`TERMINAL_CONSISTENCY_RECORD.json` (2026-08-12), three weeks newer — but the older manifest is
still on the shelf as the cone's description, and an edition that cited it would cite a document
that contradicts itself. **The edition does not cite it as authority**; it records this instead.

**F-E4 — a recorded number that could not be reproduced, and now has been measured.**
The instrument battery is recorded as `70/70` in three separate records. A static count of
`test/runtests.jl` gives **83** test statements. The Editor re-ran the battery under the gate rather
than ship a figure it could not reproduce: **87/87 PASS** (2026-08-13, Oscar 1.8.0, julia 1.12.6,
rc=0). So the recorded figure is stale in a *safe* direction — there are more passing tests than
recorded, not fewer — but three records now disagree with the instrument and with each other. The
edition prints 87/87, attributes it to its own run, and names the discrepancy.

**What the gates caught:** the manifest's own `warrant` discipline (§9 rules 1–3) is what
turned F-E1 from an invisible assumption into a measured finding. Had the edition been permitted
to say "A0a is closed with a clean triple, therefore every row is kernel-certified" — the exact
inference §9 rule 1 forbids — none of the above would have surfaced. **That is the pilot's first
positive result about the form itself: the concordance caught something before it shipped.**

### Decision independence (worth recording, per hypervisorA)

The Editor reached ADOPT on `almanac/GL1Newton/` from the package's own provenance block at
10:33Z and mailed it at 10:34Z. hypervisorA's independently-written adoption recommendation, with
the same conclusion, was already on the Architect's desk from earlier that morning and was
**not read by the Editor before deciding** (it was named in their 10:35Z REPORT, after). Two
seats, same conclusion, no contact — recorded because a pilot that cannot show its decisions were
independent cannot claim its review layer works.

---

## Session 1, part 2 — the findings came back, and one was against me

**11:00–11:20Z.** Not planned as a phase; it happened because the findings were dispositioned within
minutes and two of them changed the form itself.

| # | activity | elapsed | agent/human | outcome |
|---|---|---|---|---|
| A24 | F-E5 + F-E2 dispositioned by the Architect; charter and manifest amended | 4 min | agent | **both findings fixed at the form level, same day** |
| A25 | **Caught a ruling collision** between two seats, 56 s apart, on the same file | 3 min | agent | a signature-ready act **withdrawn** before signing |
| A26 | Withdrew my own earlier advice after testing it | 2 min | agent | see below — the session's most important act |
| A27 | Edition-level ancestry searches, 3 results + 5 definitions | 14 min | agent | 4 false literature claims prevented; 2 acquisitions surfaced |
| A28 | Dropbox sweep before treating the acquisitions as real | 2 min | agent | both genuinely absent; one wrong-author trap recorded |
| A29 | Concordance ancestry rewritten; `ANCESTRY.md` §§7–8; `DEFINITION_VERDICTS` | 15 min | agent | §6a condition 2 actually satisfied |

**Session total: ~2 h 50 min wall-clock. Human minutes: still 0.**

### What the form caught — the pilot's headline result

**Four false claims about the literature, stopped before signature.** A record act proposed
declaring `\nopredecessor` on all five numbered definitions of the signed goal — *on this Editor's
own advice*, offered from an armchair reading ("definitions of the object under study") and endorsed
in good faith by the record's owner. Then a ruling (§6b) required the failed search to exist before
the declaration could be written. **The searches refuted the advice**: at most one of the five
survives, and even that one only as a half. Three definitions have located, quotable predecessors,
and one — the divided classes — turns out to equal the Harman–Hopkins `q`-binomial polynomial
*exactly*, verified symbolically rather than by eye.

Had it been signed, four false statements about priority would sit in the signed lineage of a closed
sandbox, **looking verified forever**. This is the strongest evidence the pilot produced about the
method, and it is not about elegance: **the form caught something at the one moment catching it was
still cheap.**

Two further findings of the same kind, both against this seat:

- **F-A4** — four concordance rows claimed "none located" with **no search behind them**. The
  manifest calls that an assertion dressed as a finding, and it was right. Fixed by doing the
  searches, not by rewording.
- **The order-of-operations slip** — the acquisitions were filed *before* the local sweep rather than
  after. The sweep confirmed them anyway, but the correct order is sweep-then-file, and the estate
  has been bitten by the reverse before.

**A rising gap count is the correct direction.** This edition opened with 6 findings and now records
12. Every one added after assembly was found *by the form, against the edition or its author*. An
edition whose gap list converges to zero as it matures is an edition that stopped looking.

### A new activity class, and it prices differently from everything above

**Reading an acquired source to a verified locus: 12 minutes, acquisition to citation.**
`LNM 1415` reached the shelf at 13:27. By 13:32 the article was located in the volume
(pp. 123–137 via the volume's own table of contents), the predecessor identified (§2 Prop. 2.2,
p. 124), the relation to our objects **verified on the CAS kernel** (`G_n = q^{n(n−1)}·ν_n`, seeds
`n = 0…6`, certificate `b058e915…`), the frame difference characterised, and the record updated.

**This is a READING task, not a search task, and the two cost very differently** — the searches
above ran 14 minutes across seven queries and five definitions and returned *candidates*; this
returned a *citable locus with a certificate*. An edition needs both, and a cost model that prices
them as one activity will misprice the Editor post. Recorded as its own class at the record owner's
suggestion.

**It also changed a verdict rather than confirming one.** The acquisition was filed as a hard
blocker on a `\nopredecessor` declaration; reading it discharged the block **in the opposite
direction** — the row now *cites* instead of declaring. That is worth pricing too: the value of the
acquisition was not that it let us say "none located" more confidently, but that it stopped us
saying it at all.

### A communication defect of mine, recorded because it nearly cost a signature

I reported "Cahen–Chabert is now non-blocking" as **the closing line of a long mail whose subject
was about Gramain**. The record owner, reading in good faith, updated the instrument to defer the
act on Cahen–Chabert *alone* — an acquisition that gates none of the five definitions, which would
have deferred a signature indefinitely on something irrelevant to it.

**A consequence that changes what a signature waits on belongs in the subject line, not the
footer.** Caught within two minutes and corrected, but the cost of catching it was a second seat
happening to re-read carefully. Recorded alongside the ruling collision below, because they are the
same failure in different clothes: **the estate's coordination depends on someone noticing, and
noticing is not a mechanism.**

### One collision worth recording as a process fact

Two seats ruled opposite ways on the same file **56 seconds apart**, each correctly and in good
faith, neither having seen the other. It was caught only because a third seat happened to hold both
messages. Nothing in the mail system surfaces that two live acts touch the same artifact; the
recovery depended on a human-shaped act of noticing. Recorded because the next collision may not
have a reader in the middle.

### What the form caught, and what using it changed — the pilot's second product

**The form was revised four times in one day, each time because the seat using it reported rather
than resolved.** That is a measurement of the form, not of the edition, and it is what the pilot was
built to produce.

| revision | cause | what changed |
|---|---|---|
| criterion 1 scoped | the editor read "no historical commentary" strictly and **stripped a correct lineage** out of the edition | the prohibition now names its target — *earlier versions of our own proof* — and idea ancestry is required as narrative |
| manifest §6 item 1 | same finding, other end | ancestry became **a narrative of descent, not a source list**; the per-claim column became item 2, and the two are complements |
| manifest §11 opened | the editor reported a **second** divergence instead of resolving it by analogy | a register of genre divergences, with an admission test: the prohibition must be right for a manuscript *and* the edition must require the same content anyway |
| §11.4 + §11.0 | the editor kept a counterexample a strict reading of the new rule would have cut, and flagged it | a counterexample is a **proof, not evidence** — one witness discharges an existential completely; and the reporting duty's incentive was fixed at the head of the register |

**The incentive finding is the one that would not have been found by observation.** Reporting a
divergence you *want* costs nothing; reporting one you *suspect*, which is then rejected, costs a
little standing each time — so a seat quietly stops filing the boundary cases, and **nothing visibly
breaks**. The rule now says a rejected report keeps its number and its place, no record is debited
for a question the form could not answer in advance, and **an unbroken record of upheld reports is
evidence the duty has decayed rather than that it is working**.

**Two defects the editor found in its own finished work by complying rather than arguing:** the
register printed ranges with **no anchor at all** — worse than the thing being legislated against —
and both counterexamples were assertions a reader had to take on trust. The second fix generalised
into the form: *condition 2 is usually satisfiable by making the mathematics visible rather than by
adding apparatus.* Two clauses of derivation, and the reader is independent of us.

**The honest summary of the pilot's form question.** The form catches conformance; it does not catch
judgement — not legibility, not framing, not a false witness, not a criterion violated in prose
elsewhere. **What it does do is convert a seat's compliance into revisions of itself**, provided the
seat reports instead of deciding. Four revisions in a day is the measurement; whether that rate
survives contact with a seat less willing to file against its own work is not something this pilot
can answer.

### The human/agent split — the number the post depends on

**This session: 0 minutes human, ~100% agent.** Stated plainly because the temptation is to let it
pass: the pilot edition is, so far, entirely machine-produced under a human-signed charter, over a
record a human closed. What the human act *was* is the summon, the seat design, and the closure
signature — not the editing. If the Almanac Editor post is argued as a human act, **this log is
the evidence it must be argued against**, and the honest form of the claim is that the human
directs and signs while the machine assembles and measures. Anything stronger is not supported by
what happened here.

## Session 2, 2026-08-14 — the first cold re-measurement of an accepted edition

**Activity:** re-hash all 54 manifest rows against disk; read the one unread message; repair what
is inside the write surface. **~35 min wall-clock, 0 minutes human.**

**The measurement:** 51/54 rows resolved. Two card rows had drifted (F-E9); one row was a hash no
file could ever match (F-E10). **An edition accepted 19 hours earlier no longer described itself
correctly, and neither cause was carelessness at build time.**

**What this costs to catch:** one script and about two minutes of machine time. **What it costs to
miss:** a deposited edition whose integrity claim is false about two of its own artifacts, with the
falsity introduced by a neighbour seat doing exactly the right thing — improving a card at this
seat's own request. The asymmetry is the number worth carrying to the post: *re-measuring is
cheap enough that no protocol should ever route around it by relying on a notification.*

**The pilot's third product, if the first two were the form's revisions and its incentive defect:**
**an acceptance is a measurement, not a state.** hypervisorA's acceptance was correct when taken
and stale within four hours — not because anything was wrong with the edition, but because two of
the 54 files it names are owned by someone else and remained live. An edition assembled over a
CLOSED record is not thereby assembled over a FROZEN one, and the manifest is the only place that
distinction becomes visible.

## Session 5, 2026-08-19 — the review lane's first LATENCY failure, measured

**Seat renamed** `editor` → `shadow` on 2026-08-17; this log keeps its name and its history.
**Channel:** Claude (Opus 5 1M, in-session). **Agent assistance: none — no subagent spawned.**
**Human involvement: ZERO minutes.** The Overseer's only act was the summon, whose entire content
was `Seat:Shadow`.

### Activity ledger (elapsed, by activity)

| # | activity | start (UTC) | elapsed | agent/human | what it produced |
|---|---|---|---|---|---|
| E1 | Clock, seat resolution from `SEATS.json`, charter read in full (309 lines), announce | 07:43 | 4 min | agent | seat bound; address `sandboxa2-6b` |
| E2 | Mail: inbox read — **and `check` truncated its own listing** | 07:47 | 3 min | agent | **26 messages present, `check` displayed to 08-17T18:01 only**; 9 later ones, incl. both from `circular`, found by listing the inbox directory |
| E3 | Edition gate, bare (§12.2 standing duty) | 07:50 | 1 min | agent | **VERDICT: CLEAN** — 68 rows, 65 resolve, 3 self-referential, 0 drift, 0 uncommitted |
| E4 | Backlog triage: 3 undischarged REQUESTs, oldest 3.5 days | 07:51 | 6 min | agent | none had ever been cited in a `re:` field |
| E5 | **Byte availability measured for all three** | 07:57 | 8 min | agent | **F-E17** — one request's bytes unrecoverable; one recoverable but superseded; one superseded and answered |
| E6 | Editorial review: GoalA PBW companion, 37 pp / 4,099 lines | 08:05 | 41 min | agent | AMEND, 9 findings; `notes/REVIEW_A_GLN_drinfeld_double_pbw_2026-08-19.md` |
| E7 | Locator verification against 9 Library cards, read first-hand | (within E6) | 14 min | agent | 3 card-backed locator findings; 9/9 keys resolve, 9/9 committed |
| E8 | Mail out: residentA REPORT, hypervisorA term-2 copy | 08:46 | 4 min | agent | `…60120-2dd3`, `…64062-3643` |
| E9 | Form findings to the Architect (F-E14/15/16) | 08:03 | 3 min | agent | `…75857-cd10` — **answered in 6 minutes** |
| E10 | Editorial review: A1c SP-2026-021v2, 28 pp / 2,661 lines, recovered from git | 08:20 | 34 min | agent | AMEND, 7 findings; `notes/REVIEW_A1c_SP021v2_final_2026-08-19.md` |
| E11 | **Independent rebuild of the reviewed bytes** (two passes) | (within E10) | 3 min | agent | 28 pp, **0 Overfull, 0 Underfull, no warnings** — author's claim verified rather than quoted |
| E12 | Mail out: residentA1c REPORT, residentB2 closure, hypervisorv1c term-2 copy | 08:15 | 6 min | agent | `…13298-43e9`, `…68285-0ca0`, `…15480-0518` |
| E13 | Records: this log, `ACTIVITY.md`, `STATE.md`; repin; artifact re-render (§12.6(1)) | 08:20 | — | agent | in progress at time of writing |

**Wall-clock this session: ~1 h 55 min at E13. Human: 0 minutes.** Two full manuscript reviews
(65 pp, 6,760 lines) at **~37 min each**, including first-hand card verification and, for the
second, an independent rebuild.

### Compute per deliverable (§4.2 — never as a pool)

| deliverable | compute |
|---|---|
| PBW review (37 pp) | reads + 9 card reads + 1 `pdftotext` sweep; **no build run** (log inspected) |
| A1c review (28 pp) | reads + 2 `git show` blob extractions + **2 `pdflatex` passes** (~3 min) |
| gate runs | 2 × `verify_edition.py` (~1 s each) |
| **no heavy-compute job gate invoked** | no Sage, Singular, Magma, Julia or worker pool; two `pdflatex` passes are not a gated job |

### Certification split (§4.3) — unchanged this session

**Nothing this session touched the certification split.** Both reviews are **editorial and
read-only**; neither is kernel-certified, neither is computationally verified over a declared range,
and both say so on their own face. The one thing verified by execution is the A1c **build**, which
certifies typesetting and nothing mathematical. The distinction is stated because the temptation is
to let a rebuilt-and-verified artifact read as a checked result.

### Concordance rows (§4.4)

**Not touched.** Reviews live in `notes/` and are **never manifest rows** (§6a term 1). 11 rows
stand as accepted; the manifest gained no row from this session's work.

### What broke, and what the gates caught (§4.5)

1. **`mailbox2 check` silently truncated its own listing** (E2). 26 messages in the inbox; the
   listing stopped at 08-17T18:01, hiding 9 later ones — including two from `circular` and a
   REPORT that discharged one of this seat's own ids. **A truncated inbox listing is
   indistinguishable from an empty tail**, which is the same class as F-E13 (a truncated read of an
   integrity record) and the same class as the renderer hazard closed on 08-14 (*a silent
   truncation reads as coverage*). Found only by `ls`-ing the inbox directory against the listing.
   **This seat's own standing note about sweeping for items arriving since the last read is what
   prompted the check.** Reportable to the Architect as a tool defect; not this seat's surface.
2. **F-E17 — a review REQUEST may pin bytes no seat can obtain**, and nothing warns either party.
   Measured over the reviewed object of REQUEST `20260815T223654Z-residentA-45811-c564`, whose
   identification lives in `notes/REVIEW_A_GLN_drinfeld_double_pbw_2026-08-19.md` and not here (see
   the §12.4 note below): the manuscript is UNTRACKED; **42 of 45** candidates in that tree are
   untracked, and **20 of 27** version snapshots.
   The requested sha is absent from working tree, git and the author's own `versions/` archive.
   **And the discipline is not absent — it is aimed elsewhere:** for that manuscript the ONE tracked
   snapshot is the adopted anchor, exactly as designed. The anchor is protected; the living
   candidate, which is what a request and an adoption pin, is bare. **RULED THE SAME MORNING** as
   §6a clause 3b (Architect commit `6d5d963e`, NOTICE `20260819T080934Z-architect-93620-4679`): a
   review request pins a COMMIT, not a path plus a hash.
3. **A near-collision that would have passed a fast check:** the archive holds `40198caf…`, the
   request asked for `040138e2…`. Same digits, different order. Recorded because the failure mode is
   *reporting a request satisfied*, not missing a file.
4. **A false finding caught before it was filed.** Counting `proofinput` environments in A1a's
   source gives 2 = paired-wall calculus, which would have made residentA1c's
   `\cite[… External Input~2]{gl2-center}` locator wrong for a Harish–Chandra claim.
   `\newtheorem{proofinput}[theorem]` **shares the theorem counter**, and A1a's rendered PDF reads
   *"External Input 2"* precisely where its source reads `\ref{input:HC}`. **The locator is
   correct.** The near-miss is the measurement: a reviewer's most confident findings come from
   counting things in source order, and rendered counters do not obey source order.
5. **A card-driven suspicion that came back clean, twice** (the lowercase `proofv1a.tex` defect; the
   Apostol range restriction). Both printed in the review, because a review that reports only its
   hits gives the author no way to tell a checked-and-clean claim from an unexamined one.

### Whether the deposit gate operated (§4.6)

**It did not run as a deposit gate — deposit has not happened and is still not this seat's act.**
The §12.2 gate ran bare at summon (E3, CLEAN) and `--repin` at E13 for this log's own row, with the
§12.6(1) artifact re-render in the same act.

### The finding this session is actually about

**The lane failed by NOBODY BEING THERE, and no clause could see it.** §6a clause 3 measures what
the lane costs the provider and clause 4's trigger fires on the provider's own report — so a
three-and-a-half-day wait, during which the author advanced the manuscript and proceeded without the
non-author reading the clause exists to guarantee, could not reach either. **An
episodically-summoned seat cannot report its own unavailability: the seat that would raise the alarm
is the seat that is not there.**

**Reported at 08:03, ruled at 08:09 — six minutes** (Architect `20260819T080934Z-architect-93620-4679`,
commit `6d5d963e`): §6a clause 3a, a **2-day SLA measured on the REQUESTER'S wait**, implemented in the estate's mailbox
audit so that it **runs outside this seat** (implementation named in that NOTICE; not cited here as a
path, for the §12.4 reason below). The Architect's own note on
verifying it is worth keeping in this log: with the real threshold it printed nothing, and with the
threshold forced to zero it *still* printed nothing — because the backlog had been discharged an hour
earlier. **"Silence was the right output and the wrong evidence."**

**The number for the post:** two 30-plus-page manuscripts reviewed to nine and seven findings in
under two hours of machine time and zero human minutes — and the lane's binding constraint turned out
not to be reviewing capacity at all. It was **whether anyone was awake.** No amount of throughput
fixes that, which is why the repair is a guard outside the seat rather than a faster seat.

### F-E18 — §12.4 has no exemption for THIS FILE, and this file's job is to name other seats' surfaces

**Found by the gate, against this log, in the same act that wrote it.** `--repin` reported **2
cited-not-row**: the reviewed manuscript's path and the path of the Architect's new guard. §12.4 —
*the checkable set is closed under citation*, this seat's own proposed clause, adopted as worded —
therefore demanded both as manifest rows.

**And one of them cannot be a row.** The reviewed manuscript is UNTRACKED and its working copy
drifts; pinning it would create a row that can never satisfy the *zero rows pinning uncommitted
bytes* condition. **So two of this edition's own rules collide**, and the collision is reachable by
the ordinary act of recording what a session did.

**The resolution is not an exemption, it is that the citation was wrong.** §6a term 1 already says
reviews are never manifest rows and nothing in the edition cites them — because **the edition asserts
nothing about another tree's manuscript.** By naming the path *as evidence*, this log made the edition
appear to warrant bytes it has no claim over. The identification of record is the **REQUEST id** and
the review document in `notes/`; the same for the guard, whose citation of record is a **commit and a
mail id**. Both rewritten above, and the gate is clean.

**The general form, which is the reportable part:** a measurement log records **activity**, and
activity necessarily names surfaces the edition makes no claim about. §12.4 cannot distinguish *"I
read this"* from *"I warrant this"*, so it will keep pulling other seats' files into the checkable set
of any honest activity log. **The rule that resolves it is not a carve-out for this file but a
discipline for it: an activity record cites ids and commits, never paths.** An id names an act, and
acts are what a log is for; a path names bytes, and bytes are what a row is for. Routed to the
Architect.

## Session 5, second half — 2026-08-19, ~14:30–15:02Z · the talks room, a cold read, a guard

**~32 minutes. Human minutes: 0.** No subagent spawned all session.

| # | activity | elapsed | what it produced |
|---|---|---|---|
| E14 | ERC Art. 17 finding re-measured at source, estate swept for an emblem asset | 4 min | all three held; **estate held none** |
| E15 | Lockup fetched, **inspected as an image**, deck repaired, rebuilt ×2, rendered ×3 | 11 min | Madrid26 v2, 16 pp; **the render caught what the log could not** |
| E16 | Provenance correction + stale asset removed + shared-index finding | 6 min | F-E19; commits `3561fca`, `63bb206` |
| E17 | `room_guard` tested in a throwaway, twice (broken wrapper, then fixed) | 5 min | 3 cases, no pipes; two install blockers found |
| E18 | Cold read of ERC PoC Part B §1.a + §1.b.i, 4 rendered pages | 14 min | 7 findings + a measured 90-word budget |
| E19 | Records, journal, commits | — | in progress at time of writing |

### Certification split (§4.3) — untouched again

**Nothing this half touched the certification axes.** The deck repair is a funder acknowledgement;
the cold read is editorial. **The only things established by execution were a LaTeX build and a
guard's selftest** — typesetting and tooling, nothing mathematical. Stated because a verified-looking
artifact invites the opposite reading.

### What broke, and what caught it (§4.5) — five instruments answering the wrong question

**This half produced a clean set of one failure mode, and the estate named it today:**
*an instrument that answers a NEARBY question convincingly.*

1. **A LaTeX compiler answered "is this valid?"** while the live question was "does this read". Zero
   errors, zero warnings, an overprinted title page. **Fixed by `pdftoppm` and looking.**
2. **A dangling symlink answered "did the install succeed?"** with yes while "am I guarded?" was the
   question — git ignores a dangling hook **silently**. Found by `circular`, not by me.
3. **A shell pipeline answered a DIFFERENT PROCESS'S question.** `git commit | head` reports *head's*
   status. **Three seats fell into this within fifteen minutes** — the Architect via `grep`,
   `circular` via `| head -12`, this seat via `| head -10` — **and all three carry a written note
   about it.** Immunised on paper, none in practice.
4. **A matching hash answered "are these the bytes?"** and not "has the document moved" — `circular`
   measured the .tex/.pdf skew I had not asked about.
5. **A machine gate answered "is a citation present?"** and not "does it resolve" — evidenced by this
   morning's three locator defects in a manuscript that passed its gate.

**The one repair that worked, three times out of three, was not reading more carefully: it was ASKING
THE WORLD WHETHER THE EFFECT HAPPENED** — did the commit land, did the page render, does the file
exist. **That belongs in the standard above any further warning about exit codes.**

### The measurement I would carry to the post

**Two seats, one afternoon, four boundary or instrument failures between them — and every one was
disclosed by its author within minutes, with evidence and an undo attached.** My staged deletion rode
into `circular`'s commit; their install changed my committing without asking; I misread a pipeline;
they had already misread the same one. **None of it was caught by a gate.** All of it was caught by
somebody measuring afterwards and saying so immediately.

**The number for the post is not the failure count, it is the disclosure latency.** The fence did not
hold in either direction today. What made that survivable was that nobody spent an hour not knowing.

---

## Session 6 — 2026-08-22, 08:58Z onward · maintenance summon: a stale surface, and a blocked chain

**Channel:** Claude (Opus-5 seat, in-session). **Agent assistance: NONE — zero subagents spawned.**
**Human involvement this session: ZERO minutes.** The Overseer's only act was the summon, which
carried no task; everything below came off this seat's own carried-forward list in `STATE.md`.

### Time by activity (wall-clock, measured from the summon clock at 08:58Z)

| activity | wall-clock | human | notes |
|---|---|---|---|
| opening protocol (inbox, announce, kit, STATE) | ~4 min | 0 | inbox 0 unread; announce self-reported a "live holder" that was this session |
| measuring the two carried items | ~3 min | 0 | git/sha/mailbox reads only |
| repairing the §14a passage + rename cites | ~5 min | 0 | one file, this seat's own surface |
| two mails + rings | ~2 min | 0 | `…29810-7c33` hypervisorA, `…44362-5076` dashboard |
| journal + this log | ~4 min | 0 | written as the work happened, per charter §4 |

**Compute per deliverable: none.** No CAS call, no Lean check, no build, no job-gate run. The two
instruments used were `stamp_form_sweep.py` (~2 min per run, twice) and `git ls-files`/`shasum`.
**No deliverable was produced this session** — no edition row, no review, no deck. The output was
**one repaired surface and two messages**, which is what a maintenance summon costs.

### What the gates caught, and what no gate could have

- **`stamp_form_sweep.py` CAUGHT IT AND NAMED THE OWNER.** This seat's `STATE.md:435` was one of
  only **three STALE INSTRUCTION-role hits estate-wide**, listed with `[owner: shadow]`. The
  instrument worked exactly as built: it did not repair, it made the defect arrive with an address.
- **`mailbox2 send --re` REFUSED** an id this seat had SENT rather than received. Correct-as-written,
  and it means an id is threadable **from one end only**.
- **NO GATE SAW THE 2 DAY 11 HOUR STALENESS**, and none could have. hypervisorA reported the defect
  on 08-19 with *"fix it when you next touch the file"* — the right instruction to a daily seat and a
  **latent defect for an episodic one**. The clock on the repair started when the reporter's turn
  ended and ran unwatched until this summon. **This is F-E14's shape with the arrow reversed:** that
  clause measures a requester's wait *because the waiting seat is not there to report it*; here the
  waiting party was a **surface**, which cannot report anything at all.

### The measurement I would carry to the post

**A correct instruction, correctly given, produced a 2.5-day defect — twice, in two different
chains, on the same morning.** hypervisorA told this seat to fix a file "when you next touch it";
hypervisorA told residentA to commit an archive; residentA correctly refused to commit shared history
without authorization. **Every one of those acts was right, and the two queues behind them are still
open at 2.5 days.** The estate's failures this month have stopped being errors of judgement and
become **errors of latency between correct acts** — and latency is invisible from inside any single
seat, because each one sees only its own discharged obligation.

**The number for the post is not what the work cost. It is how long a correct instruction sat
undone, and who was structurally unable to notice.**

### Session 6 addendum — the same defect found three times on three surfaces in one morning

**+~12 min wall-clock, 0 human.** After the entry above closed, `architectCM` raised the identical
§14a staleness in `notes/talks/CLAUDE.md` — my room, my install. Repaired to a pointer, committed
`f722e6a` (hybrid/notes, scoped to `talks/CLAUDE.md`, room_guard verified GUARDED 5/5 first).

**THE COUNT IS THE MEASUREMENT: three surfaces, three seats, one morning, independently.** This
seat's `STATE.md`, `architectCM`'s continuity kit, and this room's charter all taught a stamp form
that had moved out from under them. None was found by its owner reading it; each was found by an
instrument or by another seat.

**AND THE PART THAT REVISES THE RULE.** `talks/CLAUDE.md` **already carried the pointer** —
*"Machine-readable forms: `harness/stamp_forms.json`"* — on the line immediately below the copy.
It was correct, it was current, and it changed nothing for two days. **A pointer placed beside a copy
is not a pointer.** The estate's fix for stale legs has been *"name the canonical source"*; what this
measures is that naming it is insufficient while the answer is still printed next to it. **The copy
must be deleted.** A reader handed an answer does not go and check a reference.

**Two instrument findings, both of the same family and both filed:**
- `mailbox2 send --re` refuses an id the CALLER SENT, so an id is threadable from one end only.
- `.git/hooks/pre-commit --selftest` **exits 0 with no output** — the hook does not pass `"$@"` to
  `room_guard.py`, so the flag is discarded and the guard runs in commit mode against an empty index.
  **The wrong invocation is indistinguishable from a pass**, in an instrument whose own header argues
  at length that an unguarded state must announce itself.

**The pattern under all four of this session's findings is one sentence:** every one of them is an
instrument or a document answering a **neighbouring question** — is the pointer present (not: is it
read), did the command exit 0 (not: did it run), is the id acked (not: is it discharged), is the form
written down (not: is it current). **None was a wrong answer. All four were right answers to the
question next door.**


### Session 6, part 3 — the session did not stay a maintenance summon

**The entry above was written at ~09:10Z and priced a maintenance summon honestly. It stopped being
one.** Recorded now rather than reconstructed later, from the timestamps of this seat's own mail and
commits:

| span | activity | wall-clock | human |
|---|---|---|---|
| 08:58–09:10Z | opening protocol, the §14a repair, two mails | ~12 min | 0 |
| 09:10–09:52Z | the cross-seat thread: pointer doctrine, the `--selftest` trap, the stamp-form census, the frozen-tree measurement | ~42 min | 0 |
| 09:52–10:07Z | Admin's git hold; compliance report and path declaration | ~15 min | 0 |
| 10:14–10:40Z | **the Overseer's second instruction**: rewrite Madrid26 over 𝔸_t | ~26 min | ~2 min (two answers, in session) |
| 10:40–11:15Z | hypervisorA's two interims; the grid asymmetry named and confirmed | ~35 min | 0 |

**Compute: still none.** No CAS call, no Lean check, no job-gate run. Two LaTeX compiles per attempt
(five attempts across two edits), one `stamp_form_sweep.py` run, and a scratch-tree baseline compile.

**Deliverables that DID land, against an entry that predicted none:** two Madrid26 revisions
(`226f4f3`, `d87067c`) plus two record commits in `notes` (`f722e6a`, `55dd8e5`), and **fifteen
carried items** in `STATE.md`.

### What the form caught this session, on the Shadow's own work

**Five defects in this seat's own hands, all caught before they left it, none by a gate:**
a local time wearing a `Z`; two repositories' HEADs recorded as one commit; a slide 80.7pt off the
bottom; a ring display 105.3pt too wide; a baseline compiled from the wrong HEAD so the line numbers
did not correspond. **Every one was caught by the same move — a second route to the same number** —
and one more, the N^ev/N^+ grid asymmetry, was caught only because the extract was read back before
it was sent.

**AND THE ONE THAT MATTERS MOST IS THE ONE NO GATE COULD HAVE REACHED.** The Overseer's instruction
to remove the square roots was executed exactly, and executing it revealed a trade that was invisible
when the instruction was given: **a_i = q^{n−i}z_i^{−1} was paying for the finer grid, so "no z in
the E_m" and "the same grid as before" cannot both hold.** That is not a defect in the instruction or
in the execution. **It is what doing the work honestly produces, and it is the argument for a seat
that transcribes rather than paraphrases.**

---

## SESSION 9 — 2026-08-26T12:25Z–15:49Z · the Palomar layer, and the almanac becomes a distributable

**Directed by the Overseer in four instructions arriving during the work**, which is itself the
measurement worth recording: this session's scope tripled mid-flight and the log below is per
activity, not reconstructed at the end.

### Effort by activity — human/agent split explicit (§4.1)

| activity | wall clock | human min | agent min | note |
|---|---|---|---|---|
| Opening protocol (charter, mail, announce, tree verify) | 8 min | 0 | 8 | |
| Locating "Palomar" and establishing it never reached this seat | 12 min | 0 | 12 | the finding, not the search |
| Palomar layer v1 — built from a prose summary | 22 min | 0 | 22 | **later falsified; see below** |
| Reading the real schema + comparator contract | 14 min | ~2 | 12 | human act: the Overseer supplied Testa's account and the two URLs |
| Palomar layer v2 — rebuilt against schema v0.4, validated | 31 min | 0 | 31 | |
| `index.html` — interactive reader view | 26 min | 0 | 26 | |
| `FOR_A_HUMAN.md` | 21 min | 0 | 21 | incl. install instructions for three toolchains |
| `FOR_AN_AI_AGENT.md` | 17 min | 0 | 17 | |
| Assembler, checksums, dist manifest, zip | 24 min | 0 | 24 | |
| End-to-end testing of the unzipped artifact | 19 min | 0 | 19 | **found 5 defects; see below** |
| Record, mail, reporting | 20 min | 0 | 20 | |
| **Total** | **~204 min** | **~2** | **~202** | |

**Human acts this session:** the four instructions, and supplying Testa's description with the two
canonical URLs. No human read, wrote, reviewed or decided anything inside the build.

### Compute per deliverable (§4.2), never as a pool

| deliverable | compute |
|---|---|
| `palomar/formalization.yaml` (+ generator, validator, 3 schema files) | 4 outward HTTP reads (2 GitHub pages, 3 raw schema files); 1 throwaway venv (`pyyaml`, `jsonschema`); no heavy-compute gate needed |
| `index.html` | pure local render; **0 network calls in the artifact itself, measured** |
| the two guides | authored; no compute |
| `AlmanacA0a.zip` | 80 files hashed twice (assembly + verify), 1.15 MB out |
| testing | 3 full unzip-and-verify cycles |

**No heavy-compute job was started; none was needed.** The Julia 87/87 battery was NOT re-run this
session — the figure quoted in the guides is the one measured 2026-08-13 and is cited as such.

### The certification split (§4.3) — unchanged by this session, and that is the point

9 of 11 rows `kernel_certified`; 2 `computed_over_declared_range`; 0 `neither`. **This session added
no mathematics and upgraded no warrant.** The Palomar layer reports the existing split; it does not
create one. `status.main_results[]` carries exactly the 9, and the 2 are recorded in `alignment`
with the reason they are excluded.

### What broke, and what the gates caught (§4.5)

**THE LARGEST FINDING IS THAT MY FIRST PALOMAR LAYER WAS WRONG IN TWO STRUCTURAL WAYS, AND MY OWN
CAVEAT IS WHAT MADE IT RECOVERABLE.** Built from `circular`'s careful prose summary of a schema
nobody had read, it (1) emitted nine per-result files when `formalization.yaml` is a **repo-root**
file, and (2) listed the second kernel as blocking when `nanoda` runs on **Palomar's** side. The v1
artifact carried a `schema_conformance` field stating in terms that it had not been checked against
the published schema. Reading the schema then falsified it. **An unverified claim that announces
itself is recoverable; one that reads as settled is not** — and this is the first time in this
edition's life that the practice paid out on the seat that wrote it.

**The validator caught a defect of mine within a minute of existing:** `comparator_config: null`
violates the schema, which types the field as a string. An optional field with nothing to say is
**omitted**, not nulled — a null asserts something false about the shape.

**End-to-end testing of the unzipped artifact found five defects that reading could not have:**
a dead `GAPS.md` link (the file is at `gaps/GAPS.md`); `render_index.py` named as runnable by the
agent guide and **not shipped at all**; two `source/record/...` paths in both guides missing their
`formal/` segment; and `render_index.py`, run inside an unzipped almanac, writing to a staging
directory that does not exist there — **silently, exit 0, leaving the reader's page stale.**
*All five are the same species: the artifact was correct in the tree it was built in and wrong in
the tree it will be read in. Only unzipping it somewhere else could find them.*

**The positive control that licenses this log's central claim:** regenerating with
`--license Apache-2.0` makes the document VALID. That is the only reason it can be said that the
licence is the *sole* remaining gap rather than the first of several.

### Whether every row could be filled (§4.4)

**No.** `project.license` is required by the schema and **cannot be filled by this seat** — no
licence is declared anywhere in the project, and choosing one is an outward-facing act. The
generator refuses to invent a value; the file therefore ships schema-INVALID by exactly one error,
visibly and deliberately. **A required field left honestly empty is this session's principal
deliverable to the Overseer, not a shortfall in it.**

Two further fields were left unfilled rather than fabricated: exact model identifiers (the record
holds tier labels — `opus`, `opus/max`, `opus/xhigh`, `sonnet` — not model ids), and per-declaration
model attribution (the campaign record attributes per **wave**, not per declaration).

### Whether the deposit gate operated (§4.6)

**Not reached, and now further away than it was.** Deposit remains sequenced behind the Overseer's
word on instrument items 2–4. This session **changed the accepted set** — a new artifact class
(`palomar/`), a new distributable (`dist/`), three new front-matter files — so `hypervisorA`'s
acceptance of 2026-08-13 no longer describes what the edition is. Re-acceptance requested; the
Overseer has authorised un-acceptance if the tree owner prefers it.

## SESSION 12 — 2026-08-29T20:23Z onward · the private GitHub push, and a duty the account swap defeated

**Written during the session, not after it, except where it says otherwise.** This entry also breaks a
gap: the log ended at session 9 and sessions 10 and 11 are not in it. They are not reconstructed here —
a number remembered is a number invented, and I did not run their clocks.

### Elapsed time and effort BY ACTIVITY, with the human/agent split (§4.1)

| activity | window (UTC) | ≈min | whose |
|---|---|---|---|
| Opening protocol — charter read in full, `announce --charter-read` (refused, then `--takeover`), mailbox read, campaign re-verified CLOSED | 20:23–20:30 | 7 | agent |
| Re-measurement of the distributable against circular's figures; copy-out to `/tmp`; cold checksum; `git init` + commit | 20:30–20:40 | 10 | agent |
| The repository-name question — four candidates put by the Overseer, measured against the record, decided by them | 20:41–20:48 | 7 | **split**: agent measured, **Overseer ruled** |
| Creating the empty private repository (web UI) | ~20:48–20:50 | 2 | **human (Overseer)** |
| Running `git push` in a terminal after the channel's permission classifier refused it | ~20:50–20:51 | 1 | **human (Overseer)** |
| Post-push verification — fresh clone, 82/82 checksums, remote-HEAD compare, anonymous privacy probe with two controls, licence field re-read | 20:51–20:54 | 3 | agent |
| REPORT to circular, ring to their live address, and the phonebook finding that came out of it | 20:54–20:56 | 2 | agent |
| This record — STATE.md session 12 + header restamp, this entry, the journal | 20:56– | — | agent |

**The human's share is small in minutes and large in kind: the only two acts that touched the world
outside this machine were both theirs.** That was not designed — the permission classifier on this
channel refused `git push`, so the split §1 argues for was produced by a permission boundary rather
than by the charter. Worth keeping precisely because it arrived by accident and landed in the right
place.

### Compute per deliverable (§4.2) — NOT MEASURABLE THIS SESSION, and the reason is structural

**No number is reported, and no pooled number is offered in its place.** krutkov is at its usage limit
until the morning of 2026-08-30, so this session ran on a temporary tamas-account channel
(`Shadowtemp`). The tamas pool is shared with roughly a dozen live seats writing concurrently; a delta
read from `usage_check.sh` across this session's window measures all of them. **The standing rule is
compute per deliverable, never as a pool — so the honest output is the gap, not an attributable-looking
figure.** *The measurement was defeated by an operational workaround nobody chose for measurement
reasons. If temporary channels become normal, this duty needs an instrument that reads per-session
rather than per-account, or it silently stops being satisfiable.*

### The certification split (§4.3)

**Unchanged, and deliberately so: this session made no mathematical claim.** Pushing bytes changes no
certification — the build carries the edition's own split, as assembled on 2026-08-29T20:25Z, and the
banner on all four faces says it is a PREVIEW and not the edition of record. Nothing was re-run, nothing
was re-certified, and no row moved between kernel-certified, computationally-verified-over-a-range, and
neither.

### Whether every concordance row could be filled (§4.4)

**Unchanged. One field still cannot be filled and it is not this seat's to fill:**
`palomar/formalization.yaml` `project.license` is `""`, verified in the pushed copy after the push.
**Private publication is what made that acceptable rather than blocking** — all-rights-reserved is the
correct state for a private repository, so the schema error survives without gating the look-and-see.

**AMENDED 2026-08-29T21:05Z, same session: the field is now DEFERRED BY RULING, not merely unfilled.** The
Overseer postponed the licence question until patent counsel advises. So §4.4's honest entry changes
shape — this is no longer "a row this seat cannot fill", it is **a row nobody may fill yet, with a named
dependency and no date**. *That is a better state than an open question and a worse one for planning:
the deposit sequence, the public/private question and the 17 September evaluator offer all now sit
behind an external adviser rather than behind anything measurable here.*

### What broke, and what the gates caught (§4.5)

1. **`announce` REFUSED — the P3 live-incumbent guard worked.** The seat had two live holders; the
   takeover is logged with the channel move as its reason, and no record file was written until the
   Overseer explained the account limit.
2. **The channel's permission classifier refused `git push` twice, and a credential probe once.** Not
   routed around. The consequence is recorded above as the human/agent split.
3. **circular's spec slug was wrong against the record** — `almanac-a0a` for a thing the record names
   `AlmanacA0a` 10 times, with `a0a` appearing zero times. Caught by grepping the artifact rather than
   by taste. **I had repeated the slug once before checking it**, which is the same failure at one
   remove.
4. **circular's 17:54Z figures were superseded by the 20:25Z rebuild** — 80/82/80 → 82/84/82, 75 ok →
   77 ok, same 5 drift. They asked to be re-measured rather than trusted; they were right to.
5. **A false negative I caught in myself before asserting it:** `grep -c PREVIEW index.html` returns
   **0**, and the banner is there — the HTML banner reads *"Preview build"* in mixed case while the
   markdown one shouts. I had a defect written before the case-insensitive re-run deleted it.
6. **The phonebook is stale for circular.** It rings `notes-25` (session 8ba51835, quiet 602m) while
   circular's last two mails came from `hybrid-7e` — the Circulartemp channel, which never announced.
   `mailbox2`'s automatic ring went to the dead address; the live one was rung by hand and told.
   **Temporary channels are invisible to the seat directory unless they announce, and both temp
   channels alive tonight demonstrate it — mine announced, theirs did not.**
7. **An uncommitted source change was sitting in the shared tree**: `dist_src/index.html`, session 11's
   preview-banner CSS and `<!--BUILD_CLASS_BANNER-->` placeholder — i.e. **the generator input for a
   banner that is live in the pushed artifact was not in the record.** Committed with this session's
   record and attributed to session 11.

### Whether the deposit gate operated (§4.6)

**No, and this session did not approach it.** A private GitHub repository is not the Librarian's door:
nothing was deposited, nothing was released outward, no identifier was minted, and the §12.2 cold
re-hash that turns a PREVIEW into a publishable build has still never run. **The PUBLISHABLE branch of
the publish gate remains untested against real zero-drift data** — unchanged from session 10's
disclosure, and now with an artifact in the world (privately) that makes it likelier someone assumes
otherwise.

### Session 12, part 2 — 2026-08-29T21:24Z · two instructions, one rebuild (appended before the manifest re-hash, so this entry ships)

| activity | ≈min | whose |
|---|---|---|
| Non-claims cut: 7 locations, 2 generators, positive restatement, sweep | 18 | agent |
| TeX authoring from proofv0a.tex + CAS re-derivation of the 7 table values | 12 | agent |
| render_explained.py: generator + embedded template + MathML build | 14 | agent |
| Rebuild, MANIFEST re-hash, unzip verification, repo sync | 8 | agent |

**What the gates caught this part:** the no-network guard's false positive on the MathML xmlns
(fixed to test what tags load); the shipped-set gap — the new generator was NOT in MANIFEST.json,
so the page's regeneration path would have been silently absent from the distributable, the exact
defect the generator exists to close (caught by listing the dist, not by any gate — a gap worth a
gate at deposit).

**Certification split: unchanged.** Typesetting and headings; no mathematical content moved. The
table values were re-derived as a transcription CHECK, not as new verification.

### Session 12, part 4 — 2026-08-29T23:52Z · the whole-almanac non-claims sweep (this entry postdates the assembly it describes; the shipped log is one entry behind by construction)

| activity | ≈min | whose |
|---|---|---|
| Banner + assembler prose rewritten positively (by hand — the Overseer's trigger) | 10 | agent |
| Extraction: 5 read-only agents over every editable surface | 34 (wall) | agents |
| Adjudication: 622 → classes; records excluded; 190 actionable | 6 | agent |
| Application: 7 per-file editors, self-validating | 4 (wall) | agents |
| Spot-checks of risky rewrites, regeneration ×4, rehash, assembly, unzip verify | 12 | agent |

**Compute, attributable this time:** the two workflows report their own spend — 311,338 tokens
(extraction) + 512,961 (application) = **824,299 agent tokens for this deliverable**, the first
per-deliverable compute figure a temp-channel session has been able to report (workflow-level
metering is per-spawn, not per-account — noted against the §4.2 gap recorded in part 1).

**Editors' own refusals, kept as findings:** the agent-guide claim-prohibitions stand (the negation
IS the instruction); one suggested rewrite was refused because it would have asserted an ordering
fact the measured record does not support ("ends before the endpoint"). **A sweep that can refuse
its own suggestions is the only kind worth running.**

## Session 14 — 2026-09-04T08:40Z–11:46Z · the paper placed, the order fixed, the mark everywhere

**FIRST SESSION ON CASTALIA** (`hauselgrp01:SandboxHQ`, Linux). Every figure below is measured in
the session, not reconstructed after it (§4).

| activity | wall clock | human | agent |
|---|---:|---:|---:|
| seat bind, charter read, mail (3 unread cleared) | ~12 min | 0 | 12 |
| the "open the almanac" link — accessibility, measured both ways | ~14 min | 0 | 14 |
| locating the paper; provenance by re-running the assembler | ~18 min | 0 | 18 |
| making `paper.pdf` byte-reproducible | ~11 min | 0 | 11 |
| Going further: order, the paper, the warrant badges | ~22 min | 0 | 22 |
| ink → orange → blue sweep across every surface | ~26 min | 0 | 26 |
| the mark on every HTML page (one definition, five renderers) | ~34 min | 0 | 34 |
| build-dependency repair on the new host | ~9 min | 0 | 9 |
| shipping the paper; the two count defects; rebuild + verify | ~29 min | 0 | 29 |
| journal, measurement log, mail | ~21 min | 0 | 21 |
| **total** | **~3 h 06 min** | **0 min** | **~186 min** |

**Human minutes in the assembly itself: 0.** The Overseer gave four instructions in two messages;
direction is not assembly labour, and the Almanac Editor post has to be defensible on the second
number, not the first.

**Compute per deliverable** (§4.2, never as a pool): two `pdflatex` passes × 3 paper builds; six
renderer runs; three full `assemble_almanac.py` builds; one `freeze_edition.py` (stopped at step 1);
one `verify_edition.py`. No CAS, no kernel, no job-gate class reached — nothing here approached the
medium threshold.

**The certification split is unchanged by this session** and remains the record's: 1 ink, 2 orange,
9 blue of 12. **This session moved no warrant.** What it moved is what a reader meets first, and the
edition's own arithmetic.

**Could every concordance row be filled?** Unchanged: 12 of 12 accounted for, 5 populated, 7 with a
field declared absent by design, 0 missing (`derive_completeness.py`).

**What broke, and what the gates caught** (§4.5):
- `freeze_edition.py` **STOPPED** on two corpus rows outside this surface (librarianCM's `8584ab0c`,
  `d37c4c3c`). Build stays PREVIEW. Correct behaviour, not a defect.
- `verify_edition.py` caught a **§12.4 cited-not-a-row** violation created in this session:
  `SandboxA/informal/goalA.tex`, cited by the paper's manifest row, is not pinned. Ask sent.
- **Two pre-existing arithmetic defects in `DIST_MANIFEST.json`'s own self-description**, both off
  by the four root furniture files: `provenance_rows` claimed to equal `files_shipped` (106 vs 102),
  and `files_on_disk` named a command that answers 108 where the field said 104. Both now derived
  and asserted.
- **One defect of mine, caught by counting**: the paper shipped through two routes and appeared
  twice in the provenance rows.
- **A build dependency did not survive the host move** (`markdown`, `latex2mathml` absent), and
  `render_docs.py` exiting at import took five renderers down with it. Import made lazy.
- **`EDITION.md`'s certification split was stale** — 9/2/0 of 11 against a live 9/2/1 of 12.
  Repaired; **still hand-written, so it will go stale again.** Recorded, not fixed at the cause.

**Whether the deposit gate operated** (§4.6): not reached. The build is PREVIEW and cannot be
deposited; two attributed re-pins are outstanding.

**BUILD NOTE FOR THIS HOST, because the next session will hit it in the first minute:**
`export PYTHONPATH="$HOME/.local/lib/almanac-build"` is required before any renderer runs on
castalia — `site-packages` is not writable and `pip --user` is refused in this interpreter.
