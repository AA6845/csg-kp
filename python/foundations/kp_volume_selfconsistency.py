#!/usr/bin/env python3
"""
kp_volume_selfconsistency.py  --  The KP four-volume route to the absolute scale.

Theorem 64 (KP self-consistency) fixes Lambda* through a four-volume average, NOT
through the causal Shaw-Barrow relation.  This module carries the volume route and
makes its mechanism, its strength, and its one residual input explicit.

Three facts, each asserted:

  (1) TOPOLOGICAL CONSTRAINT (manuscript Eq. for A2):
        Lambda_eff * V_4 = int <T^mu_mu> sqrt(g) d^4x = 4 a_gamma .
      The right-hand side is the Euler/Gauss-Bonnet integral on S^4
      (int E_4 = 32 pi^2 chi(S^4) = 64 pi^2), hence TOPOLOGICAL and
      a_max-INVARIANT.  The bulk vacuum energy cancels (sequestering): this is
      what removes the 10^122 hierarchy without anthropics.

  (2) CATEGORY-ERROR FIX (Theorem 64, step 3 averages rho_total, not rho_m):
        <rho_total>_V4 = <rho_m>_V4 + <rho_phi>_V4 .
      <rho_m> ~ 1/a_max^3 -> 0 (dilutes), but <rho_phi> -> V_plateau (the scalaron
      potential does NOT dilute) -> <rho_total> is a_max-STABLE.  Averaging rho_m
      alone (the earlier mistake) wrongly gave Lambda*~0.

  (3) SHARPNESS vs the de Sitter identity  --  *** DEPRECATED PROXY ***.
      The function mean_R_over_4 below builds a closed history from a CONSTANT
      positive Omega_Lambda plus a curvature term Ok that forces H^2=0 at a_max.
      But constant OL>0 NEVER recollapses, so this makes H^2<0 on 1<a<a_max, which
      the proxy hides with max(H^2,1e-30).  Its <R>/4 numbers (and the "de Sitter
      identity / tautology" they suggested) are ARTEFACTS of floored geometry.
      The correct treatment (real recollapse needs V(phi)<0) is in
      foundations/cw_banach_iteration.py, which shows Lambda* is universal but its
      value is amplitude-set and the absolute Omega_Lambda (phi_0) stays free.
      The proxy is kept here only so its (artefactual) behaviour is reproducible;
      do NOT read a sharp Lambda* off it.

What is unconditionally derived (the falsifiability advantage of CSG-KP over
Lombriser's y=1/2): the *ratio* Omega_K/Omega_Lambda = a_gamma/(8 pi^2) is
theorem-level and prior-free.  The absolute scale is NOT delivered by this route:
the correct CW dynamics (foundations/cw_banach_iteration.py) give a Lambda* that is
universal in phi_0 and Omega_m (structure) but amplitude-set, with phi_0 -- hence the
absolute Omega_Lambda -- left free.  The topological constraint Lambda_eff V_4 = 4 a_g
and the a_max-stable total average are solid; the sharp value and the absolute scale
are not delivered by this route (see cw_banach_iteration.py).
"""
from __future__ import annotations
import math
import os
import sys

import numpy as np
from scipy.integrate import quad

_HERE = os.path.dirname(os.path.abspath(__file__))
_PARENT = os.path.dirname(_HERE)
for p in (_HERE, _PARENT):
    if p not in sys.path:
        sys.path.insert(0, p)

from csg_kp_core import A_GAMMA, C_Q  # noqa: E402


# ---------------------------------------------------------------------------
# (1) Topological KP constraint:  int_{S^4} <T> sqrt(g) = 4 a_gamma  (a_max-free)
# ---------------------------------------------------------------------------
def anomaly_integral() -> tuple[float, float]:
    """int_{S^4} E_4 sqrt(g) = 32 pi^2 chi(S^4) = 64 pi^2; <T>=a_g E_4/16pi^2
    integrates to 4 a_gamma.  Both are topological (independent of the radius,
    hence of a_max)."""
    chi_S4 = 2
    int_E4 = 32 * math.pi ** 2 * chi_S4              # = 64 pi^2
    int_T = A_GAMMA / (16 * math.pi ** 2) * int_E4   # = 4 a_gamma
    return int_E4, int_T


# ---------------------------------------------------------------------------
# (2) Category-error fix: <rho_total> is a_max-stable, <rho_m> is not
# ---------------------------------------------------------------------------
def _cycloid_average(a_max: float, rho_of_a) -> float:
    """V4-weighted average of rho_of_a(a) over a closed (cycloid) history,
    normalized so a=1 'today' on the rising branch."""
    eta = np.linspace(1e-4, 2 * math.pi - 1e-4, 200000)
    A = a_max / 2.0
    a = A * (1 - np.cos(eta))
    half = len(a) // 2
    it = int(np.argmin(np.abs(a[:half] - 1.0)))
    s = 1.0 / a[it]
    a = a * s
    dt = A * (1 - np.cos(eta))           # dt/d eta
    w = a ** 3 * dt                      # V4 weight
    rho = rho_of_a(a)
    return float(np.trapezoid(rho * w, eta) / np.trapezoid(w, eta))


def avg_rho_m(a_max: float, rho_m0: float = 1.0) -> float:
    return _cycloid_average(a_max, lambda a: rho_m0 * a ** -3)


def avg_rho_total(a_max: float, rho_m0: float = 1.0, V_plateau: float = 0.7) -> float:
    return _cycloid_average(a_max, lambda a: rho_m0 * a ** -3 + V_plateau)


# ---------------------------------------------------------------------------
# (3) Sharpness vs de Sitter identity:  <R>/4 over a closed matter+Lambda history
# ---------------------------------------------------------------------------
def mean_R_over_4(OL: float, a_max: float) -> float:
    """*** DEPRECATED / ARTEFACT *** V4-weighted <R>/4 for a closed matter+Lambda
    history forced to turn around at a_max.  Because constant OL>0 cannot recollapse,
    H^2 goes NEGATIVE on 1<a<a_max and is floored at 1e-30 -> the returned <R>/4 is an
    artefact of unphysical geometry.  See foundations/cw_banach_iteration.py for the
    correct CW dynamics.  Retained only for reproducibility of the (wrong) behaviour."""
    Om = 1 - OL
    Ok = (Om * a_max ** -3 + OL) * a_max ** 2     # H^2=0 at a_max
    H2 = lambda a: max(Om * a ** -3 + OL - Ok * a ** -2, 1e-30)
    dH2 = lambda a: -3 * Om * a ** -4 + 2 * Ok * a ** -3
    R = lambda a: 12 * H2(a) + 3 * a * dH2(a)     # 12H^2 + 6*(0.5 a dH2/da)
    w = lambda a: a ** 3 / math.sqrt(H2(a))
    num, _ = quad(lambda a: w(a) * R(a), 1e-3, a_max * (1 - 1e-6), limit=300)
    den, _ = quad(w, 1e-3, a_max * (1 - 1e-6), limit=300)
    return 0.25 * num / den


def main() -> int:
    print("=" * 72)
    print("KP four-volume self-consistency: absolute-scale route (Theorem 64)")
    print("=" * 72)

    # (1) topological constraint
    int_E4, int_T = anomaly_integral()
    print("\n(1) Topological KP constraint  Lambda_eff * V_4 = int <T> sqrt(g):")
    print(f"    int_S4 E_4 = 32 pi^2 chi = {int_E4:.4f}  (= 64 pi^2 = {64*math.pi**2:.4f})")
    print(f"    int_S4 <T> sqrt(g) = 4 a_gamma = {int_T:.6f}  (a_max-INVARIANT)")
    assert abs(int_E4 - 64 * math.pi ** 2) < 1e-9
    assert abs(int_T - 4 * A_GAMMA) < 1e-12

    # (2) category-error fix
    print("\n(2) Category-error fix: average rho_total (Thm 64 step 3), not rho_m:")
    print("     a_max     <rho_m>      <rho_total>   (rho_m0=1, V_plateau=0.7)")
    rm_prev = None
    for amx in [3.0, 1e2, 1e4, 1e8]:
        rm = avg_rho_m(amx)
        rt = avg_rho_total(amx)
        print(f"    {amx:8.1e}  {rm:.4e}   {rt:.4f}")
        rm_prev = rm
    rt_big = avg_rho_total(1e8)
    rm_big = avg_rho_m(1e8)
    assert rm_big < 1e-10               # rho_m collapses (the old mistake)
    assert abs(rt_big - 0.7) < 1e-2     # rho_total a_max-stable at the plateau
    print("    => <rho_m> -> 0 (the earlier mistake); <rho_total> -> V_plateau (stable).")

    # (3) sharpness vs de Sitter identity  -- DEPRECATED PROXY (artefact, see below)
    print("\n(3) DEPRECATED proxy mean_R_over_4 (floored H^2<0; artefact) -- input OL=0.685:")
    print("    [correct dynamics: foundations/cw_banach_iteration.py]")
    print("     a_max    <R>/4      ratio to 3*OL=2.055   verdict")
    OL = 0.685
    target = 3 * OL
    for amx in [1.5, 2.0, 3.0, 10.0, 100.0]:
        v = mean_R_over_4(OL, amx)
        ratio = v / target
        verdict = "SHARP (matter breaks identity)" if ratio < 0.95 else "-> identity"
        print(f"    {amx:6.1f}   {v:.4f}     {ratio:.4f}                {verdict}")
    sharp = mean_R_over_4(OL, 1.5)
    ident = mean_R_over_4(OL, 100.0)
    assert sharp < 0.95 * target        # moderate a_max: identity broken -> sharp
    assert abs(ident - target) < 0.02 * target  # large a_max: de Sitter identity

    print("\nVERDICT:")
    print("  - bulk vacuum energy cancels (sequestering); Lambda not free (Thm 64).")
    print("  - <rho_total>/<R> averages are a_max-STABLE (rho_m-only was the error).")
    print("  - the (3) proxy mean_R_over_4 is GEOMETRICALLY INCONSISTENT (floored H^2<0);")
    print("    its 'identity/sharp' reading was an artefact. The correct CW dynamics")
    print("    (foundations/cw_banach_iteration.py) give a UNIVERSAL Lambda* whose value")
    print("    is amplitude-set, with the absolute Omega_Lambda (phi_0) left FREE.")
    print("  - so the volume route delivers the universality STRUCTURE + order of")
    print("    magnitude, but NOT the sharp Lambda* nor the absolute scale.")
    print(f"  - theorem-level & prior-free regardless: ratio Omega_K/Omega_L "
          f"= a_gamma/(8pi^2) = {A_GAMMA/C_Q:.4e}.")
    print("\n[kp-volume] topological 4 a_g + a_max-stable total-average solid; (3) proxy is a "
          "floored-geometry artefact (see cw_banach_iteration.py); ratio theorem-level")
    return 0


if __name__ == "__main__":
    sys.exit(main())
