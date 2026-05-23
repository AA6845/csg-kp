#!/usr/bin/env python3
"""
csg_kp_core.py  --  CSG-KP framework constants and the central prediction.

Single source of truth for the parameter-free curvature-to-dark-energy ratio

        |Omega_K| / Omega_Lambda  =  a_gamma / (8 pi^2)  =  31 / (1440 pi^2)

and its Friedmann translation to the observable Omega_K today.  Every other
script in this directory imports its constants from here, so the numbers are
defined once and only once.

Inputs (both first-principles / literature-standard):
    a_gamma = 31/180     photon type-A conformal trace anomaly  (Birrell-Davies)
    C_Q     = 8 pi^2     Q-curvature charge of the hemisphere D^4 (Chang-Yang)

Prediction levels:
    L0  R_0    = a_gamma / (8 pi^2)                topological leading order (exact)
    L1  R_cap  = delta_theta_star / (8 pi^2)       cap-variational refinement
    L3  Omega_K^obs = R * Omega_Lambda             present-epoch Friedmann observable

Run directly for a self-test printing all headline numbers and the DESI pull.
Dependencies: numpy, scipy.
"""
from __future__ import annotations
import math
from scipy.optimize import brentq

# ---------------------------------------------------------------------------
# First-principles / literature inputs
# ---------------------------------------------------------------------------
A_GAMMA_NUM, A_GAMMA_DEN = 31, 180           # photon type-A anomaly: exact rational, single source
A_GAMMA = A_GAMMA_NUM / A_GAMMA_DEN          # float form (= 31/180); sympy modules build sp.Rational(NUM, DEN)
C_Q = 8.0 * math.pi ** 2                     # Q-curvature charge of D^4 (= 8 pi^2)

# ---------------------------------------------------------------------------
# Leading-order topological ratio (L0) and its inverse
# ---------------------------------------------------------------------------
L0 = A_GAMMA / C_Q                           # = 31 / (1440 pi^2) ~ 2.181e-3
L_B = C_Q / A_GAMMA                          # = 8 pi^2 / a_gamma ~ 458.4


def delta_theta_star() -> float:
    """Exact cap-saddle shift: solve a_gamma * cos^4(dtheta) = sin(dtheta)."""
    f = lambda x: A_GAMMA * math.cos(x) ** 4 - math.sin(x)
    return brentq(f, 0.01, 0.5, xtol=1e-12)


DELTA_THETA_STAR = delta_theta_star()        # ~ 0.16391
L1 = DELTA_THETA_STAR / C_Q                  # cap-variational refinement ~ 2.076e-3


def ratio(level: str = "L0") -> float:
    """Return |Omega_K|/Omega_Lambda at the requested prediction level."""
    if level == "L0":
        return L0
    if level == "L1":
        return L1
    raise ValueError(f"unknown level {level!r}; use 'L0' or 'L1'")


# ---------------------------------------------------------------------------
# Friedmann translation (L3)
# ---------------------------------------------------------------------------
# CSG-consistent matter fraction. The parameter-free prediction is the RATIO L0;
# the absolute Omega_Lambda = 4 a_g = 0.6889 is the budget-ladder conjecture
# (manuscript sec:ladder). Using the ladder-consistent Omega_m = 1 - 4 a_g - Omega_K
# = 0.3096 (the ladder-consistent matter fraction, not the CMB-only 0.3153) makes the
# single absolute value self-consistently across the pipeline. Planck 2018
# (Omega_m = 0.3111 +/- 0.0056) is consistent with it.
OMEGA_M = 0.3096


def omega_k_obs(omega_m: float = OMEGA_M, level: str = "L0", sign: str = "open") -> float:
    """Present-epoch curvature parameter from the ratio and the Friedmann sum rule.

    Omega_m + Omega_Lambda + Omega_K = 1  with  Omega_Lambda = L_b * |Omega_K|.
    For an open universe (K<0) the cosmological-convention Omega_K is positive.
    """
    r = ratio(level)
    Lb = 1.0 / r
    sgn = +1.0 if sign == "open" else -1.0
    # |Omega_K| = (1 - Omega_m) / (Lb +/- 1); the open branch carries the + sign.
    omega_k_abs = (1.0 - omega_m) / (Lb + sgn)
    return sgn * omega_k_abs


def omega_lambda_from(omega_m: float = OMEGA_M, level: str = "L0", sign: str = "open") -> float:
    """The dark-energy density implied by the ratio at fixed Omega_m: Omega_Lambda = L_b * |Omega_K|."""
    return abs(omega_k_obs(omega_m, level, sign)) / ratio(level)


def pull(predicted: float, measured: float, sigma: float) -> float:
    """Tension between prediction and measurement, in units of sigma."""
    return (measured - predicted) / sigma


# DESI DR2 + Planck curvature constraint (Chen & Zaldarriaga 2025).
DESI_OK = 0.0023
DESI_OK_SIGMA = 0.0011


def _selftest() -> None:
    print("=" * 70)
    print("CSG-KP core constants and central prediction")
    print("=" * 70)
    print(f"  a_gamma                = 31/180        = {A_GAMMA:.6f}")
    print(f"  C_Q                    = 8 pi^2        = {C_Q:.6f}")
    print(f"  delta_theta_star (exact)               = {DELTA_THETA_STAR:.6f}")
    print()
    print(f"  L0  R_0   = a_gamma/(8 pi^2)           = {L0:.6e}")
    print(f"  L1  R_cap = dtheta*/(8 pi^2)           = {L1:.6e}")
    print(f"  L_b = Omega_Lambda/|Omega_K|           = {L_B:.4f}")
    print(f"  L1/L0 (cap shift)                      = {L1 / L0:.4f}  (~5% smaller)")
    print()
    for level in ("L0", "L1"):
        ok = omega_k_obs(level=level)
        ol = abs(ok) / ratio(level)
        p = pull(ok, DESI_OK, DESI_OK_SIGMA)
        print(f"  {level}: Omega_K^obs = {ok:+.5e}, Omega_Lambda = {ol:.4f}, "
              f"DESI pull = {p:.2f} sigma")
    print()
    print("STATUS")
    print("  L0  : proven (topological identity).  L1 : cap-variational refinement.")
    print("  L3  : conditional on the physical-identification postulate A5 and on the")
    print("        observed Omega_m. Sign 'open' conditional on the HH branch (DESI >=2 sigma).")


if __name__ == "__main__":
    _selftest()
