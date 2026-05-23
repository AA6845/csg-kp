#!/usr/bin/env python3
"""
lightcone_coefficient.py  --  Can the causal closure be forced unique?

The causal closure writes 3 Omega_L = c/t_U^2 with c built from the past light cone.
Two separate questions, answered honestly:

  (1) THE HYPERSURFACE -- FORCED.  The maximal-enclosed-3-volume slice ("belly")
      is EXACTLY the apparent horizon (theta=0, r=1/H): dr/dt = Hr-1 = 0 <=> r=1/H.
      Two independent characterizations (max 3-volume; covariant Bousso/Hayward
      theta=0 surface) pick the same slice (r*H = 1.000).  The particle horizon
      (r*H ~ 55, the big-bang tip) is NOT a covariant boundary and is excluded.
      The earlier "x500 definition dependence" was an artifact of comparing the
      genuine causal boundary with a non-boundary.

  (2) THE FUNCTIONAL FORM -- NOT FORCED.  No available principle fixes it:
        - KP stationarity Lambda=1/4 <R>_M over the cone: NO fixpoint (the past-cone
          average is matter-dominated, <R>_M/4 ~ 14 vs needed ~2).
        - dimensional closures on the unique AH SPREAD over 0.49..0.96 (median 0.93),
          no cluster near the observed 0.685.
        - first law at the AH (Cai-Kim): reproduces Friedmann identically, no Lambda
          constraint.
        - de Sitter entropy saturation: Omega_L = 1 (trivial).
      The closure 3 OL = V3(AH)/(V_M t_U) -> 0.725 is ONE selective choice, NOT a
      distinguished one; most natural closures give ~0.93.

Conclusion: the causal route forces the hypersurface (apparent horizon) and an O(1)
band, but NOT a sharp or even narrow value -- the closure functional is undetermined,
and the natural candidates (KP stationarity, AH thermodynamics) fail. Honest status:
this route does not deliver the sharp Omega_L; it pins the ratio (theorem elsewhere),
the magnitude, the unique hypersurface, and an O(1) range, no more.
"""
from __future__ import annotations
import math
import os
import sys

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

_HERE = os.path.dirname(os.path.abspath(__file__))
_PARENT = os.path.dirname(_HERE)
for p in (_HERE, _PARENT):
    if p not in sys.path:
        sys.path.insert(0, p)


def E(a, OL): return math.sqrt((1 - OL) * a ** -3 + OL)
def age(OL):  return quad(lambda a: 1 / (a * E(a, OL)), 1e-8, 1, limit=200)[0]
def chi_lc(a, OL): return quad(lambda ap: 1 / (ap ** 2 * E(ap, OL)), a, 1, limit=200)[0]


def _cone(OL, n=6000):
    ag = np.linspace(1e-3, 1, n)
    H = np.array([E(a, OL) for a in ag])
    r = np.array([a * chi_lc(a, OL) for a in ag])
    return ag, H, r


def _geom(OL):
    ag, H, r = _cone(OL)
    V3 = (4 * math.pi / 3.0) * r ** 3
    rb = float(r.max())
    return dict(rb=rb, Ab=4 * math.pi * rb ** 2, Vb=(4 * math.pi / 3.0) * rb ** 3,
                VM=float(np.trapezoid(V3 / (ag * H), ag)), tU=age(OL))


def apparent_horizon_rH(OL):
    ag, H, r = _cone(OL)
    i = int(np.argmax(r))
    return r[i] * H[i]


def particle_horizon_rH(OL):
    ag, H, r = _cone(OL)
    return r[0] * H[0]


def mean_R_over_4_lightcone(OL):
    ag, H, r = _cone(OL)
    V3 = (4 * math.pi / 3.0) * r ** 3
    R = 3 * (1 - OL) * ag ** -3 + 12 * OL
    w = V3 / (ag * H)
    return 0.25 * np.trapezoid(R * w, ag) / np.trapezoid(w, ag)


# natural dimensionless closures on the unique apparent-horizon surface
_CLOSURES = {
    "1/t_U^2":            lambda g: 1 / g['tU'] ** 2,
    "V3(AH)/(V_M t_U)":   lambda g: g['Vb'] / (g['VM'] * g['tU']),
    "1/r_AH^2":           lambda g: 1 / g['rb'] ** 2,
    "V3(AH)/(V_M r_AH)":  lambda g: g['Vb'] / (g['VM'] * g['rb']),
    "sqrt(A_AH/V_M^?)":   lambda g: math.sqrt(g['Ab']) / math.sqrt(g['VM']),
}


def closure_fixpoints():
    out = {}
    for name, X in _CLOSURES.items():
        try:
            out[name] = brentq(lambda OL: 3 * OL - X(_geom(OL)), 0.15, 0.97, xtol=1e-6)
        except ValueError:
            out[name] = None
    return out


def main() -> int:
    OBS = 0.685
    print("=" * 72)
    print("Causal light-cone closure: is it uniquely forced?")
    print("=" * 72)

    print("\n[1] HYPERSURFACE -- FORCED: belly == apparent horizon (theta=0, r*H=1)")
    for OL in [0.489, OBS, 0.704]:
        print(f"    OL={OL:.3f}:  r_belly * H_belly = {apparent_horizon_rH(OL):.4f}")
    print(f"    particle horizon: r*H = {particle_horizon_rH(OBS):.1f} >> 1  -> excluded.")

    print("\n[2] FORM -- NOT FORCED (a) KP stationarity over the cone has no fixpoint:")
    for OL in [OBS, 0.704]:
        print(f"    OL={OL:.3f}:  (1/4)<R>_M = {mean_R_over_4_lightcone(OL):.2f}  vs need 3 OL = {3*OL:.2f}")

    print("\n[2] FORM -- NOT FORCED (b) dimensional closures spread, no cluster near 0.685:")
    fp = closure_fixpoints()
    for name, v in fp.items():
        print(f"    {name:22s} -> Omega_L* = {('none' if v is None else round(v,4))}")
    vals = np.array([v for v in fp.values() if v is not None])
    print(f"    spread: {vals.min():.3f}..{vals.max():.3f} (median {np.median(vals):.3f}); "
          f"0.725 is ONE selective choice, not distinguished.")

    print("\n[2] FORM -- NOT FORCED (c) thermodynamics:")
    print("    first law at AH -> Friedmann identity (no Lambda constraint);")
    print("    de Sitter entropy saturation -> Omega_L=1 (trivial).")

    # --- assertions -------------------------------------------------------
    assert abs(apparent_horizon_rH(OBS) - 1.0) < 1e-2          # belly = AH
    assert particle_horizon_rH(OBS) > 10                       # particle horizon excluded
    assert mean_R_over_4_lightcone(OBS) > 3 * 0.704            # KP form overshoots
    assert vals.max() - vals.min() > 0.3                       # closures genuinely spread
    assert np.median(vals) > 0.8                               # most land high (~0.93), not 0.685

    print("\nVERDICT:")
    print("  - HYPERSURFACE forced (apparent horizon); earlier x500 framing was wrong.")
    print("  - FORM not forced: KP stationarity fails, dimensional closures spread")
    print("    0.49..0.96 (median 0.93), AH thermodynamics give identity / Omega_L=1.")
    print("  - 0.725 is a selective closure, not distinguished. The causal route pins")
    print("    the hypersurface and an O(1) band, NOT a sharp value.")
    print("\n[lightcone] apparent-horizon hypersurface FORCED; functional form NOT forced "
          "(KP/thermo fail, closures spread 0.49..0.96); causal route gives O(1) band, not a sharp value")
    return 0


if __name__ == "__main__":
    sys.exit(main())
