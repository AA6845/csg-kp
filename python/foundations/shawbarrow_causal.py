#!/usr/bin/env python3
"""
shawbarrow_causal.py  --  Causal legitimation of the finite region and scale.

Reproduces the numerical content of the manuscript section "Causal legitimation
of the finite region and the saddle scale" (Shaw-Barrow, arXiv:1010.4262),
transferred to the CSG-KP setting:

  (B) Causal scale self-consistency Lambda ~ 1/t_U^2  ->  t_Lambda/t_U = 0.73,
      fixing L_HH ~ 1/H0 with no free scale.
  (C) Shaw-Barrow curvature N-integral (their Eq. 26) -> Omega_k0 ~ -0.0056,
      same family as CSG (Lambda -> field, <T>-constraint, curvature prediction).
  (D) Light-cone time weighting: the anomaly stress (a^4 H^4) is early-time
      dominated, so a naive dynamical (Lorentzian) evaluation fails -- the
      topological evaluation is required.
  (F) Hierarchy levels: O(1) / 10^122 (=A2=energy density) / 10^244 (=V4),
      and the 10^240 dynamical failure mode equals the V4 four-volume factor.

Dependencies: numpy, scipy.  numpy>=2: np.trapezoid.
Run:  python3 shawbarrow_causal.py
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import quad, cumulative_trapezoid
from scipy.optimize import brentq

A_GAMMA = 31.0 / 180.0

# --- (B) causal scale Lambda ~ 1/t_U^2 -------------------------------------
def t_U(OL):
    Om = 1 - OL
    val, _ = quad(lambda a: 1.0 / (a * np.sqrt(Om * a ** -3 + OL)), 1e-6, 1.0, limit=200)
    return val  # in 1/H0

def t_Lambda(OL):
    return 1.0 / np.sqrt(3 * OL)

def causal_scale_fixpoint():
    return brentq(lambda OL: 3 * OL - 1 / t_U(OL) ** 2, 0.1, 0.95)

# --- (C) Shaw-Barrow N-integral (their Eq. 26) -----------------------------
def _build(OL, Ntau=300000):
    Om = 1 - OL
    a = np.linspace(1e-5, 1.0, Ntau)
    Hphys = np.sqrt(Om * a ** -3 + OL)
    tau = cumulative_trapezoid(1.0 / (a ** 2 * Hphys), a, initial=0.0)
    tau0 = tau[-1]
    Hc = a * Hphys
    Aint = Hc * cumulative_trapezoid(a ** 2 / (6 * Hc ** 2), tau, initial=0.0)
    return tau, tau0, a, Hphys, Aint

def N_of(OL):
    tau, tau0, a, Hphys, Aint = _build(OL)
    r = tau0 - tau
    num = np.trapezoid(a * r ** 3 * Aint, tau)
    den = np.trapezoid(a ** 2 * (2 / 3 * r ** 3 + tau * r ** 2) * Aint, tau)
    return num / den

def shaw_barrow_curvature(OL=0.73, zeta_b=0.5, Ob0=0.0423):
    return -(zeta_b * Ob0 / 2) * N_of(OL)

# --- (D) light-cone time weighting -----------------------------------------
def lightcone_weighting(OL=0.685):
    tau, tau0, a, Hphys, Aint = _build(OL)
    r = tau0 - tau
    w_b = a * r ** 3 * Aint                      # baryon: a^4 rho_b ~ a
    w_an = a ** 4 * Hphys ** 4 * r ** 3 * Aint     # anomaly proxy: a^4 H^4
    def median_a(w):
        cw = cumulative_trapezoid(w, tau, initial=0.0); cw /= cw[-1]
        return np.interp(0.5, cw, a)
    return median_a(w_b), median_a(w_an)

# --- (F) hierarchy levels --------------------------------------------------
def hierarchy_levels(MPl=2.435e18, H0=1.5e-42):
    r = MPl / H0
    return r ** 2, r ** 4   # A2 (energy density / N_eff), V4 (four-volume)

# ---------------------------------------------------------------------------
def main():
    print("=" * 72)
    print("Causal legitimation (Shaw-Barrow) of the finite region and scale")
    print("=" * 72)

    print("\n(B) Causal scale  Lambda ~ 1/t_U^2")
    print("    OL      t_U[1/H0]   t_Lambda/t_U")
    for OL in [0.5, 0.685, 0.8]:
        print(f"    {OL:.3f}   {t_U(OL):.4f}      {t_Lambda(OL)/t_U(OL):.4f}")
    OL_fix = causal_scale_fixpoint()
    rl = t_Lambda(0.685) / t_U(0.685)
    print(f"    fixpoint 3 OL = 1/t_U^2 (factor unity): Omega_Lambda = {OL_fix:.3f}")
    print(f"    at observed 0.685: t_Lambda/t_U = {rl:.4f}  (Shaw-Barrow 9.7/13.7=0.73)")
    assert 0.70 < rl < 0.75, "coincidence ratio must be ~0.73"

    print("\n(C) Shaw-Barrow curvature N-integral (Eq. 26)")
    Ok0 = shaw_barrow_curvature()
    print(f"    Omega_k0 = -(zeta_b Ob0/2) N = {Ok0:+.5f}   (paper: -0.0056)")
    print("    Same family as CSG: Lambda->field, <T>-constraint, curvature prediction.")
    assert -0.008 < Ok0 < -0.004, "Shaw-Barrow curvature must be ~ -0.0056"

    print("\n(D) Light-cone time weighting (anomaly a^4 H^4 vs baryon a)")
    mb, man = lightcone_weighting()
    print(f"    baryon median a = {mb:.3f},  anomaly median a = {man:.3f}")
    print("    -> anomaly is early-time dominated; naive Lorentzian use fails,")
    print("       the topological (heat-kernel) evaluation is required.")
    assert man < mb, "anomaly must be weighted earlier than baryon"

    print("\n(F) Hierarchy levels")
    A2, V4 = hierarchy_levels()
    print(f"    (M_Pl/H0)^2 = {A2:.2e}  [energy density / N_eff = A2]")
    print(f"    (M_Pl/H0)^4 = {V4:.2e}  [four-volume = V4]")
    print(f"    naive anomaly ~ (a_g/8pi^2)(H/M_Pl)^2 ~ {A_GAMMA/(8*np.pi**2)/A2:.1e} (10^-125)")
    print("    Mechanism-2 failure 10^240 == V4 (NOT a (10^120)^2 artifact);")
    print("    P5: N_eff = M_Pl^2/H^2 ~ 10^122 compensates -> Omega_eff = a_g/(8pi^2).")
    assert 1e120 < A2 < 1e124 and 1e240 < V4 < 1e248

    print("\nSTATUS")
    print("  The causal principle legitimizes the finite region (= past light cone")
    print("  = Euclidean hemisphere) and the scale L_HH ~ 1/H0. It fixes magnitude")
    print("  and coincidence to order unity; the absolute Omega_Lambda it does not.")


if __name__ == "__main__":
    main()
