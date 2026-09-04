#!/usr/bin/env python3
"""Assemble paper.tex — the edition's reading document — from the three source manuscripts.

WHY IT EXISTS. The record keeps the statement and the proof as SEPARATE documents, and that
separation is load-bearing: the goal is signed and hash-frozen before any proving begins, so the
claim "the proof proves the statement that was signed" has content. A reader does not want two
documents. Measured 2026-09-03: goalv0a.tex carries five definitions and no theorem; proofv0a.tex
carries the theorem and no definitions. NEITHER IS A PAPER.

IT ASSEMBLES, IT DOES NOT AUTHOR. Every definition, statement and proof step is lifted verbatim
from a source manuscript. The framing sections and the reference apparatus are written here, and
every citation is grounded in a shipped card or the edition's ancestry record — including the two
constraints those cards carry in their own traps: Gramain is CITED BY ARTICLE, never by the volume
that contains him, and Jantzen §6.6 is cited for CONTAINMENT ONLY, never for the isomorphism.
Pólya's classical theorem has NO bibliography entry, deliberately: the original is not on the
shelf, and this project does not cite what it does not hold — the theorem is reached through the
held quotation in Harman--Hopkins, and the text says so.

MACROS COLLIDE AND THAT IS HANDLED EXPLICITLY: goalA.tex writes \\At for \\mathbb A_t, while
goalv0a.tex and proofv0a.tex write \\At for A_t. The rank-n section redefines them and the
rank-one section restores them, because a silent collision here would typeset a different ring.
"""
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "..", "..", "..", ".."))
SRC = {
    "flagship": os.path.join(ROOT, "SandboxA/informal/goalA.tex"),
    "goal1":    os.path.join(ROOT, "SandboxA/sandboxA0a/informal/goalv0a.tex"),
    "proof1":   os.path.join(ROOT, "SandboxA/sandboxA0a/informal/proofv0a.tex"),
}


def source_date_epoch(directory):
    """The edition's own assembly date as a Unix epoch — the timestamp pdfTeX stamps into the PDF.

    Read from MANIFEST.json's built_utc, which is what the assembler already uses to flatten the
    zip's mtimes. One constant, two artifacts, and neither reads the clock.
    """
    import calendar, datetime, json
    stamp = "2026-08-13"
    mp = os.path.join(directory, "MANIFEST.json")
    if os.path.exists(mp):
        stamp = json.load(open(mp, encoding="utf-8")).get("built_utc", stamp)[:10]
    return calendar.timegm(datetime.datetime.strptime(stamp, "%Y-%m-%d").timetuple())


def body(path, start, end=r"\end{document}"):
    t = open(path, encoding="utf-8").read()
    i = t.index(start)
    j = t.index(end, i)
    out = t[i + len(start):j]
    out = re.sub(r"^%.*$", "", out, flags=re.M)          # source comments are not for a reader
    return out.strip("\n")


PREAMBLE = r"""\documentclass[11pt]{article}
\usepackage[a4paper,margin=1.15in]{geometry}
\usepackage{amsmath,amssymb,amsthm}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[hidelinks]{hyperref}
\emergencystretch=3em

\newtheorem{theorem}{Theorem}
\newtheorem{proposition}{Proposition}
\newtheorem{lemma}{Lemma}
\newtheorem{definition}{Definition}
\newtheorem{remark}{Remark}
\newtheorem*{goal}{Statement}

% the rank-one meanings are the default; the rank-n section overrides and restores
\newcommand{\At}{A_t}
\newcommand{\Ft}{F_t}
\newcommand{\Nev}{\mathcal N^{\mathrm{ev}}}
\newcommand{\Uev}{U^{\mathrm{hyb,ev}}}
\newcommand{\HC}{\operatorname{HC}}
\newcommand{\Yc}{\check Y}
\newcommand{\Z}{\mathbb Z}
\newcommand{\ev}{\mathrm{ev}}
\newcommand{\qbinom}[2]{\genfrac{[}{]}{0pt}{}{#1}{#2}_{q}}
\newcommand{\Atev}{\mathbb A_t^{\mathrm{ev}}}
\newcommand{\Ftev}{\mathbb F_t^{\mathrm{ev}}}
\newcommand{\Nat}{\mathcal N_{\mathbb A_t}}
\newcommand{\Natev}{\mathcal N_{\mathbb A_t^{\mathrm{ev}}}}

\title{\textbf{The centre of the even hybrid family quantum $GL_n$}\\[2pt]
\large the statement for general $n$, and the case $n=1$ proved\thanks{The statement for
$n=1$ was fixed and signed before any proof was attempted, and the proof was checked against the
signed text; this document was assembled from those two records by the Almanac Editor of Project
Sandbox --- for the pilot edition, a software agent. The full record, including per-claim warrants
and machine verification, is the accompanying almanac edition.}}
\author{Tam\'as Hausel}
\date{}
"""


def build(outdir):
    P = [PREAMBLE, r"\begin{document}", r"\maketitle", ""]
    A = P.append

    A(r"""\begin{abstract}\noindent
A family quantum group carries, alongside the deformation parameter, independent toral parameters
$t_1,\dots,t_n$. Its \emph{even hybrid integral form} is the part of it that preserves every
integral Verma lattice; the question this paper is about is what the centre of that form looks like.
The answer proposed here is that the Harish--Chandra projection carries it isomorphically onto the
Weyl-invariant part of a \emph{Newton lattice} --- the functions on the multiplicative grid that take
integral values at every weight. Section 2 states this for $GL_n$. Sections 3 and 4 state and prove
it for $n=1$, where the root system is empty, the Weyl group is trivial, and the whole content is a
statement about integer-valued Laurent polynomials on a geometric grid: a bilateral form of the
quantum P\'olya theorem of Harman and Hopkins \cite{HarmanHopkins}. Section 5 records what was
searched for in the literature and what was found.
\end{abstract}""")

    A(r"\section{Introduction}")
    A(r"""\noindent
Two things distinguish the family quantum group from the usual one. The toral parameters
$t_1,\dots,t_n$ are free, so the algebra is a family over a torus rather than a single object; and
one takes not the whole algebra but the \emph{hybrid} integral form --- the elements preserving
every integral Verma lattice --- and inside that, the torally even part. The centre of that form is
the object of study.

\medskip\noindent
The shape of the answer is the same in every rank, and it is worth saying before any notation. A
central element is determined by what it does to a highest-weight vector, weight by weight; that
assignment is a function on a grid of weights; and the condition of being \emph{integral} --- of
landing in $\At$ at every weight rather than merely in the fraction field --- cuts out a lattice of
such functions. \emph{The theorem is that the centre is exactly that lattice of integer-valued
functions, cut down by the Weyl symmetry.} Nothing is lost and nothing extra appears.

\medskip\noindent
The lattice in question has a long classical ancestry. That the integer-valued polynomials on
$\mathbb Z$ are free on the binomial coefficients is P\'olya's basis theorem (we reach the original
through its quotation as \cite[Prop.~1.1]{HarmanHopkins}; the standard modern reference for the
subject is Cahen--Chabert \cite{CahenChabert}). On a \emph{geometric} progression --- the grid that
appears here --- the corresponding basis is due to Gramain \cite[Prop.~2.2]{Gramain}, for $q$ a
natural number; the $q$-analogue on the additive grid, with $q$ an indeterminate, is Harman--Hopkins
\cite{HarmanHopkins}. What the present setting adds is recorded in Section~5.

\medskip\noindent
Section~2 states the result for $GL_n$ in four clauses: a PBW basis, an intrinsic characterisation
of the integral form, the Harish--Chandra isomorphism onto the invariant Newton lattice, and a
coefficient-even refinement. \textbf{This general statement is not proved here.} It is the
programme's flagship, and it is stated so the rank-one case can be seen for what it is: not a
curiosity, but the first instance, with the root system empty.

\medskip\noindent
Sections~3 and~4 are the case $n=1$, stated and then proved in full. With $\Phi=\emptyset$ and
$W=\{1\}$ the algebra is a torus, the Harish--Chandra projection is the identity, and the three
clauses reduce to one substantial assertion: the even Newton lattice is spanned over $\At$ by the
shifted divided classes $\Yc^{u}\nu_r(\Yc)$.

\medskip\noindent
The rank-one case is small on purpose. It was carried from statement to proof to machine-checked
formalisation so that the cost and the failure modes of doing so could be measured; nine of the
twelve results in the accompanying edition carry a proof-kernel certificate. That apparatus is not
the subject of this paper and is not described here.""")

    # ---------------------------------------------------------------- rank n
    A(r"\section{The statement for $GL_n$}")
    A(r"""\noindent
\emph{What follows is the programme's flagship statement. It is stated, not proved.} Its
individual ingredients are classical: the triangular decomposition and the freeness of the toral
part go back to Lusztig \cite[\S3.2]{Lusztig}; quantum Verma modules and their contravariant forms
are treated in De Concini--Procesi \cite[\S\S17.1--17.4]{DCP}; and over the fraction field the
Harish--Chandra map is an isomorphism onto the invariants by De Concini--Procesi
\cite[\S18.3]{DCP} and Jantzen \cite[Thm.~6.25 and \S6.26]{Jantzen} --- Jantzen's \S6.6 already
placing the image inside the \emph{even} toral invariants. Integral forms assembled, as here, from
a divided-power negative part and a toral lattice appear in Habiro--L\^e \cite[\S8G]{HabiroLe}.
What is new in the statement is the family parameter, the hybrid (Verma-preserving)
characterisation, and above all the assertion that over $\At$ the centre is the full
\emph{integer-valued} lattice --- not the monomial ring the generic statement would suggest.
\renewcommand{\At}{\mathbb A_t}\renewcommand{\Ft}{\mathbb F_t}""")
    A(body(SRC["flagship"], r"\maketitle"))
    A(r"\renewcommand{\At}{A_t}\renewcommand{\Ft}{F_t}")

    # ------------------------------------------------------------- rank one
    A(r"\section{The case $n=1$}")
    A(r"""\noindent
Here $\Phi=\emptyset$, $W=\{1\}$, and the cocharacter lattice is $\Lambda=\mathbb Z$. The four
clauses above collapse: there are no root vectors, so the PBW basis is the toral monomials alone;
the Harish--Chandra projection is the identity; and the Weyl invariance is vacuous. What remains is
clause~(iii), and it is not vacuous at all.""")
    A(body(SRC["goal1"], r"\medskip"))

    # ------------------------------------------------------------- the proof
    A(r"\section{Proof of the case $n=1$}")
    # the proof's own \section headings are one level too high inside this paper: they are the
    # three clauses OF section 4, not siblings of it. Demote deepest-first so the second
    # substitution cannot eat the output of the first.
    _pf = body(SRC["proof1"], r"\section{Conventions}", r"\section{Attribution}")
    _pf = _pf.replace(r"\subsection{", r"\subsubsection{").replace(r"\section{", r"\subsection{")
    A(_pf)

    # -------------------------------------------------------- the precedents
    A(r"\section{Precedents}")
    A(r"""\noindent
This section records what was looked for in the literature, what was found, and what was not. It is
included because a claim of novelty is only as good as the search behind it; one search returned
nothing, which is a result, and is stated as one.

\subsection*{Clause (iii): the P\'olya ancestry, in three layers}
The classical layer is P\'olya's basis theorem: the integer-valued polynomials on $\mathbb Z$ are
free on the binomial coefficients. We hold it through its quotation as
\cite[Prop.~1.1]{HarmanHopkins}; the source states a \emph{basis}, from which the strict
containment $\mathbb Z[x]\subsetneq\mathrm{Int}(\mathbb Z)$ is immediate --- but the strictness
itself is not P\'olya's statement, and we do not attribute it to him. The standard reference for
the whole subject is Cahen--Chabert \cite{CahenChabert}.

The multiplicative layer is Gramain \cite[Prop.~2.2]{Gramain}: a basis for the functions taking
integral values on a \emph{geometric} progression. One distinction matters and is easy to miss:
Gramain's $q$ is a natural number $\ge 2$ and integrality means values in $\mathbb Z$, whereas here
$q$ is an indeterminate and integrality means values in $\At$. His grid is ours; his coefficient
ring is not. (Cahen--Chabert treat the geometric progression once, in Chapter~II, Exercise~15,
attributing it to Gramain on the page; the exercise as printed carries two misprints --- the second
node of the product and the sign of an exponent --- identified in the course of this search and
recorded in the edition's errata cards.)

The $q$-analogue layer is Harman--Hopkins \cite[\S1, Props.~1.1--1.2]{HarmanHopkins}: one variable,
additive grid, coefficient ring $\mathbb Z[q^{\pm1}]$, no family parameter. Both the forward
inclusion and the windowed reverse interpolation of Section~4 follow their~\S1. What is added here
is the passage to the multiplicative grid $\Yc=q^{\chi}$ and to bilateral exponents
$u\in\mathbb Z$, together with the Laurent clearing that makes the two-sided statement follow from
the one-sided one; the substitution $\Yc=1+(q-1)x$, which their \S4 closing remark connects to the
Cartan part of Lusztig's integral form, carries their grid node $x=[n]_q$ to $\Yc=q^{n}$ and their
basis term to $\nu_k(\Yc)$ term by term.

\subsection*{Clause (ii), and the general statement}
Clause~(ii) rests on the corresponding $GL_2$ statement proved earlier in this programme
\cite{SandboxGL2}. For the $GL_n$ statement of Section~2 the generic precedents are as cited there:
Lusztig \cite[\S3.2]{Lusztig}, De Concini--Procesi \cite[\S\S17--18]{DCP}, Jantzen
\cite[\S6]{Jantzen}, Habiro--L\^e \cite[\S8G]{HabiroLe}. None of these treats the family parameter
or the integer-valued lattice; over the fraction field the centre is the invariant \emph{monomial}
ring, and the content of the flagship is precisely that over $\At$ it is the strictly larger
Newton lattice.

\subsection*{What was searched, and how}
The citation cycle over the manuscript was run on 2026-08-09 and re-run over the whole library on
2026-08-13. Every result of Section~4 carries a citation; no result claims to have no predecessor.
One methodological finding is worth repeating, because it changed an answer: the first query run
--- the exact phrase \emph{Harish--Chandra isomorphism} against the statement shelf --- returned two
entries, both irrelevant, where the shelf in fact held twelve. \textbf{A hit count over a phrase
reports the shape of the query, not the shape of the shelf}, and a ``none located'' finding is
worth only as much as the surface it was run against.

\subsection*{What was not found}
For the coefficient-field bridge --- the assertion that enlarging the ambient coefficient ring from
$\Ft$ to $\operatorname{Frac}(\At)$ adds no new elements to the Newton lattice --- \textbf{no
predecessor was located}. The queries were \emph{base change}, \emph{faithfully flat},
\emph{extension of scalars} and \emph{localization}; every hit was unrelated. The nearest published
statement, Vandermonde coefficient descent in Cahen--Chabert \cite[Prop.~I.3.1]{CahenChabert}, was
located on the later pass and is the closest thing to a predecessor this claim has.
Harman--Hopkins \cite[\S4, Prop.~4.3]{HarmanHopkins} was assessed as a candidate and
\textbf{rejected}, and the reason is worth stating because the two look alike: their proposition
says the object \emph{grows} under localization and identifies the enlargement exactly, while the
claim here is that it does \emph{not} grow. ``Bigger, and here is how much bigger'' is not
evidence for ``not bigger at all'', however much both statements wear the word \emph{localization};
their localization also inverts the deformation parameter, where this one enlarges the coefficient
field of the toral parameter. Adjacent, and adjacency is not ancestry.""")

    A(body(SRC["proof1"], r"\section{Attribution}", r"\begin{thebibliography}"))

    A(r"""\begin{thebibliography}{9}

\bibitem{CahenChabert}
P.-J.~Cahen and J.-L.~Chabert,
\emph{Integer-Valued Polynomials},
Mathematical Surveys and Monographs \textbf{48}, American Mathematical Society, 1997.

\bibitem{DCP}
C.~De Concini and C.~Procesi,
\emph{Quantum groups},
in: D-modules, Representation Theory, and Quantum Groups,
Lecture Notes in Mathematics \textbf{1565}, Springer, 1993.

\bibitem{Gramain}
F.~Gramain,
\emph{Fonctions enti\`eres d'une ou plusieurs variables complexes prenant des valeurs enti\`eres
sur une progression g\'eom\'etrique},
in: Cinquante Ans de Polyn\^omes / Fifty Years of Polynomials,
Lecture Notes in Mathematics \textbf{1415}, Springer, 1990, pp.~123--137.

\bibitem{HabiroLe}
K.~Habiro and T.~T.~Q.~L\^e,
\emph{Unified quantum invariants for integral homology spheres associated with simple Lie
algebras},
Geom.\ Topol.\ \textbf{20} (2016), 2687--2835.

\bibitem{HarmanHopkins}
N.~Harman and S.~Hopkins,
\emph{Quantum integer-valued polynomials},
arXiv:1601.06110 (2016).

\bibitem{Jantzen}
J.~C.~Jantzen,
\emph{Lectures on Quantum Groups},
Graduate Studies in Mathematics \textbf{6}, American Mathematical Society, 1996.

\bibitem{Lusztig}
G.~Lusztig,
\emph{Introduction to Quantum Groups},
Progress in Mathematics \textbf{110}, Birkh\"auser, 1993.

\bibitem{SandboxGL2}
Project Sandbox,
\emph{The centre of the even hybrid family quantum $GL_2$}
(closure record of the signed goal, revision A1+R5), 2026.

\end{thebibliography}""")
    A(r"\end{document}")

    tex = os.path.join(outdir, "paper.tex")
    open(tex, "w", encoding="utf-8").write("\n\n".join(P) + "\n")
    return tex


if __name__ == "__main__":
    d = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    tex = build(d)
    latex = shutil.which("pdflatex") or "/Library/TeX/texbin/pdflatex"
    if not os.path.exists(latex):
        print(f"  wrote {tex} (no pdflatex found; not compiled)")
        sys.exit(0)
    # A REPRODUCIBLE PDF: same sources in, same bytes out — the same property the zip already has
    # and for the same reason. pdfTeX stamps /CreationDate and a trailer id from the CLOCK, so two
    # builds of identical LaTeX produced two different hashes (measured 2026-09-04: paper.tex
    # identical byte-for-byte, paper.pdf 73bb59dd -> 67165529). This edition PINS the sha256 of
    # every file it ships, so a clock in the output means the pin moves on a rebuild that changed
    # nothing — "the hash moved but nothing did" is the one answer an almanac must never give.
    # SOURCE_DATE_EPOCH is read from the manifest's own built_utc, never from the clock, exactly as
    # assemble_almanac.py stamps the zip; FORCE_SOURCE_DATE makes pdfTeX honour it for \today too.
    env = dict(os.environ, SOURCE_DATE_EPOCH=str(source_date_epoch(d)), FORCE_SOURCE_DATE="1")
    for _ in range(2):                      # twice, so references settle
        r = subprocess.run([latex, "-interaction=nonstopmode", "-halt-on-error",
                            "-output-directory", d, tex], capture_output=True, text=True, env=env)
    if r.returncode:
        tail = "\n".join(l for l in r.stdout.splitlines() if l.startswith("!") or "l." in l)[:1200]
        sys.exit(f"render_paper: pdflatex failed\n{tail}")
    for ext in (".aux", ".log", ".out", ".toc"):
        p = os.path.join(d, "paper" + ext)
        if os.path.exists(p):
            os.remove(p)
    print(f"  wrote paper.pdf ({os.path.getsize(os.path.join(d,'paper.pdf')):,} bytes)")
