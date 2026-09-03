---
id: lit-jantzen-harish-chandra-even-torus
status: literature-theorem
provenance: cited
provenance_note: "provenance split from grade 2026-08-01 (Librarian ruling). The old `literature-theorem` fused BOTH: it said somebody else proved this, which is provenance, not how well established it is for us. Provenance is mechanical and safe to set; the GRADE is NOT determined by it and is deliberately left unset — for most of these we hold a transcript, not a verdict."
lens: harish-chandra-image-vs-isomorphism-generic-quantum-group
sources: ["jantzen-lectures-on-quantum-groups:[printed p.109, Section 6.6 Proposition and its Remark; printed p.124, Lemma 6.23, 6.24(1), Theorem 6.25]", "J. C. Jantzen, Lectures on Quantum Groups, Graduate Studies in Mathematics 6, AMS, 1996; DOI 10.1090/gsm/006 — NOT on arXiv; shelf scan, read by vision"]
feeds: ["residentA — GL_n even-hybrid centre reference audit; the containment-vs-isomorphism distinction in the Harish-Chandra image statement"]
conventions_gap: "Jantzen's map is the SHIFTED Harish-Chandra homomorphism gamma_{-rho} o pi — the toral projection pi composed with the -rho shift — not a bare toral projection. Replacing it by a bare projection requires transporting the shift into a shifted Weyl action, and that dictionary is NOT written. His torus is the ORDINARY GENERIC even torus U^0_ev with exponents in 2*Lambda; it is NOT a family/Newton integral torus. He works over a field k with char(k)=0 and q transcendental over Q for the isomorphism — nothing here is a statement over a Z-form, at a root of unity, or with q an indeterminate over a ring."
cas_probe_sketch: "SEPARATING WITNESS for the two statements, and it is the whole point: exhibit an element of (U^0_ev)^W and ask whether it is IN THE IMAGE. Section 6.6 licenses no answer — it only says the image is contained in (U^0_ev)^W. Theorem 6.25 says every such element is hit, but only when char(k)=0 and q is transcendental over Q. So a probe that merely checks gamma_{-rho} o pi(z) lands in (U^0_ev)^W for various central z CONFIRMS 6.6 AND CANNOT DISTINGUISH IT FROM 6.25 — it is degenerate for the question being audited. To exercise 6.25 you must produce a preimage. Concretely: take lambda dominant with 2*lambda in Z*Phi, form z_lambda from Lemma 6.23, and check 6.24(1), gamma_{-rho} o pi(z_lambda) = sum_nu dim L(lambda)_{-(1/2)nu} K_nu, against the target element."
traps: ["DO NOT CITE SECTION 6.6 FOR THE HARISH-CHANDRA ISOMORPHISM. It proves CONTAINMENT ONLY: 'maps Z(U) to (U^0_ev)^W'. Jantzen's own Remark on the same page points forward to 6.25 for surjectivity. The collaborator note corpus/literature/collab/Center_computation.pdf cites 6.6 in support of an image statement; that citation does not carry the weight put on it.", "THEOREM 6.25'S HYPOTHESES ARE LOAD-BEARING: char(k) = 0 AND q transcendental over Q. Outside them the isomorphism is not asserted by this source.", "The evenness mu in 2*Lambda is DERIVED inside the 6.6 proof from the sign automorphisms sigma-tilde attached to homomorphisms Z*Phi -> {+-1}; it is not an assumption. Anyone reproducing it needs 5.2(1).", "THE SHELF PDF's TEXT LAYER IS OCR OF A SCAN AND IS UNUSABLE FOR MATHEMATICS (renders the membership sign as E, mangles subscripts). Everything on this card was read by eye. Do not quote this book from text extraction.", "Page offset for this scan: PDF page = printed page + 9.", "Sections 6.4-6.5, 6.22, 6.26 and 8.30 are NOT transcribed. **PARTIALLY DISCHARGED 2026-08-15: 6.26 IS NOW TRANSCRIBED, on `lit-jantzen-6-26-hypothesis-weakening-q-not-root-of-unity`, and it REMOVES the hypotheses this card records as load-bearing — the book extends Theorem 6.25 to `q` not a root of unity. Read the two cards together; this card is correct about §6.25's proof and must not be cited for the theorem's reach. 8.30 is located but still unread, so that link is relayed rather than verified. 6.4-6.5 and 6.22 remain untranscribed.** In particular the LATER EXTENSION of 6.25 that 6.26 and 8.30 describe is not captured, so this card must not be read as the last word on how far the isomorphism reaches."]
---
**SECTION 6.6 PROPOSITION [printed p.109]** — verbatim:

> The Harish–Chandra homomorphism $\gamma_{-\rho}\circ\pi$ **maps** $Z(U)$ **to** $(U^0_{ev})^W$.

**Containment only.** Neither surjectivity nor injectivity is asserted.

**REMARK, same page, Jantzen's own** — verbatim:

> We shall see in 6.25 that the image of $\gamma_{-\rho}\circ\pi$ is **all of** $(U^0_{ev})^W$ (at least if $\mathrm{char}(k)=0$ and $q$ transcendental over $\mathbf Q$).

**THEOREM 6.25 [printed p.124]** — verbatim:

> Assume that $\mathrm{char}(k)=0$ and that $q$ is transcendental over $\mathbf Q$. The Harish–Chandra homomorphism is an **isomorphism** between $Z(U)$ and $(U^0_{ev})^W$.

**The even-torus lattice [p.109].** Writing $\gamma_{-\rho}\circ\pi(u)=\sum_{\mu\in\mathbf Z\Phi}a_\mu K_\mu$ with $a_{w\mu}=a_\mu$, one shows $a_\mu\neq0$ forces $2(\mu,\alpha)/(\alpha,\alpha)$ even for every $\alpha\in\Pi$, i.e. $\mu\in2\Lambda$ — derived via the automorphisms $\tilde\sigma$ attached to $\sigma:\mathbf Z\Phi\to\{\pm1\}$, which preserve $Z(U)$, satisfy $\tilde\sigma\circ\pi=\pi\circ\tilde\sigma$ and commute with each $\gamma_\lambda$ on $U^0$.

**LEMMA 6.23 (TQ) [p.124]** — for $\lambda\in\Lambda$ dominant with $2\lambda\in\mathbf Z\Phi$ there is a unique $z_\lambda\in U$ with $\langle u,z_\lambda\rangle$ the trace of $uK_{2\rho}^{-1}$ on $L(\lambda)$; and $z_\lambda\in Z(U)$. **6.24(1):** $\gamma_{-\rho}\circ\pi(z_\lambda)=\sum_\nu \dim L(\lambda)_{-(1/2)\nu}K_\nu$ — the construction that supplies preimages, i.e. the surjectivity half.
