---
id: lit-v2.jantzen-dilated-linkage-blocks
status: literature-theorem
lens: collab-notes
sources:
  - "collab-k-theory-fixed-points-quantum-groups-1-4:[p.7] Definitions 2.6-2.7 and Proposition 2.8"
  - "J.C. Jantzen, Lectures on Quantum Groups, II.6.4; Q. Situ, Proposition 3.7 (citations given in the draft)"
feeds:
  - "v2 GL3 centre: gives the exact ell-dilated affine-Weyl wall structure and strong-linkage order for Jantzen/Kac-Kazhdan wall crossing."
  - "v1c completed centre + ribbon: the accompanying block-center claim is a completion of affine-flag cohomology at roots of unity."
conventions_gap: >-
  The note uses cocharacters X_bullet, W_aff=Z Phi_bullet semidirect W, and the ell-dilated rho-shifted action at q=zeta_ell. Our GL3 HC variables carry the rho shift while Vermas are unshifted, and our even parameter is Q=q^2. Convert their lambda,mu to our coweight/HC lattice, determine whether ell or 2ell is the correct dilation after passing to Q, and fix affine-reflection translation signs before identifying walls with Shapovalov/Jantzen factors.
cas_probe_sketch: >-
  For A2 and small ell, enumerate W_aff orbits under bullet_rho^ell, generate all simple-reflection chains, and compare predicted linkage blocks with vanishing loci and rank drops of small Verma Shapovalov matrices.
traps:
  - "At roots of unity some blocks may refine further, as the transcript notes."
  - "The direction of the strong-linkage inequalities and the convention for affine reflections are load-bearing."
  - "Replacing q by Q changes the effective root-of-unity order when ell is even."
  - "The center-completion sentence is a cited draft claim, not proved in this transcript."
---

> **[p.7] DEFINITION 2.6.** `$\ell$`-dilated `$\lambda$`-shifted action:
> $$(\nu,w) \bullet_\lambda^\ell \mu = w(\mu - \lambda - \ell\nu) + \lambda,$$
> for `$\nu\in\mathbb{Z}\Phi_\bullet$`, `$w\in W$`. `$\ell=1,\lambda=0$` = natural action.

> **[p.7] DEFINITION 2.7 (Jantzen).** `$\lambda,\mu\in X_\bullet(T)$` are linked at `$\zeta_\ell$` if they are in the same `$(W_\mathrm{aff},\bullet_\rho^\ell)$`-orbit; they are strongly linked via a chain
> $$\lambda=\mu_0=s_1\bullet_\rho^\ell\mu_1\le\mu_1=s_2\bullet_\rho^\ell\mu_2\le\cdots\le\mu_{r-1}=s_r\bullet_\rho^\ell\mu_r\le\mu_r=\mu,$$
> where every `$s_i=s_{\beta_i,m_i}$` is an affine simple reflection. The order is denoted `$\lambda\uparrow_\zeta\mu$`.

> **[p.7] PROPOSITION 2.8 (CLAIM, cites [Sit24] Prop 3.7).** For `$\zeta\in\mu_\infty(k)$`:
> 1. `$\mathcal O_\zeta\simeq\bigoplus_\gamma\mathcal O_\zeta^\gamma$`, with blocks labelled by orbits of `$(W_\mathrm{aff},\bullet_\rho^\ell)$`.
> 2. `$[M(\mu):E(\lambda)]\ne0$` iff `$\lambda\uparrow\mu$`.

> **[p.7] CLAIM.** The categorical center `$Z(\mathcal O_\zeta^\gamma)$` at roots of unity is a completion of the cohomology ring of the affine flag variety `$\mathcal Fl_\ell=L_\ell G/\mathcal P_{\ell,\gamma}$`.

