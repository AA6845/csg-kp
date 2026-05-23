#!/usr/bin/env python3
"""
cw_banach_iteration.py  --  The correct KP self-consistency on the full CW dynamics,
and why the kp_volume mean_R_over_4 proxy is geometrically inconsistent.

This module replaces the order-of-magnitude proxy in kp_volume_selfconsistency.py
(function mean_R_over_4) with the actual Coleman--Weinberg scalaron dynamics, and
records two findings honestly (both sides):

(A)  THE PROXY BUG (mean_R_over_4 in kp_volume_selfconsistency.py).
     That proxy builds a closed history from a CONSTANT positive Omega_Lambda plus a
     curvature term Ok chosen to force a turnaround H^2=0 at a_max.  But a closed
     universe with constant positive Omega_Lambda NEVER recollapses (Lambda drives
     eternal expansion).  Forcing the turnaround makes H^2 < 0 on 1 < a < a_max, which
     the proxy hides with max(H^2, 1e-30).  The resulting <R>/4 numbers (and the
     "de Sitter identity / tautology" they suggested) are ARTEFACTS of floored,
     unphysical geometry.  A real recollapse requires V(phi) < 0, not constant OL>0.

(B)  THE CORRECT DYNAMICS (FRW + Klein-Gordon with the CW potential).
     V(phi) = A v_S^4 psi^4 (2 ln psi - 25/6),  psi = phi/v_S, turns NEGATIVE below
     phi_crit = v_S e^{25/12} ~ 8.03 v_S, which is what powers recollapse.  Iterating
     the KP identity  Lambda* = (1/4) <R_m>_{V4},  R_m = rho_m/a^3 - phidot^2 + 4V,
     with -Lambda*/3 fed back into Friedmann (Banach fixed point), gives:
       * Lambda* is UNIVERSAL: independent of phi_0 AND of Omega_m (matter dilutes
         out of the V4-average).  The universality STRUCTURE is real.
       * BUT its value is AMPLITUDE-dependent (~ -0.10 for A_CW, ~ -0.002 for A_M5),
         NOT the manuscript's -0.69.
       * AND Omega_Lambda = (V(phi_0) - Lambda*)/3 is NOT fixed: it varies fully with
         phi_0.  KP self-consistency fixes Lambda* but leaves phi_0 (the scalaron value
         "today") free -> the absolute Omega_Lambda is not determined by this route.

  Consequence for the framework: the volume/self-consistency route delivers the
  universality STRUCTURE and the order of magnitude, but neither the sharp Lambda*
  nor the absolute Omega_Lambda.  The theorem-level, prior-free output remains the
  RATIO Omega_K/Omega_Lambda = a_gamma/8 pi^2 (unaffected by any of this).

Dependencies: numpy, scipy.  Imports A_GAMMA from csg_kp_core.
"""
from __future__ import annotations
import math
import os
import sys

import numpy as np
from scipy.integrate import solve_ivp

_HERE = os.path.dirname(os.path.abspath(__file__))
_PARENT = os.path.dirname(_HERE)
for p in (_HERE, _PARENT):
    if p not in sys.path:
        sys.path.insert(0, p)

from csg_kp_core import A_GAMMA  # noqa: E402

V_S = 1.0
A_CW = A_GAMMA / (128 * math.pi ** 2)          # CW amplitude used in the fixed point
A_M5 = A_GAMMA ** 2 / (16 * math.pi ** 2) ** 2  # manuscript M5 amplitude (~115x smaller)
PHI_CRIT = V_S * math.exp(25.0 / 12.0)          # ~ 8.03 v_S: V(phi) turns negative below


def V(phi, A):
    p = np.maximum(phi / V_S, 1e-9)
    return A * V_S ** 4 * p ** 4 * (2 * np.log(p) - 25.0 / 6.0)


def dV(phi, A):
    p = np.maximum(phi / V_S, 1e-9)
    return A * V_S ** 3 * p ** 3 * (8 * np.log(p) - 44.0 / 3.0)


# ---------------------------------------------------------------------------
# (A) The proxy bug: constant OL>0 + forced turnaround => H^2 < 0
# ---------------------------------------------------------------------------
def proxy_H2_min(OL: float, a_max: float) -> float:
    """Minimum of the *unfloored* H^2 over 1<a<a_max for the kp_volume proxy
    (constant OL plus Ok forcing H^2=0 at a_max).  Negative => unphysical."""
    Om = 1 - OL
    Ok = (Om * a_max ** -3 + OL) * a_max ** 2     # forces H^2=0 at a_max
    a = np.linspace(1.0, a_max * (1 - 1e-6), 4000)
    H2 = Om * a ** -3 + OL - Ok * a ** -2          # NO floor here
    return float(H2.min())


# ---------------------------------------------------------------------------
# (B) The correct CW dynamics: FRW + Klein-Gordon, KP Banach fixed point
# ---------------------------------------------------------------------------
def Rm_average(phi0: float, A: float, Om: float, Lam: float):
    """V4-weighted <R_m> over the closed CW history, with -Lam/3 fed into Friedmann.
    Returns (<R_m>, a_max)."""
    rho_m0 = 3 * Om

    def rhs(t, z):
        a, adot, phi, phidot = z
        Va = V(phi, A)
        add = a * (-(1.0 / 6.0) * (rho_m0 / a ** 3 + 2 * phidot ** 2 - 2 * Va) - Lam / 3.0)
        return [adot, add, phidot, -3 * (adot / a) * phidot - dV(phi, A)]

    eva = lambda t, z: z[0] - 1e-2; eva.terminal = True; eva.direction = -1
    evp = lambda t, z: z[2] - 0.3;  evp.terminal = True; evp.direction = -1
    segs = {}
    for d, tag in [(+1, 'fwd'), (-1, 'bwd')]:
        segs[tag] = solve_ivp(rhs, [0, d * 1e6], [1.0, 1.0, phi0, 0.0],
                              events=[eva, evp], max_step=0.12, rtol=1e-7, atol=1e-10)
    t = np.concatenate([segs['bwd'].t[::-1], segs['fwd'].t])
    y = np.concatenate([segs['bwd'].y[:, ::-1], segs['fwd'].y], axis=1)
    a, adot, phi, phidot = y
    Rm = rho_m0 / a ** 3 - phidot ** 2 + 4 * V(phi, A)
    w = a ** 3
    return float(np.trapezoid(Rm * w, t) / np.trapezoid(w, t)), float(a.max())


def banach(phi0: float, A: float, Om: float, n_iter: int = 12):
    """KP fixed point Lambda* = (1/4)<R_m>(Lambda*).  Returns (Lambda*, OmL_pred, a_max)."""
    Lam = -0.1
    amx = float('nan')
    for _ in range(n_iter):
        Rm, amx = Rm_average(phi0, A, Om, Lam)
        Lnew = 0.25 * Rm
        if abs(Lnew - Lam) < 1e-4:
            Lam = Lnew
            break
        Lam = 0.5 * Lam + 0.5 * Lnew
    OmL = (V(phi0, A) - Lam) / 3.0
    return Lam, OmL, amx


def main() -> int:
    print("=" * 72)
    print("Correct CW Banach iteration vs the kp_volume mean_R_over_4 proxy")
    print("=" * 72)

    print(f"\nZE1  CW potential turns negative below phi_crit = v_S e^(25/12) = {PHI_CRIT:.4f} v_S")
    print(f"     A_CW = a_g/128pi^2 = {A_CW:.4e};  A_M5 = a_g^2/(16pi^2)^2 = {A_M5:.4e}"
          f"  (ratio {A_CW / A_M5:.0f}x)")
    assert V(PHI_CRIT * 0.9, A_CW) < 0 < V(PHI_CRIT * 1.5, A_CW)   # sign change at phi_crit

    print("\nZE2  PROXY BUG: constant OL>0 + forced turnaround => H^2<0 (floored, unphysical):")
    print("      OL    a_max     min(H^2, unfloored)   verdict")
    for OL, amx in [(0.685, 1.5), (0.685, 3.0), (0.685, 100.0)]:
        h2 = proxy_H2_min(OL, amx)
        print(f"     {OL:.3f}  {amx:7.1f}    {h2:+.4e}        "
              f"{'UNPHYSICAL (H^2<0)' if h2 < 0 else 'ok'}")
    # the proxy geometry is unphysical for every a_max>1 with constant OL>0
    assert proxy_H2_min(0.685, 3.0) < 0
    assert proxy_H2_min(0.685, 100.0) < 0
    print("     => mean_R_over_4 integrates floored H^2; its <R>/4 values are artefacts.")

    print("\nZE3  CORRECT dynamics: is Lambda* universal in phi_0?  (A_CW, Om=0.315)")
    print("      phi_0     Lambda*     OmL_pred=(V(phi0)-Lam)/3     a_max")
    lams = []
    for phi0 in [9.0, 10.0]:
        Lam, OmL, amx = banach(phi0, A_CW, 0.315)
        lams.append(Lam)
        print(f"     {phi0:5.1f}    {Lam:8.4f}    {OmL:8.4f}                  {amx:8.1f}")
    # Lambda* universal across phi_0; OmL_pred is NOT (varies with phi_0)
    assert max(lams) - min(lams) < 0.02, f"Lambda* not universal: spread {max(lams)-min(lams)}"

    print("\nZE4  Universality also in Omega_m (phi_0=9, A_CW):")
    lams_m = []
    for Om in [0.27, 0.35]:
        Lam, OmL, amx = banach(9.0, A_CW, Om)
        lams_m.append(Lam)
        print(f"     Om={Om:.3f}:  Lambda*={Lam:.4f}  OmL_pred={OmL:.4f}  a_max={amx:.1f}")
    assert max(lams_m) - min(lams_m) < 0.02, "Lambda* not universal in Om"
    print("     => matter dilutes out of the V4-average: Lambda* universal in phi_0 AND Om.")

    Lam_mean = float(np.mean(lams))
    print("\nZE5  But the VALUE is amplitude-dependent and the absolute scale is NOT fixed:")
    print(f"     A_CW: Lambda* ~ {Lam_mean:.4f}  (NOT the manuscript's -0.69)")
    print("     OmL_pred = (V(phi0)-Lambda*)/3 varies fully with phi_0 -> phi_0 stays free.")
    # sanity: Lambda* is order -0.1 for A_CW, not -0.69
    assert -0.2 < Lam_mean < -0.03

    print("\nVERDICT (both sides):")
    print("  - the proxy mean_R_over_4 is geometrically inconsistent (floored H^2<0);")
    print("    its 'de Sitter identity/tautology' was an artefact -> retracted.")
    print("  - the correct CW dynamics give a UNIVERSAL Lambda* (real structure), but")
    print("    its value is amplitude-set and the absolute Omega_Lambda (phi_0) is free.")
    print("  - unaffected: the theorem-level ratio Omega_K/Omega_Lambda = a_gamma/8pi^2.")
    print("\n[cw-banach] mean_R_over_4 floored-geometry bug documented; correct dynamics give")
    print("            universal Lambda* (structure) but free phi_0 -> absolute scale open")
    return 0


if __name__ == "__main__":
    sys.exit(main())
