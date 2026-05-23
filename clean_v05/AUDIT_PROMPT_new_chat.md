# AUDIT PROMPT — CSG-KP v05 (paste as the first message in a new chat, attach csg-kp-clean_v05.zip)

You are a hostile, fair peer reviewer and code auditor. Operate in strict
falsification mode. No confirmation bias. No softening for elegance or effort.
Do not accept rhetorical claims without proof. Do not accept internal
consistency as external evidence. Before you output any comment, praise, or
criticism, try to break it yourself first.

Use this status taxonomy throughout: THEOREM (proven) / DERIVED-GIVEN-ASSUMPTION
/ LITERATURE-SUPPORTED / CONVENTION / POSTULATE / CONJECTURE / OPEN / WRONG.

## What is attached
`csg-kp-clean_v05.zip` — a cosmology project (CSG-KP) restructured around a
single open assumption. Key files:
- `clean_v05/csg_kp_clean_one_assumption.tex` — the clean structure
  (assumption L; falsifiable core C1–C6; quarantined magnitude M1–M5).
- `clean_v05/formal_derivation_skeleton.tex` — formal chain S1→S7 with status.
- `clean_v05/Peer_Review_CSG-KP_v04.md` — prior review.
- `clean_v05/revision_package_v05.md` — revision list for the main manuscript.
- `manuscript/csg_kp_facharbeit.tex` — the full manuscript (~2200 lines).
- `python/verify_clean_pipeline.py` — re-verification + built-in falsification.
- `python/run_all.py` and `python/foundations/*` — the full engine.

## The claim to be tested
Under ONE open assumption — (L) the no-boundary construction has a stable
Lorentzian realisation Φ that preserves the scale-free anomaly quotient and
persists to today — the photon conformal anomaly yields a parameter-free,
sharply falsifiable curvature ratio Ω_K/Ω_Λ = a_γ/(8π²) = 2.18×10⁻³ with
Ω_K>0 (open), testable by DESI DR3 / Euclid. Everything magnitude-related is a
separate, open postulate and must NOT inflate the status of this ratio.

## Your tasks
1. **Re-derive every core number independently** (do NOT trust the repo's code;
   recompute with your own sympy/mpmath): a_γ = 31/180 from the heat-kernel b₄;
   C_Q = ∫_{D⁴}Q₄ = 8π²; ρ_E = a_γ/8π² = 31/(1440π²); cap-saddle root of
   a_γcos⁴δ = sinδ (expect 0.16391); the BFK closure 2·(52/45) − 3 = −31/45;
   |ζ(0)|/a_γ = 4. Report any discrepancy as WRONG.
2. **Run and audit the engine.** Run `verify_clean_pipeline.py` and `run_all.py`.
   For each "PASS", decide whether it is a real numeric check or an argument
   that merely "passes by running". Flag every tautological pass (e.g. a Banach
   fixed point with Lipschitz constant 0).
3. **Check three-way consistency:** manuscript ↔ clean .tex ↔ code. Where the
   manuscript says one thing and the clean doc/code another, report it.
4. **Attack the single-assumption claim.** Verify or refute the following
   findings (already suspected; confirm independently):
   - (L) is the only OPEN assumption, but the core also rests on A3 (photon-IR
     uniqueness, KS a-theorem, with a graviton premise inside sub-assumption
     A3.1) and on the hemisphere selection of the Q-charge. Is "one open
     assumption" honest, or is A3 doing hidden work?
   - FLT (Feldbrugge–Lehners–Turok) instability of the Lorentzian no-boundary
     wavefunction: confirm the manuscript does NOT resolve it and that CSG's
     proven stability is only the EUCLIDEAN Hessian (a different object).
   - The magnitude (P5) carries all 122 orders and is a postulate; confirm the
     ratio is provably P5-independent (H, M_Pl cancel) so the quarantine holds.
   - The budget ladder Ω_Λ = 4a_γ is a 0.0σ central-value coincidence
     (σ≈0.0056), an action-invariant not derivable from dynamics — confirm it
     does NOT leak into the C6 falsifiable number.
   - The cap-saddle uniqueness (Banach contraction |G'|<2) is numerical, not
     analytic; the invariant uniqueness (Prop) is "within criteria (i)-(iv)",
     not unconditional. Confirm.
5. **Hunt for NEW hidden assumptions** the above list missed.
6. **Compare to the field:** Boyle–Turok / Deng–Handley (PRD 110, 103528, 2024;
   PRD 113, 023546, 2026) predict a discrete, version-shifting, closed Ω_K
   spectrum with a fitted Δk; check that CSG's fixed single value + sign-output
   is correctly distinguished from this, and that the comparison is fair.

## Required output
- Verdict (≤10 sentences): does the work prove its claim, make it plausible,
  postulate it, fit it empirically, or shift it onto an open principle? Is the
  shift precise and falsifiable?
- Claim-by-claim audit table (claim / location / author's status / actual
  status / comment).
- Engine audit: which checks are real, which are tautological/argument-only.
- Three strongest objections, each with the exact attack point and what
  computation or citation would settle it.
- A concrete punch-list to make the paper STRAIGHT-LINE: one open assumption
  (L) → the DESI-DR3-falsifiable ratio a_γ/8π², with everything else (magnitude,
  absolute Ω_Λ) clearly quarantined or removed. List exactly what to cut, what
  to relabel, what to keep.

## Hard rules
- "Stronger" must mean *better defended and more precise*, never *more likely
  true*. Do not let restructuring be mistaken for new evidence.
- If you find yourself constructing a derivation to please the author, STOP:
  the base rate for an on-demand derivation of an open quantum-gravity bridge
  is a hidden circularity, not a breakthrough. Report the gap; do not fill it.
- Child-safety, copyright, and harm rules apply as normal. Cite the field
  literature you actually verify; do not invent attributions.
