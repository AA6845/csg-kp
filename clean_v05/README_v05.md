# CSG-KP — clean_v05 (single-assumption restructuring)

This folder restructures the CSG-KP project around **one open assumption**, with
the entire falsifiable content made conditional on it and the magnitude sector
quarantined. Nothing in the original physics was changed; the *architecture* and
the *honesty of dependency tracking* were tightened.

## Contents
- `csg_kp_clean_one_assumption.tex` — the clean structure: assumption (L);
  falsifiable core C1–C6 conditional on (L); magnitude sector M1–M5 quarantined.
- `formal_derivation_skeleton.tex` — formal chain S1→S7 with status per step;
  isolates the single non-deductive jump (A5b: does the Wick map Φ preserve the
  scale-free quotient?).
- `revision_package_v05.md` — surgical revision list for the main manuscript
  (11 items, priorities, plus what self-falsification *rejected*).
- `Peer_Review_CSG-KP_v04.md` — full independent peer review (verdict: major
  revisions; core sound, framing overstated).
- `../python/verify_clean_pipeline.py` — new verification pipeline organised by
  the C/M architecture; re-derives every core number independently and contains
  a built-in falsification of the "one assumption" claim.

## The architecture in one screen
**(L)** — the single OPEN assumption: the no-boundary construction has a stable
Lorentzian realisation Φ that preserves the scale-free anomaly quotient and
persists to today. **Open and FLT-contested; CSG does not resolve it.**

**Core C1–C6** (falsifiable, conditional on (L)):
- C1 a_γ = 31/180 — theorem, (L)-independent
- C2 C_Q = 8π² — value theorem; relevance needs hemisphere selection
- C3 ρ_E = a_γ/8π² = 2.18×10⁻³ — theorem, (L)-independent
- C4 Ω_K/Ω_Λ = Φ_*(ρ_E) — needs (L); the entire empirical content
- C5 sign Ω_K>0 — needs (L)+HH branch (cap saddle δ*=0.16391>0)
- C6 prediction band + falsifiers — DESI DR3 / Euclid

**Magnitude M1–M5** (quarantined; postulates/conjectures, NOT the falsifiable core):
A2 sequestering, P5 accumulation (carries all 122 orders), KP self-consistency,
budget-ladder conjecture Ω_Λ=4a_γ, A3+A5c. The scale-free ratio C4 is provably
independent of all of these (ρ_E has no H, M_Pl).

## What the self-falsification found (and the documents now state)
"One assumption" is a simplification. The honest core rests on:
**one OPEN assumption (L)**, **plus A3** (photon-IR uniqueness — literature-
supported by the Komargodski–Schwimmer a-theorem, but with the graviton premise
inside sub-assumption A3.1), **plus the hemisphere selection**. The clean .tex
and the pipeline both now state this; "one assumption" without this qualification
would be an overclaim.

## Reproduce
```
cd python && python3 verify_clean_pipeline.py    # core re-verification + falsification
python3 run_all.py                               # original full suite (unchanged)
```
PASS means the stated identity was independently recomputed; it does NOT certify
(L), A3, or the magnitude postulates.

## v05 tightening (this revision)
- C6 made quarantine-clean: the falsifiable number is the *dimensionless ratio*
  Ω_K/Ω_Λ = 2.18×10⁻³ itself, tested directly against the DESI-DR3 measured
  ratio. No Ω_Λ value is fed in, so the ladder conjecture (M4) cannot leak in.
- C4 relabelled [STRUCT|L]: a structural claim conditional on (L), with no
  numeric content of its own (no false green check).
- `AUDIT_PROMPT_new_chat.md` added: paste into a fresh chat with the ZIP to run
  an independent hostile audit toward a straight-line paper.
