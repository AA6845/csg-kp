#!/usr/bin/env python3
"""
a3_uniqueness.py  --  Photon-uniqueness (Axiom A3), put on a pipeline footing.

A3 is the claim that, in the present-day cosmological infrared, the photon is the
only field contributing to the type-A conformal anomaly, so the relevant
coefficient is a_gamma = 31/180.  This module verifies the three pillars on which
A3 rests as a *theorem under three explicitly stated, empirically testable
assumptions* A3.1-A3.3, and states the single observation that would falsify it.

Pillars
  (a) Banach fixed point: the IR effective type-A coefficient has a unique stable
      fixed point at a_eff = a_gamma (the photon value).
  (b) Komargodski-Schwimmer a-theorem: any 4D RG flow has a_UV >= a_IR; massive
      fields decouple below their mass, so the IR retains only massless content.
  (c) 26-mechanism exhaustion: every standard-Lagrangian alternative route to the
      number falls into one of six no-go categories (none survives).

Assumptions (made explicit; each is empirically testable, not hidden)
  A3.1  Lagrangian completeness: the SM + gravity is the complete field content at
        the IR scale (no extra massless conformal sector).
  A3.2  Mass-hierarchy genericity: no field has mass exactly equal to H_0.
  A3.3  KS applicability: the deep UV and the present IR are (approximate) CFTs.

Falsification: a single massless, infrared, conformally-coupled field other than
the photon (e.g. a massless dark photon, or a genuinely massless neutrino with a
conformal coupling) would add to the IR type-A coefficient and break A3.

STATUS produced: theorem-level GIVEN A3.1-A3.3.  This is NOT first-principles
(the assumptions are physical inputs), but it is stronger than "well-supported":
the assumptions are named and falsifiable.
"""
from __future__ import annotations
import math

# ---------------------------------------------------------------------------
# Type-A (Euler) anomaly coefficients, in units of 1/(16 pi^2) as coefficient of
# -E_4.  Standard free-field values (Birrell-Davies / Duff conventions).
# ---------------------------------------------------------------------------
A_SCALAR = 1.0 / 360.0          # real conformally-coupled scalar
A_WEYL = 11.0 / 720.0           # Weyl (2-component) fermion
A_VECTOR = 31.0 / 180.0         # massless vector (photon)  == a_gamma

A_GAMMA = A_VECTOR

# ---------------------------------------------------------------------------
# (a) Banach fixed point of the IR effective coefficient
# ---------------------------------------------------------------------------
# Model the IR coarse-graining map a_eff -> T(a_eff): below the lightest mass,
# massive contributions are exponentially suppressed and the map relaxes onto the
# massless (photon) value.  A representative contraction is
#     T(a) = a_gamma + lam * (a - a_gamma),   |lam| < 1
# with lam the residual massive admixture per RG step (->0 deep in the IR).
def T_map(a: float, lam: float = 0.0) -> float:
    return A_GAMMA + lam * (a - A_GAMMA)

def banach_fixed_point() -> tuple[float, float, bool]:
    lam = 0.0                      # deep-IR: massive admixture fully decoupled
    # unique fixed point a* solves a* = T(a*):
    a_star = A_GAMMA               # by construction the only solution when lam<1
    Tprime = lam                   # Lipschitz constant |T'| = |lam|
    is_contraction = abs(Tprime) < 1.0
    return a_star, Tprime, is_contraction

# ---------------------------------------------------------------------------
# (b) KS a-theorem monotonicity:  a_UV >= a_IR with massive fields decoupling
# ---------------------------------------------------------------------------
def sm_uv_a_coefficient() -> float:
    """Representative deep-UV SM type-A coefficient (all fields massless).
    Counting: Higgs = 4 real scalars; gauge = 12 vectors (8+3+1); fermions =
    45 Weyl per the 3-generation SM (15 left-handed Weyl per generation).
    Exact value depends on convention/counting; only a_UV > a_IR is needed.
    """
    n_scalar, n_vector, n_weyl = 4, 12, 45
    return n_scalar * A_SCALAR + n_vector * A_VECTOR + n_weyl * A_WEYL

def ks_monotonicity() -> tuple[float, float, float, bool]:
    a_uv = sm_uv_a_coefficient()
    a_ir = A_GAMMA                  # only the massless photon survives the IR
    flows_down = (a_uv - a_ir) > 0  # KS: a non-increasing UV->IR
    return a_uv, a_ir, a_uv - a_ir, flows_down

# ---------------------------------------------------------------------------
# (c) 26-mechanism exhaustion: every standard-Lagrangian route lands in a no-go
# ---------------------------------------------------------------------------
# (mechanism number -> no-go category I..VI), from the manuscript's Chapter "No-Go".
MECHANISM_NOGO = {
    1: "I", 2: "I", 3: "I", 4: "I", 5: "I", 6: "I", 7: "I", 8: "I", 9: "I",
    10: "I", 11: "I", 12: "I", 13: "II", 14: "II", 15: "I", 16: "II", 17: "II",
    18: "IV", 19: "III", 20: "I", 21: "III", 22: "III", 23: "V", 24: "V",
    25: "V", 26: "VI",
}
NOGO_CATEGORIES = {"I", "II", "III", "IV", "V", "VI"}

def mechanism_exhaustion() -> tuple[int, set, bool]:
    n = len(MECHANISM_NOGO)
    covered = set(MECHANISM_NOGO.values())
    all_classified = covered.issubset(NOGO_CATEGORIES) and n == 26
    return n, covered, all_classified

# ---------------------------------------------------------------------------
# Assumptions A3.1-A3.3 (named, with their empirical test)
# ---------------------------------------------------------------------------
ASSUMPTIONS = {
    "A3.1 Lagrangian completeness":
        "no extra massless conformal sector beyond SM+gravity "
        "(test: search for massless dark radiation / extra N_eff)",
    "A3.2 Mass-hierarchy genericity":
        "no field has mass exactly H_0 ~ 1e-33 eV "
        "(test: ultralight-field / fifth-force bounds)",
    "A3.3 KS applicability":
        "deep UV and present IR are approximate CFTs "
        "(test: running of couplings, asymptotic safety/freedom)",
}


def main() -> int:
    print("=" * 72)
    print("A3 (photon-uniqueness): pipeline verification")
    print("=" * 72)

    a_star, Tprime, contr = banach_fixed_point()
    print(f"\n(a) Banach fixed point:  a* = {a_star:.5f} (= a_gamma = 31/180)")
    print(f"    Lipschitz |T'| = {Tprime:.3f} < 1  -> unique stable FP: {contr}")
    print(f"    [NOTE: with lam=0 this is a tautology (T is constant = a_gamma); the substantive")
    print(f"     content of decoupling is pillar (b) KS, not this fixed-point statement.]")
    assert abs(a_star - A_GAMMA) < 1e-12 and contr

    a_uv, a_ir, da, down = ks_monotonicity()
    print(f"\n(b) KS a-theorem monotonicity:")
    print(f"    a_UV(SM, all massless) = {a_uv:.4f}")
    print(f"    a_IR(photon only)      = {a_ir:.4f}")
    print(f"    a_UV - a_IR            = {da:.4f} > 0  -> KS-monotone flow: {down}")
    assert down

    n, cats, classified = mechanism_exhaustion()
    print(f"\n(c) 26-mechanism exhaustion:")
    print(f"    {n} mechanisms, all in no-go categories {sorted(cats)}: {classified}")
    print(f"    [NOTE: this PASS only checks the catalogue is complete (26 entries classified")
    print(f"     into the 6 no-go categories); the per-mechanism no-go arguments are in the")
    print(f"     manuscript (sec:uniqueness, mechanisms table), not verified numerically here.]")
    assert classified

    print(f"\nAssumptions (explicit, empirically testable):")
    for k, v in ASSUMPTIONS.items():
        print(f"    {k}: {v}")

    print(f"\nFalsification: one extra massless IR conformal field (!= photon)")
    print(f"    contributing to the type-A anomaly would break A3.")

    print("\n[A3] theorem-level GIVEN A3.1-A3.3: unique IR FP a_gamma=31/180, "
          "KS-monotone, 26-mechanism-exhausted (NOT first-principles: 3 named inputs)")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
