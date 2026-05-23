# Absolute Λ scale: investigation log (findings)

Question: can the pipeline triangulate the *absolute* dark-energy density
Ω_Λ (not just the ratio Ω_K/Ω_Λ), or is it irreducibly undetermined?

## Findings (in order, each verified numerically/analytically)

1. **Causal relation is an ansatz, not a CSG derivation.** `shawbarrow_causal.py`
   implements 3Ω_Λ = c/t_U² with c = A_∂M/V_M = O(1) as a *Shaw–Barrow analogue*,
   not derived from CSG.

2. **c = 1.86 is circular.** It equals the choice L = age t_U: then
   c = Λt_U² = 3Ω_Λ(H₀t_U)² returns the inserted Ω_Λ by construction.

3. **Causal-scale ambiguity is a scale-choice ambiguity.** Λ·L² gives
   c = 2.05 (Hubble), 1.86 (age), 2.72 (event horizon), 21.6 (particle horizon).

4. **dS event-horizon self-consistency has no non-trivial fixpoint.**
   3Ω_Λ − 3/χ_e²(Ω_Λ) < 0 for all Ω_Λ∈(0,1) (robust ∞-integration); only the
   trivial Ω_Λ=1 (pure dS) saturates it.

5. **Shaw–Barrow themselves claim only Λ = O(1/t_U²)** (their §, "naturally
   expect ... O(1/t_U²)"). Their *sharp* prediction comes from a SECOND relation
   (curvature consistency Eq.26 with ζ_b≈½ and inflation e-folds N), not from the
   causal Λ~1/t_U² alone.

6. **Causal-diamond A_∂M/V_M is definition-dependent O(1)–O(10),** not equal to
   3Ω_Λ (computed two boundary definitions; neither sharp).

7. **Correct route: not causal, but Theorem 64 (KP).** Λ* = ¼⟨ρ_m⟩_V4 from the
   matter density over the closed history. The CW vacuum has a unique minimum at
   ψ_min = e^(11/6), Λ*<0, and Λ*/v_S⁴ = −765.2·a_γ/128π² is a sharp dimensionless
   number.

8. **Correct classification: NOT the anthropic measure problem (categorical),**
   but a *averaging-prescription* problem (homogeneous vs structure-weighted) —
   physical, not anthropic.

9. **Scaling identity:** ⟨ρ_m⟩_V4 = ρ_m0·(∫dt)/(∫a³dt). So Λ*/ρ_m0 is a pure
   *shape* number of a(t): there is **no second scale**. v_S is dimensionally
   locked to ρ_m0; Ω_Λ/Ω_m is in principle predicted, NOT categorically free.
   (This kills the "categorically undetermined" framing.)

10. **But the value scales as 1/a_max³.** Moderate closed history (a_max~1.1–1.5)
    → Λ*/ρ_m0 ~ 0.13–0.33; physical σ-driven history (a_max~6.5e17) → ~3.6e-54,
    i.e. ~0. The σ-recollapse is far too late to truncate the V₄ average.

11. **Structure-weighting with an a³ volume factor ALSO collapses with a_max**
    (0.226 → 2.6e-53). Any V₄-volume measure is dominated by the late empty
    de Sitter volume. (Refuted the "structure-weighting is a_max-robust" guess.)

12. **KP and Lombriser are different mechanisms.** Theorem 64 = a V₄-*volume*
    average (suffers 1/a_max³). Lombriser 0.704 = structure-formation
    self-consistency (spherical collapse, y=½, a₀/a_eq) — NOT a volume average;
    it sidesteps the a_max³ problem because it does not average over 4-volume.

13. **KEY (analytic): the KP V₄ self-consistency is SCALE-INVARIANT.** On a closed
    matter+Λ history, ⟨ρ_m⟩/ρ_m0 = (x/3)·I1/I2 with x=|Λ|/ρ_m0, a_max³=3/x, and
    I1 = ∫₀¹ u^{1/2}(1−u³)^{−1/2}du = π/3, I2 = ∫₀¹ u^{7/2}(1−u³)^{−1/2}du = π/6,
    so I1/I2 = 2 exactly. Thus ⟨ρ_m⟩/ρ_m0 ∝ x (LINEAR), and the self-consistency
    x = ¼·(x/3)·(I1/I2) = x/6 is scale-invariant: it does NOT fix x. The 1/a_max³
    dilution of finding 10 IS this scale-invariance, g(x) ∝ x.

## Three framings, each corrected
- "categorically undetermined (measure problem)" — FALSE (too pessimistic);
  v_S is locked to ρ_m0, no second scale (finding 9).
- "81% prior-free + 19% averaging" — TOO OPTIMISTIC; the 81% holds only for an
  idealized moderate history, not the physical σ-history (finding 10).
- TRUE: the KP V₄ trace-zero condition is scale-invariant (finding 13); it fixes
  the Λ STRUCTURE (sign, no-vacuum-dependence) but not the dimensionless Ω_Λ/Ω_m.

## Resolution — the explanation IS derivable from what we already have

The "absolute Ω_Λ" is NOT a separate open hole. It follows from one proven fact:

  (P) the KP trace-zero condition is scale-invariant  (finding 13, I1/I2=2 exact).

Dimensional consequence: a scale-invariant condition determines all DIMENSIONLESS
ratios but leaves exactly ONE overall scale free. Hence:
  - Ω_K/Ω_Λ = a_γ/8π²  is fixed (dimensionless)  → THEOREM, as proven.
  - the one free overall scale must be supplied by a single dimensionful anchor.

That single anchor is v_S (the CW scale; "calibrated" in the Facharbeit) — or
equivalently any one of {ρ_m0, a_eq, H₀}, all dimensionful and set by
microphysics/measurement (like Λ_QCD is). It is NOT a measure problem and NOT an
extra postulate beyond the one the Facharbeit already names.

So the chain closes with no new open point:
  scale-invariance of trace-zero (proven)
    => only dimensionless ratios are fixed by the framework (ratio is Theorem)
    => exactly one dimensionful anchor is needed and sufficient (= v_S, calibrated)
    => absolute Omega_L = (dimensionless prediction) x (that one anchor).

KP (scale-invariant structure, sign Lambda<0) and Lombriser (structure-formation
self-consistency that supplies the anchor via a_eq + collapse threshold, with the
single assumption y(t0)=1/2) are COMPLEMENTARY, not competing. The only genuine
residual freedom is y(t0)=1/2 inside the structure-formation averaging —
everything else is either Theorem (ratio) or the one calibrated scale that
scale-invariance *requires* to exist.

## Update (this session): two further results

1. **The mean_R_over_4 sharpness proxy is a floored-geometry artefact (retracted).**
   The "moderate a_max breaks the de Sitter identity -> sharp <R>/4" construction
   in `kp_volume_selfconsistency.py` builds a closed history from a CONSTANT
   positive Omega_Lambda plus a curvature term forcing H^2=0 at a_max. But constant
   OL>0 never recollapses, so H^2<0 on 1<a<a_max and was silently floored at 1e-30;
   the resulting numbers (and the "identity regime" reading) are artefacts. The
   correct CW dynamics (real recollapse needs V(phi)<0) are in
   `cw_banach_iteration.py`: Lambda* is UNIVERSAL in phi_0 and Om (the structure is
   real) but its value is amplitude-set (~-0.10 for A_CW, not -0.69), and
   Omega_Lambda=(V(phi_0)-Lambda*)/3 stays free. This CONFIRMS this log's conclusion
   (only the ratio is fixed; one anchor is needed) by an independent route, and it
   supersedes the "81% / identity-regime" framing of findings 10 and the Facharbeit.

2. **A geometric budget ladder (conjecture) — the one route that would NOT need an
   anchor.** `budget_ladder.py`: with Omega_Lambda = int<T>(S^4) = 4 a_gamma, the
   factors 16pi^2, 32pi^2=int E_4(D^4), 64pi^2=int E_4(S^4) form a 2^n pi^2 ladder
   giving Omega_Lambda=4a_g (leading, a_g^1), Omega_K=a_g^2/2pi^2 (subleading, a_g^2),
   joined by the exact identity Omega_K*32pi^2=Omega_Lambda^2; full budget matches
   Planck at 0.0/-0.27 sigma. If true, the absolute scale is topological (no anchor).
   BUT the identification Omega_Lambda=int<T>(S^4) is NOT derived: the local
   energy-density route gives only the RATIO a_g/8pi^2, so 4a_g needs an action/
   topological identification A5 does not supply, in tension with Lambda-channel
   sequestering. So this is a conjecture against this log's "one anchor required"
   conclusion, not a replacement for it — pending the action-identification bridge.
