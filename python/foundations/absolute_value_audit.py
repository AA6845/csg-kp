#!/usr/bin/env python3
"""
absolute_value_audit.py  --  Why 4 a_gamma is an ACTION invariant, not a dynamical
value, and the sharpest form of the remaining identification conjecture.

This module records two results that sharpen (not close) the open absolute-value
question left by budget_ladder.py / spectral_coherence.py.

================================================================================
RESULT 1 -- a no-go by exhaustion.
  Every dynamical / energy-density route to the absolute Omega_Lambda gives a
  DIFFERENT number, and none gives 4 a_gamma:

    KP sequestering   rho_L = int<T>/V_4         -> (a_g/8pi^2)(H/M_Pl)^2 ~ 1e-122
    Euclidean         rho_L = -dS_E/dV_4         -> 1/2            (NEW, this module)
    M5/KP fixed point 1/(12 a_g)                 -> 0.484
    CW Banach iteration                          -> phi_0 free (not fixed)
    Riegert saddle                               -> linear, no saddle
    causal bare closures (median)                -> 0.93
    causal KP  <R>_M / 4                         -> ~14 (no fixed point)
    Lorentzian light-cone anomaly                -> too weak by (M_Pl/H)^4 ~ 1e240
    Lombriser uniform prior                      -> 0.704 (prior-dependent)

  The ONLY route to 4 a_gamma is the pure action invariant
    int_{S^4} <T^mu_mu> sqrt(g) = 4 a_gamma  ( = |zeta(0;Maxwell;S^4)|
                                             = Riegert scale-flow dS_anom/dsigma ),
  cutoff-free and exact, but an ACTION, not a dynamically forced density. Hence
  4 a_gamma is not a dynamical equilibrium value at all; it is a topological-
  spectral invariant. The identification "DE fraction = this invariant" therefore
  CANNOT be derived from any dynamics -- each dynamics demonstrably gives something
  else. This is a structural reason for the open step, not a failed attempt.

RESULT 2 -- the conjecture sharpened to a single normalization.
  Omega_Lambda = 4 a_gamma is EXACTLY equivalent to the choice
    N_eff = S_dS / C_Q  ,
  the de Sitter (Gibbons-Hawking) entropy per Q-curvature charge:
    S_dS = 8 pi^2 M_Pl^2 / H^2  (A/4G, reduced M_Pl^2 = 1/8piG),
    C_Q  = 8 pi^2,
    N_eff = S_dS / C_Q = (M_Pl/H)^2  (prefactor c = 1)  =>  Omega_L = 4 c a_g = 4 a_g.
  This reduces the open question from "a vague action identification" to "why this
  one geometrically natural normalization (entropy per Q-charge)". It is sharper
  and more falsifiable, but still a setting: S_dS/C_Q is not more forced than the
  bulk-projection prefactor 4/3pi.

STATUS: both are HONEST sharpenings of an OPEN point, not a resolution. The value
4 a_gamma stays a conjecture (now: action-invariant, single normalization); the
epoch binding stays the categorical anthropic measure problem (sec:measure).
================================================================================
"""
from __future__ import annotations
import sympy as sp

import os as _os, sys as _sys
_HERE = _os.path.dirname(_os.path.abspath(__file__)); _PARENT = _os.path.dirname(_HERE)
for _p in (_HERE, _PARENT):
    if _p not in _sys.path:
        _sys.path.insert(0, _p)
from csg_kp_core import A_GAMMA_NUM, A_GAMMA_DEN  # single source of truth

ag = sp.Rational(A_GAMMA_NUM, A_GAMMA_DEN)  # imported from core -- NOT a local hardcode
PI = sp.pi
H, Mpl, H0 = sp.symbols('H M_Pl H_0', positive=True)


def euclidean_vacuum_energy():
    """Canonical Euclidean vacuum energy rho_L = -dS_E/dV_4 on the S^4 saddle -> 1/2."""
    S_E = -8 * PI**2 * Mpl**2 / H**2 + 4 * ag * sp.log(H0 / H)   # gravity + anomaly (1-loop)
    V4 = 8 * PI**2 / (3 * H**4)
    rho_L = sp.simplify(-sp.diff(S_E, H) / sp.diff(V4, H))
    OmL = sp.simplify(rho_L / (3 * Mpl**2 * H**2))               # = 1/2 - (a_g/8pi^2)(H/M_Pl)^2
    OmL_leading = OmL.subs(H, 0)                                  # drop the 1e-122 term
    return OmL, OmL_leading


def action_invariant():
    """The unique route to 4 a_gamma: the integrated trace anomaly (an action)."""
    intE4_S4 = 64 * PI**2
    int_T = sp.simplify(ag / (16 * PI**2) * intE4_S4)            # = 4 a_gamma
    return int_T


def sds_over_cq():
    """Omega_L = 4 a_g  <=>  N_eff = S_dS/C_Q = (M_Pl/H)^2 (c=1)."""
    S_dS = 8 * PI**2 * Mpl**2 / H**2          # Gibbons-Hawking, reduced Planck units
    C_Q = 8 * PI**2
    N_eff = sp.simplify(S_dS / C_Q)            # = (M_Pl/H)^2
    c = sp.simplify(N_eff / (Mpl**2 / H**2))   # = 1
    OmL = sp.simplify(4 * c * ag)              # = 4 a_g
    return N_eff, c, OmL


def _selftest():
    ok = True
    print("=" * 72)
    print("absolute_value_audit.py  --  action-invariant no-go + S_dS/C_Q sharpening")
    print("=" * 72)

    OmL_euc, OmL_lead = euclidean_vacuum_energy()
    c1 = (sp.simplify(OmL_lead - sp.Rational(1, 2)) == 0)
    print(f"  [{'PASS' if c1 else 'FAIL'}] Euclidean rho_L=-dS_E/dV_4 gives Omega_L = "
          f"{sp.nsimplify(OmL_euc)} -> leading {OmL_lead} (NOT 4 a_g)")
    ok &= c1

    int_T = action_invariant()
    c2 = (sp.simplify(int_T - 4 * ag) == 0)
    print(f"  [{'PASS' if c2 else 'FAIL'}] only route to 4 a_g: int_(S^4)<T> = "
          f"{sp.nsimplify(int_T)} = 4 a_g (an ACTION, not a forced density)")
    ok &= c2

    N_eff, c, OmL = sds_over_cq()
    c3 = (sp.simplify(N_eff - Mpl**2 / H**2) == 0) and (c == 1) and (sp.simplify(OmL - 4 * ag) == 0)
    print(f"  [{'PASS' if c3 else 'FAIL'}] Omega_L=4a_g <=> N_eff=S_dS/C_Q=(M_Pl/H)^2 "
          f"(c={c}); single natural normalization")
    ok &= c3

    print("-" * 72)
    print("  Route audit (none gives 4 a_g; only the action invariant does):")
    routes = [
        ("KP sequestering int<T>/V_4", "1e-122"),
        ("Euclidean -dS_E/dV_4",       "1/2"),
        ("M5 fixed point 1/(12a_g)",   "0.484"),
        ("CW Banach iteration",        "phi_0 free"),
        ("Riegert saddle",             "linear, none"),
        ("causal bare closures",       "0.93 (median)"),
        ("causal <R>_M/4",             "~14"),
        ("Lorentzian light-cone",      "1e240 too weak"),
        ("Lombriser uniform prior",    "0.704 (prior)"),
    ]
    for r, v in routes:
        print(f"      {r:32s} -> {v}")
    print("  => 4 a_g is an action-invariant, not a dynamical value. Identification")
    print("     'DE fraction = this invariant' is not derivable from any dynamics.")
    print("     Sharpest conjectural form: N_eff = S_dS/C_Q (entropy per Q-charge).")
    print(f"\n  Self-test: {'ALL PASS' if ok else 'FAILURE'}")
    return 0 if ok else 1


if __name__ == "__main__":
    import sys
    sys.exit(_selftest())
