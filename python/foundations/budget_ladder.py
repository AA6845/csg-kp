#!/usr/bin/env python3
"""
budget_ladder.py  --  The geometric 2^n pi^2 ladder linking Omega_Lambda, Omega_K.

This module records a structural observation about the cosmic budget that the
manuscript's central ratio Omega_K/Omega_Lambda = a_gamma/(8 pi^2) sits inside.
It is presented HONESTLY: the geometric ladder (the relations among the numbers)
is exact and forced; the *physical identification* of the leading term with the
dark-energy fraction is a CONJECTURE with one explicit open step (see STATUS).

--------------------------------------------------------------------------------
The ladder (all factors are 2^n pi^2 of 4D conformal geometry):

    16 pi^2 = 2^4 pi^2   one-loop factor in  <T> = a_gamma E_4 / 16 pi^2
    32 pi^2 = 2^5 pi^2   = int_{D^4} E_4   (observer hemisphere, chi = 1)
    64 pi^2 = 2^6 pi^2   = int_{S^4} E_4   (full no-boundary sphere, chi = 2)

The three budget quantities, all from a_gamma and the Euler integrals:

    Omega_Lambda          = int_{S^4} <T> sqrt(g) = 4 a_gamma          (leading, a_g^1)
    Omega_K / Omega_Lambda = 4 a_gamma / int_{D^4} E_4 = a_gamma/8 pi^2 (ratio,   a_g^1)
    Omega_K               = Omega_Lambda^2 / int_{D^4} E_4 = a_gamma^2/2 pi^2 (sub,  a_g^2)

The SAME numerator 4 a_gamma appears in Omega_Lambda and in the ratio's numerator;
dividing by int_{D^4} E_4 = 32 pi^2 turns the full-sphere anomaly into the cap
ratio.  Hence the exact algebraic identity

    Omega_K * (32 pi^2) = Omega_Lambda^2 .

PERTURBATION HIERARCHY (the content reason |Omega_K| << Omega_Lambda):
  dark energy is the LEADING anomaly effect (~ a_gamma^1); curvature is a
  SECOND-ORDER effect (~ a_gamma^2).  The smallness of curvature is therefore
  structural, not a tuning.  This mirrors the holographic V_4 = A_2^2 relation
  (4-volume = area^2, manuscript Z.6087): Omega_K is to Omega_Lambda as a
  quadratic is to a linear quantity.

GEOMETRY split (consistent with the observer framing):
  full S^4  (timeless no-boundary substrate)  -> absolute Omega_Lambda
  hemisphere D^4 (observer past light cone)    -> the ratio Omega_K/Omega_Lambda
  the factor 32 pi^2 = int_{D^4} E_4 is the substrate -> observer bridge.

--------------------------------------------------------------------------------
STATUS  (read before citing this):
  EXACT / forced:
    - the algebraic ladder  Omega_K * 32 pi^2 = Omega_Lambda^2  given the two
      identifications below;
    - the factor 32 pi^2 = int_{D^4} E_4 is geometric, not a free normalization;
    - Omega_K/Omega_Lambda = a_gamma/8 pi^2 is the manuscript's theorem-level ratio.
  CONJECTURE / open (the one non-derived step):
    - the IDENTIFICATION  Omega_Lambda = int_{S^4} <T> sqrt(g) = 4 a_gamma, i.e.
      the dark-energy density FRACTION equals the integrated anomaly ACTION on the
      full sphere.  The local energy-density route (rho_anom/rho_crit * N_eff,
      see the de Sitter identity) yields only the RATIO a_gamma/8 pi^2, NOT 4 a_gamma.
      So 4 a_gamma = Omega_Lambda needs an ACTION/topological identification of the
      dark energy, which A5 does not (yet) provide -- A5 establishes only the ratio.
    - This is also in tension with A5/C1 (KP sequestering closes the Lambda-channel):
      Omega_Lambda = 4 a_gamma would require the full-S^4 substrate vacuum (NOT the
      cap anomaly) to appear as DE, i.e. two separate channels.
  So the numerical match Omega_Lambda = 4 a_gamma = 0.6889 ~ Planck is striking and
  the ladder is coherent, but it is a CONJECTURE pending the action-identification
  bridge, not a proven prediction of the absolute scale.

Dependencies: numpy.  Imports A_GAMMA from csg_kp_core.
"""
from __future__ import annotations
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_PARENT = os.path.dirname(_HERE)
for p in (_HERE, _PARENT):
    if p not in sys.path:
        sys.path.insert(0, p)

from csg_kp_core import A_GAMMA  # noqa: E402

PI2 = math.pi ** 2

# Euler integrals (Gauss-Bonnet) -- geometric, not free
INT_E4_D4 = 32 * PI2          # hemisphere D^4, chi = 1
INT_E4_S4 = 64 * PI2          # full sphere S^4, chi = 2  (= 2 * int_{D^4})
LOOP = 16 * PI2               # one-loop factor in <T>

# Planck 2018 base-LCDM (TT,TE,EE+lowE+lensing+BAO), VI Table 2
PLANCK_OL, PLANCK_OL_S = 0.6889, 0.0056
PLANCK_OM, PLANCK_OM_S = 0.3111, 0.0056


def omega_lambda_ladder() -> float:
    """Leading term: the full-S^4 integrated anomaly  int<T> = 4 a_gamma."""
    return A_GAMMA / LOOP * INT_E4_S4          # = a_g/16pi^2 * 64pi^2 = 4 a_g


def omega_k_over_lambda() -> float:
    """The cap ratio = 4 a_gamma / int_{D^4} E_4 = a_gamma / 8 pi^2."""
    return (4 * A_GAMMA) / INT_E4_D4           # = a_g / 8 pi^2


def omega_k_ladder() -> float:
    """Subleading: Omega_Lambda^2 / int_{D^4} E_4 = a_gamma^2 / 2 pi^2."""
    OL = omega_lambda_ladder()
    return OL ** 2 / INT_E4_D4                 # = (4a_g)^2/32pi^2 = a_g^2/2pi^2


def pull(pred: float, obs: float, sig: float) -> float:
    return (pred - obs) / sig


def main() -> int:
    print("=" * 72)
    print("Geometric budget ladder: Omega_Lambda, Omega_K from a_gamma and int E_4")
    print("=" * 72)

    print("\nZE1  The 2^n pi^2 ladder of 4D conformal geometry:")
    print(f"     16 pi^2 = 2^4 pi^2 = {LOOP:8.3f}   one-loop factor in <T>=a_g E_4/16pi^2")
    print(f"     32 pi^2 = 2^5 pi^2 = {INT_E4_D4:8.3f}   = int E_4 on D^4 (hemisphere, chi=1)")
    print(f"     64 pi^2 = 2^6 pi^2 = {INT_E4_S4:8.3f}   = int E_4 on S^4 (sphere, chi=2)")
    assert abs(INT_E4_S4 - 2 * INT_E4_D4) < 1e-9          # sphere = 2 hemispheres
    assert abs(INT_E4_D4 - 2 * LOOP) < 1e-9               # 32pi^2 = 2*16pi^2

    OL = omega_lambda_ladder()
    rK = omega_k_over_lambda()
    OK = omega_k_ladder()
    Om = 1 - OL - OK
    print("\nZE2  The three budget quantities (all from a_gamma + Euler integrals):")
    print(f"     Omega_Lambda          = int<T>(S^4)         = 4 a_g       = {OL:.4f}")
    print(f"     Omega_K/Omega_Lambda  = 4a_g/int E_4(D^4)   = a_g/8pi^2   = {rK:.4e}")
    print(f"     Omega_K               = Omega_L^2/int E_4(D^4)= a_g^2/2pi^2= {OK:.4e}")
    print(f"     Omega_m = 1-Omega_L-Omega_K                              = {Om:.4f}")
    # exact algebraic identities of the ladder
    assert abs(OL - 4 * A_GAMMA) < 1e-12
    assert abs(rK - A_GAMMA / (8 * PI2)) < 1e-12
    assert abs(OK - A_GAMMA ** 2 / (2 * PI2)) < 1e-12
    assert abs(OK * INT_E4_D4 - OL ** 2) < 1e-12          # Omega_K*32pi^2 = Omega_L^2
    assert abs(OK - rK * OL) < 1e-12                      # ratio consistency

    print("\nZE3  Exact ladder identity  Omega_K * 32 pi^2 = Omega_Lambda^2:")
    print(f"     {OK * INT_E4_D4:.6f} = {OL ** 2:.6f}   [check]")

    print("\nZE4  Perturbation hierarchy in a_gamma (why |Omega_K| << Omega_Lambda):")
    print(f"     Omega_Lambda ~ a_g^1 (leading)    = 4 a_g       = {OL:.4f}")
    print(f"     Omega_K      ~ a_g^2 (subleading) = a_g^2/2pi^2 = {OK:.4e}")
    print(f"     ratio        ~ a_g^1              = a_g/8pi^2   = {rK:.4e}")
    print("     -> curvature is 2nd order in the anomaly: structural, not a tuning.")

    print("\nZE5  Full budget vs Planck 2018 (base-LCDM):")
    print(f"     Omega_Lambda: pred {OL:.4f}  obs {PLANCK_OL:.4f}+-{PLANCK_OL_S:.4f}"
          f"  -> {pull(OL, PLANCK_OL, PLANCK_OL_S):+.2f} sigma")
    print(f"     Omega_m:      pred {Om:.4f}  obs {PLANCK_OM:.4f}+-{PLANCK_OM_S:.4f}"
          f"  -> {pull(Om, PLANCK_OM, PLANCK_OM_S):+.2f} sigma")
    print(f"     |Omega_K|:    pred {OK:.4e}  obs |Om_K|<2e-3 (consistent)")
    # the match must be within ~1 sigma to be worth recording (sanity, both sides)
    assert abs(pull(OL, PLANCK_OL, PLANCK_OL_S)) < 1.0
    assert abs(pull(Om, PLANCK_OM, PLANCK_OM_S)) < 1.0

    print("\nSTATUS (zero confirmation bias -- both sides):")
    print("  EXACT/forced : the ladder algebra (Omega_K*32pi^2=Omega_L^2); 32pi^2=int E_4(D^4)")
    print("                 is geometric; the ratio a_g/8pi^2 is theorem-level.")
    print("  CONJECTURE   : Omega_Lambda = int<T>(S^4) = 4 a_g. The local energy-density")
    print("                 route gives only the RATIO a_g/8pi^2, not 4 a_g. The absolute")
    print("                 DE = full-S^4 anomaly ACTION is NOT derived (A5 gives the ratio")
    print("                 only) and is in tension with A5/C1 (Lambda-channel sequestering).")
    print("  -> coherent geometric structure + exact Planck match, but the absolute scale")
    print("     rests on the open action-identification bridge; NOT a proven prediction.")
    print("\n[budget-ladder] Omega_L=4a_g leading, Omega_K=a_g^2/2pi^2 subleading, joined by")
    print("                int E_4(D^4)=32pi^2; ladder exact, DE action-identification open")
    return 0


if __name__ == "__main__":
    sys.exit(main())
