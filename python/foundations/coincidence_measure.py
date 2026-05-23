#!/usr/bin/env python3
"""
coincidence_measure.py  --  Why the SHARP absolute Omega_Lambda is not pinned by
the history-ensemble average (the measure problem).

Scope: this module is about the *sharp* value via an ensemble average. The
structural fixing of Lambda (not free, sign negative, bulk vacuum cancels) is
separately derived by the KP self-consistency route; the absolute scale, however,
is NOT delivered by it -- Lambda* is universal but amplitude-set and phi_0 stays
free (foundations/cw_banach_iteration.py). What is NOT pinned here is the
sharp number: levers (1)-(3) are attempts to remove Lombriser's uniform prior
using a CSG-KP ingredient; each fails, and the ANTHROPIC (observer-weighted
ensemble) version of the problem is categorical. Lever (4) shows the way around
it: a causal closure needs no measure and brackets Omega_L prior-free to an O(1) band.

  (1) Collapse-time lever.  Lombriser's 0.704 is the limit of the longest-lived
      shell; shorter shell lifetimes give SMALLER Omega_Lambda.  CSG Theorem 64
      forbids t_max -> infinity (finite V4 via background recollapse), which
      could in principle truncate the shell lifetime.

  (2) Recollapse test (the lever fails).  Forward integration of the full
      background dynamics (Friedmann + Klein-Gordon with the Coleman-Weinberg
      potential) gives recollapse at a_max ~ 6.5e17 (~41 e-folds), whereas
      Omega_Lambda=0.685 would require a_max ~ 6.7 -- 17 orders too late.

  (3) Measure lever.  Replacing the uniform-in-y prior by the Hartle-Hawking
      amplitude |Psi|^2 ~ exp(-8 a_gamma sigma_0) does not fix the answer:
      combined with different companion measures Omega_Lambda ranges over the
      whole interval 0..1.  No axiom fixes the companion (observer) measure.

Dependencies: numpy, scipy.  numpy>=2: np.trapezoid.
Run:  python3 coincidence_measure.py
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid
from scipy.optimize import brentq

A_GAMMA = 31.0 / 180.0

# ---------------------------------------------------------------------------
# Spherical-collapse top-hat (equality normalization a_eq = 1, pure Lambda)
# ---------------------------------------------------------------------------
def _om_a(a):
    return a ** -3 / (a ** -3 + 1.0)

def _tophat_rhs(N, Y):
    y, yp = Y
    om = _om_a(np.exp(N))
    return [yp, -(2 - 1.5 * om) * yp - 0.5 * om * (y ** -3 - 1) * y]

_N_INIT = np.log(1e-3)

def _evolve(delta_i, N_max=np.log(1e5)):
    def collapse(N, Y):
        return Y[0] - 1e-3
    collapse.terminal = True
    collapse.direction = -1
    return solve_ivp(_tophat_rhs, [_N_INIT, N_max], [1 - delta_i / 3, -delta_i / 3],
                     events=collapse, dense_output=True,
                     rtol=1e-11, atol=1e-14, max_step=0.01)

# ---------------------------------------------------------------------------
# (1) Collapse-time lever: Omega_Lambda as a function of shell lifetime
# ---------------------------------------------------------------------------
def collapse_time_lever():
    """Return list of (delta_i, a_collapse, a_half, Omega_Lambda)."""
    rows = []
    for di in [1.1346e-3, 1.20e-3, 1.50e-3, 3.0e-3, 8.0e-3]:
        s = _evolve(di)
        if s.t_events[0].size == 0:
            continue
        a_collapse = np.exp(s.t_events[0][0])
        N = np.linspace(_N_INIT, s.t[-1], 400_000)
        y = s.sol(N)[0]
        a = np.exp(N)
        idx = np.where(np.diff(np.sign(y - 0.5)))[0]
        if idx.size == 0:
            continue
        a_half = a[idx[-1]]
        OL = 1.0 / (a_half ** -3 + 1.0)
        rows.append((di, a_collapse, a_half, OL))
    return rows

# ---------------------------------------------------------------------------
# (2) Recollapse test: Friedmann + Klein-Gordon with the CW potential
#     V(phi) = A phi^4 (2 ln(phi/v_S) - 25/6),  reduced units M_Pl = H0 = 1
# ---------------------------------------------------------------------------
_A_CW, _VS, _PHI0 = 3.6e-6, 1.0, 22.9

def _V(phi):  return _A_CW * phi ** 4 * (2 * np.log(phi / _VS) - 25.0 / 6.0)
def _dV(phi): return _A_CW * phi ** 3 * (8 * np.log(phi / _VS) - 44.0 / 3.0)
def _d2V(phi):return _A_CW * phi ** 2 * (24 * np.log(phi / _VS) - 36.0)

_PHI_CRIT = _VS * np.exp(25.0 / 12.0)          # phi where V = 0  (~8.03)
_RHO_M0 = 3.0 - _V(_PHI0)                       # today: 3H^2 = rho_m + V, H=a=1

def _bg_rhs(N, Y):
    phi, phip = Y
    rho_m = _RHO_M0 * np.exp(-3 * N)
    H2 = (rho_m + _V(phi)) / (3 - 0.5 * phip ** 2)
    if H2 <= 0:
        return [phip, 0.0]
    HoH = -0.5 * (rho_m / H2 + phip ** 2)
    return [phip, -(3 + HoH) * phip - _dV(phi) / H2]

def recollapse_scale():
    """e-folds and a_max at which phi reaches phi_crit (V=0); beyond, V<0 and
    recollapse is unavoidable once matter dilutes."""
    def cross(N, Y):
        return Y[0] - _PHI_CRIT
    cross.terminal = True
    cross.direction = -1
    phip0 = -_dV(_PHI0) / _V(_PHI0)             # slow-roll start
    s = solve_ivp(_bg_rhs, [0, 300], [_PHI0, phip0], events=cross,
                  rtol=1e-10, atol=1e-13, max_step=0.05)
    N_c = s.t_events[0][0] if s.t_events[0].size else np.nan
    return N_c, np.exp(N_c)

# ---------------------------------------------------------------------------
# (3) Hartle-Hawking amplitude as prior, with four companion measures
#     |Psi(sigma_0)|^2 ~ exp(-8 a_gamma sigma_0), sigma_0 = ln a along the
#     critical-shell trajectory; <y> then maps to Omega_Lambda.
# ---------------------------------------------------------------------------
def hh_measure_spread():
    """Return dict {companion: (mean_y, Omega_Lambda)}."""
    di = brentq(lambda d: 1.0 if _evolve(d).t_events[0].size > 0 else -1.0,
                1e-3, 1.3e-3, xtol=1e-10)
    s = _evolve(di * 1.000001)
    N = np.linspace(_N_INIT, s.t[-1], 300_000)
    y = s.sol(N)[0]
    a = np.exp(N)
    om = _om_a(a)
    H = np.sqrt(om * a ** -3 + (1 - om))         # H in units where pure-L part = 1-om
    sigma0 = N - N[0]                            # conformal factor proxy >= 0
    w_hh = np.exp(-8 * A_GAMMA * sigma0)         # Hartle-Hawking weight
    # Omega_Lambda implied if the universe "is observed" at scale a (y there):
    OL_at = 1.0 / (a ** -3 + 1.0)
    companions = {
        "dN  (uniform in sigma0)": np.ones_like(a),
        "dt":                       1.0 / H,
        "V4  (a^3 y^3 dt)":         a ** 3 * y ** 3 / H,
        "phase space (a^3 dt)":     a ** 3 / H,
    }
    out = {}
    for name, comp in companions.items():
        w = w_hh * comp
        mean_y = np.trapezoid(y * w, N) / np.trapezoid(w, N)
        mean_OL = np.trapezoid(OL_at * w, N) / np.trapezoid(w, N)
        out[name] = (mean_y, mean_OL)
    return out

# ---------------------------------------------------------------------------
# (4) Causal closure: avoids the measure problem; narrows Omega_L to an O(1) band
#     3 Omega_L = c / t_U^2,  c = light-cone coefficient A_dM/(t_U^-1 V_M) = O(1).
# ---------------------------------------------------------------------------
from scipy.integrate import quad as _quad

def _t_U(OL):
    Om = 1 - OL
    v, _ = _quad(lambda a: 1 / (a * np.sqrt(Om * a ** -3 + OL)), 1e-7, 1, limit=200)
    return v

def causal_bracket():
    """Prior-free Omega_L from causal self-consistency, for natural c in [1,2]."""
    out = {}
    for c in (1.0, 1.5, 1.86, 2.0):
        OL = brentq(lambda x: 3 * x - c / _t_U(x) ** 2, 0.05, 0.98)
        out[c] = OL
    return out

# ---------------------------------------------------------------------------
def main():
    print("=" * 72)
    print("Coincidence / measure problem: why absolute Omega_Lambda is not derivable")
    print("=" * 72)

    print("\n(1) Collapse-time lever  (Lombriser 0.704 = longest-lived shell)")
    print("    delta_i      a_collapse   a_half      Omega_Lambda")
    rows = collapse_time_lever()
    for di, ac, ah, OL in rows:
        print(f"    {di:.4e}  {ac:9.2f}    {ah:7.3f}     {OL:.4f}")
    OL_crit = rows[0][3]
    assert 0.70 < OL_crit < 0.71, "critical shell must give ~0.704"
    print("    -> 0.704 is the long-lifetime limit; shorter lifetime -> smaller Omega_L.")
    print("       Truncating the lifetime to a_collapse ~ O(10) would give ~0.685.")

    print("\n(2) Recollapse test  (does CSG's finite-V4 recollapse truncate it?)")
    N_c, a_max = recollapse_scale()
    print(f"    CW potential V(phi)=A phi^4(2 ln(phi/v_S)-25/6), A={_A_CW}, phi0={_PHI0}")
    print(f"    V(phi0)={_V(_PHI0):.3f} (~rho_L today), m_phi={np.sqrt(_d2V(_PHI0)):.3f} H0")
    print(f"    phi reaches phi_crit={_PHI_CRIT:.2f} (V=0) at N={N_c:.1f} e-folds")
    print(f"    => a_max ~ {a_max:.2e} x today   (needed for 0.685: ~6.7)")
    overshoot = a_max / 6.7
    print(f"    LEVER FAILS: recollapse {np.log10(overshoot):.0f} orders of magnitude too late.")
    assert a_max > 1e15, "recollapse must be astronomically late"

    print("\n(3) Measure lever  (Hartle-Hawking prior, four companion measures)")
    spread = hh_measure_spread()
    print("    HH x companion             <y>      Omega_Lambda")
    vals = []
    for name, (my, mol) in spread.items():
        print(f"    {name:26s} {my:.3f}    {mol:.3f}")
        vals.append(mol)
    lo, hi = min(vals), max(vals)
    print(f"    -> Omega_Lambda ranges over [{lo:.2f}, {hi:.2f}]: the companion measure")
    print("       (physically the observer density) is free; no axiom fixes it.")
    assert hi - lo > 0.5, "the point is a wide spread (measure problem)"

    print("\n(4) Causal closure  (avoids the measure problem: no ensemble, no observer weight)")
    cb = causal_bracket()
    print("    3 Omega_L = c / t_U^2,  c = light-cone coefficient O(1):")
    for c, OL in cb.items():
        tag = "  <- observed 0.685" if abs(OL - 0.685) < 0.01 else ""
        print(f"    c = {c:.2f}  ->  Omega_L = {OL:.3f}{tag}")
    band = (min(cb.values()), max(cb.values()))
    print(f"    prior-free band over c in [1,2]: Omega_L in [{band[0]:.2f}, {band[1]:.2f}] "
          f"(contains 0.685)")
    assert band[0] < 0.685 < band[1], "observed value must lie in the causal band"

    print("\nSTATUS")
    print("  Structure of Lambda (not free, sign, vacuum cancels) is derived; the absolute")
    print("  scale is NOT (Lambda* universal but amplitude-set, phi_0 free; cw_banach_iteration.py).")
    print("  What is NOT pinned is the SHARP value via a history ensemble: the ANTHROPIC")
    print("  measure (levers 1-3) is categorical -- ensemble x observer weight undetermined,")
    print("  Omega_L spreads 0..1. The CAUSAL closure (4) needs no measure, and on it the")
    print("  boundary hypersurface is FORCED: it is the apparent horizon (theta=0, r*H=1),")
    print("  not a free choice (the particle horizon, r*H~55, is excluded). But the closure")
    print("  FUNCTIONAL is NOT forced: KP stationarity has no fixpoint over the cone, AH")
    print("  thermodynamics give an identity or Omega_L=1, and bare dimensional closures")
    print("  spread 0.49..0.96 (the 0.725 closure is one selective choice, not distinguished).")
    print("  Fixed prior-free: ratio Omega_K/Omega_L = a_g/(8 pi^2) (theorem) and a forced")
    print("  apparent-horizon hypersurface with an O(1) range -- NOT a sharp value; the sharp")
    print("  0.704 stays halo-prior (y=1/2) conditional, or the budget-ladder conjecture.")


if __name__ == "__main__":
    main()
