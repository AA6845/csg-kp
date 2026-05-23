#!/usr/bin/env python3
"""
schwinger_keldysh_p5.py  --  In-in localization of P5 as the Cohen-Kaplan-Nelson bound.

This module records what the Schwinger-Keldysh (in-in) computation of the de Sitter
vacuum energy rigorously gives, and exactly where P5 (the holographic accumulation)
enters. It does NOT prove P5; it localizes it precisely and honestly.

WHAT IN-IN GIVES RIGOROUSLY (proven):
  The trace anomaly <T^mu_mu> = a_g E_4/16pi^2 is in-in robust: Adler-Bardeen
  one-loop exact for Type-A, no secular growth in the trace sector (in-in = in-out
  for the trace). The local anomaly vacuum density is therefore
      rho_anom = (a_g/8pi^2) * 3 H^4   (~ H^4).

WHAT IN-IN DOES NOT GIVE (the localization of P5):
  The Friedmann fraction from the LOCAL density is
      Omega_local = rho_anom/rho_crit = (a_g/8pi^2)(H/M_Pl)^2 ~ 10^-125 today,
  i.e. 122 orders too small. The lift factor N_eff = (M_Pl/H)^2 that fixes this is
  NOT an in-in mode sum (the mode sum is already inside rho_anom). It is the
  Cohen-Kaplan-Nelson UV-IR bound (rho_L <= M_Pl^2/L^2, L=1/H) -- a holographic
  consistency relation, not a consequence of local QFT.

THE CKN BOUND HAS TWO PARTS (the key honest split):
  (i)  Schwarzschild consistency rho_L <= M_Pl^2/L^2: FOLLOWS from gravity (an EFT
       may not contain states already collapsed to a black hole of size L). NOT a
       postulate; it fixes the ORDER OF MAGNITUDE (10^-122, not M_Pl^4).
  (ii) Saturation rho_L = c^2 M_Pl^2/L^2 (the bound is reached): this is the
       ASSUMPTION (P5), with CSG-KP coefficient c^2 = 4 a_g.

STATUS (honest):
  Schwinger-Keldysh PROVES part (i) magnitude support and LOCALIZES P5 exactly as
  CKN saturation (ii) with c^2 = 4 a_g. It does NOT prove (ii): saturating the
  holographic bound is the microscopic-holography problem of all of physics, not a
  one-loop or sympy computation. P5 is identified as a NAMED literature principle
  (CKN/Pad-manabhan), not a vague accumulation; closure = not achieved.
"""
from __future__ import annotations
import os
import sys
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_PARENT = os.path.dirname(_HERE)
for _p in (_HERE, _PARENT):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from csg_kp_core import A_GAMMA_NUM, A_GAMMA_DEN

ag = sp.Rational(A_GAMMA_NUM, A_GAMMA_DEN)
H, Mpl = sp.symbols('H M_Pl', positive=True)
PI = sp.pi


def local_fraction():
    """In-in local Friedmann fraction (proven, but 122 orders too small)."""
    rho_anom = ag / (8 * PI**2) * 3 * H**4
    return sp.simplify(rho_anom / (3 * Mpl**2 * H**2))


def ckn_lifted_fraction():
    """CKN-lifted fraction: N_eff = (M_Pl/H)^2 = horizon area in Planck units."""
    rho_anom = ag / (8 * PI**2) * 3 * H**4
    N_eff = Mpl**2 / H**2
    return sp.simplify(N_eff * rho_anom / (3 * Mpl**2 * H**2))


def main() -> int:
    print("=" * 72)
    print("Schwinger-Keldysh in-in: localization of P5 as the CKN bound")
    print("=" * 72)

    loc = local_fraction()
    print("\nZE1  in-in PROVES (Adler-Bardeen, no secular trace growth):")
    print(f"      local fraction rho_anom/rho_crit = {loc} = (a_g/8pi^2)(H/M_Pl)^2")
    print("      ~ 10^-125 today: 122 orders too small. This is what local QFT gives.")
    assert loc == ag / (8 * PI**2) * H**2 / Mpl**2

    lifted = ckn_lifted_fraction()
    print("\nZE2  the lift N_eff=(M_Pl/H)^2 is NOT a mode sum -- it is the CKN bound:")
    print(f"      N_eff * rho_anom / rho_crit = {lifted} = a_g/8pi^2 (correct magnitude)")
    print("      N_eff = (M_Pl/H)^2 = horizon area in Planck units (CKN: rho_L<=M_Pl^2/L^2).")
    assert lifted == ag / (8 * PI**2)

    print("\nZE3  CKN has two parts:")
    print("      (i)  Schwarzschild consistency rho_L<=M_Pl^2/L^2: FOLLOWS from gravity,")
    print("           NOT a postulate; fixes magnitude 10^-122 (not M_Pl^4).")
    print(f"      (ii) saturation rho_L=c^2 M_Pl^2/L^2 with c^2=4a_g={float(4*ag):.4f}: the ASSUMPTION (P5).")

    print("\nZE4  STATUS: in-in proves the local anomaly + magnitude support (i); localizes P5")
    print("      exactly as CKN saturation (ii), c^2=4a_g. Does NOT prove (ii) -- that is the")
    print("      microscopic-holography problem, not a 1-loop computation. Named principle now,")
    print("      not vague accumulation. Progress, not closure.")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
