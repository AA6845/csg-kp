#!/usr/bin/env python3
"""
lombriser_coincidence.py  --  Structure-formation averaging fixes Omega_Lambda.

Reproduction of Lombriser's structure-formation counterpart to Kaloper-Padilla
(arXiv:1901.08588).  A dynamical dark-energy component cannot simultaneously have
w ~ -1 (data) and track matter (coincidence); the coincidence is therefore
resolved by the averaging prescription for Lambda, not by dark-energy dynamics.
Halo-weighted averaging with a uniform prior on the collapse variable
(equivalently y(t_0) = 1/2) DERIVES Omega_Lambda ~ 0.704.

Spherical-collapse top-hat (equality normalization a_eq = 1, pure Lambda):
    y'' + (2 + H'/H) y' + (1/2) Omega_m(a) (y^-3 - 1) y = 0,   ' = d/d ln a,
with Omega_m(a) = a^-3 / (a^-3 + 1), matter-dominated initial data
y_i = 1 - delta_i/3, y_i' = -delta_i/3.

Outputs the critical overdensity, a_0/a_eq at y = 1/2, Omega_Lambda, and the
synthesis trio (Omega_Lambda, Omega_m, Omega_K) using the CSG-KP ratio.

Dependencies: numpy, scipy.  Imports the ratio from csg_kp_core.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

from csg_kp_core import ratio, A_GAMMA, C_Q


def Omega_m_a(a):
    return a ** -3 / (a ** -3 + 1.0)


def _rhs(N, Y):
    """Top-hat ODE in e-folds N = ln a (equality normalization)."""
    y, yp = Y
    a = np.exp(N)
    om = Omega_m_a(a)
    return [yp, -(2 - 1.5 * om) * yp - 0.5 * om * (y ** -3 - 1) * y]


A_INIT = 1e-3
N_INIT = np.log(A_INIT)


def evolve(delta_i, N_max=np.log(1e6)):
    """Evolve a top-hat shell of initial overdensity delta_i until collapse."""
    def collapse(N, Y):
        return Y[0] - 1e-3
    collapse.terminal = True
    collapse.direction = -1
    return solve_ivp(_rhs, [N_INIT, N_max], [1 - delta_i / 3, -delta_i / 3],
                     events=collapse, dense_output=True,
                     rtol=1e-11, atol=1e-14, max_step=0.01)


def critical_overdensity():
    """Smallest delta_i that still collapses (the longest-lived shell)."""
    return brentq(lambda d: 1.0 if evolve(d).t_events[0].size > 0 else -1.0,
                  1e-3, 1.3e-3, xtol=1e-10)


def omega_lambda_from_collapse():
    """Derive Omega_Lambda from the uniform-prior condition y(t_0) = 1/2."""
    dic = critical_overdensity()
    sol = evolve(dic * 1.000001)
    N = np.linspace(N_INIT, sol.t[-1], 600_000)
    y = sol.sol(N)[0]
    a = np.exp(N)
    i_half = np.where(np.diff(np.sign(y - 0.5)))[0][-1]
    a0 = a[i_half]
    omega_lambda = 1.0 / (a0 ** -3 + 1.0)
    return dic, a0, omega_lambda


def main():
    print("=" * 70)
    print("Cosmic coincidence: structure-formation averaging (Lombriser 2019)")
    print("=" * 70)

    dic, a0, omega_lambda = omega_lambda_from_collapse()
    print(f"\n  critical overdensity  delta_i^crit = {dic:.6e}")
    print(f"  uniform prior y = 1/2 at  a_0/a_eq = {a0:.4f}")
    print(f"  => Omega_Lambda = 1/(a_0^-3 + 1) = {omega_lambda:.4f}")
    print(f"     (Lombriser 2019: 0.704;  Planck observation: 0.685)")

    omega_m = 1.0 - omega_lambda
    omega_k = omega_lambda * ratio("L0")
    print("\n  Synthesis trio (CSG-KP ratio a_gamma/(8 pi^2) for Omega_K):")
    print(f"    Omega_Lambda = {omega_lambda:.4f}   (+{100*(omega_lambda/0.685-1):.1f}% vs Planck 0.685)")
    print(f"    Omega_m      = {omega_m:.4f}")
    print(f"    Omega_K      = {omega_k:.3e}")

    assert 0.70 < omega_lambda < 0.71, "Omega_Lambda must reproduce ~0.704"
    print("\nSTATUS")
    print("  Omega_Lambda = 0.704 : DERIVED, but CONDITIONAL on the uniform-prior")
    print("  assumption y(t_0) = 1/2 (anthropic-like; not derived from the framework).")
    print("  The Euclidean topology fixes the dimensionless ratio Omega_K/Omega_Lambda;")
    print("  the KP self-consistency route gives only the universality structure of")
    print("  Lambda* (cw_banach_iteration.py), not the absolute scale (phi_0 free); this")
    print("  halo-weighted route supplies that scale as 0.704, at the cost of y=1/2.")


if __name__ == "__main__":
    main()
