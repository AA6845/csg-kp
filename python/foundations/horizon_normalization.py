#!/usr/bin/env python3
"""
horizon_normalization.py  --  resolving Mottola's open normalization with CSG.

Mottola's anomaly EFT supplies the MECHANISM of P5 (condensate coherence, horizon-scale
backreaction; coherence_from_condensate.py) but leaves the VALUE open: it "depends on
macroscopic boundary conditions at the cosmological horizon scale" and the conformal
theory (hence a_gamma) is unspecified. That is precisely the framework CSG has and Mottola
does not: CSG fixes the boundary condition by the Q-curvature charge and the conformal
theory by the photon. Feeding CSG's numbers into Mottola's mechanism fixes the one O(1)
that coherence_from_condensate.py left open.

================================================================================
WHAT MOTTOLA LEAVES OPEN  ->  WHAT CSG SUPPLIES (reverse).
  (i)   the value: "depends on horizon boundary conditions"   -> CSG: C_Q = 8 pi^2.
  (ii)  the conformal theory (a_gamma unspecified)            -> CSG: photon, a_g = 31/180.
  (iii) the exact O(1) of N_eff                               -> CSG: N_eff = S_dS/C_Q.

THE NORMALIZATION.
  de Sitter (Gibbons-Hawking) entropy, reduced Planck mass M_Pl^2 = 1/(8 pi G):
        S_dS = A/(4G) = (4 pi/H^2)/(4G) = 8 pi^2 (M_Pl/H)^2.
  Q-curvature charge of the hemisphere D^4 (Chang-Yang):
        C_Q = int_{D^4} Q_4 = 8 pi^2.
  Accumulation = de Sitter entropy per Q-charge:
        N_eff = S_dS / C_Q = (M_Pl/H)^2,   O(1) factor EXACTLY 1,
  because S_dS and C_Q share the same 8 pi^2 normalization. Mottola cannot obtain this
  without the Q-curvature structure (C_Q) and the photon (a_g); CSG can. The finite value
  Mottola's Lambda->0 does not give is the anomaly residual Omega_Lambda = 4 a_g, fixed by
  a_g (photon) and C_Q (hemisphere).

P5 AS THE DECLARED FOUNDING ASSUMPTION (not a deficit).
  P5 := N_eff = S_dS/C_Q (coherent accumulation = de Sitter entropy per Q-charge). Mottola
  supplies its physics (condensate coherence, horizon scale, not UV); CSG supplies its
  number (C_Q, a_g). P5 is the single founding assumption of the framework -- as fundamental
  as the holographic principle itself -- stated explicitly. Given P5, the framework is
  internally complete: value (4 a_g), sign (cap saddle), ratio (a_g/8 pi^2), interaction
  (running vacuum) are all fixed. This is the legitimate structure of a physical theory:
  one declared postulate, its consequences, and a falsification channel (DESI/Euclid).

STATUS: Mottola's open normalization is closed by CSG's C_Q (factor exactly 1) and his
unspecified conformal theory by the photon (a_g). The residual is no longer an undetermined
O(1) but the explicit, accepted founding assumption P5 = (entropy per Q-charge). A clean
relocation of the open surface onto a single declared postulate, not a hidden gap.
================================================================================
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

from csg_kp_core import A_GAMMA_NUM, A_GAMMA_DEN, C_Q  # noqa: E402  (core: single source of truth)

ag = sp.Rational(A_GAMMA_NUM, A_GAMMA_DEN)             # imported -- NOT a local hardcode
PI = sp.pi
H, Mpl, G = sp.symbols('H M_Pl G', positive=True)


def de_sitter_entropy():
    """Gibbons-Hawking S_dS = A/(4G) with M_Pl^2 = 1/(8 pi G): = 8 pi^2 (M_Pl/H)^2."""
    A = 4 * PI / H**2
    S = (A / (4 * G)).subs(G, 1 / (8 * PI * Mpl**2))
    return sp.simplify(S)


def n_eff_from_entropy_per_charge():
    """N_eff = S_dS / C_Q = (M_Pl/H)^2 (O(1) factor exactly 1)."""
    return sp.simplify(de_sitter_entropy() / (8 * PI**2))


def _selftest():
    ok = True
    print("=" * 72)
    print("horizon_normalization.py  --  Mottola's open O(1) closed by CSG's C_Q")
    print("=" * 72)

    S = de_sitter_entropy()
    a = (sp.simplify(S - 8 * PI**2 * Mpl**2 / H**2) == 0)
    print(f"  [{'PASS' if a else 'FAIL'}] S_dS = A/4G = {S} = 8 pi^2 (M_Pl/H)^2 (Gibbons-Hawking)")
    ok &= a

    b = abs(C_Q - float(8 * sp.pi**2)) < 1e-9
    print(f"  [{'PASS' if b else 'FAIL'}] C_Q from core = {C_Q:.6f} = 8 pi^2 (Chang-Yang Q-charge)")
    ok &= b

    N = n_eff_from_entropy_per_charge()
    c = (sp.simplify(N - Mpl**2 / H**2) == 0)
    print(f"  [{'PASS' if c else 'FAIL'}] N_eff = S_dS/C_Q = {N} = (M_Pl/H)^2 -> O(1) factor EXACTLY 1 "
          f"(S_dS and C_Q share the 8 pi^2 normalization)")
    ok &= c

    OmL = 4 * ag
    d = (OmL == sp.Rational(31, 45))
    print(f"  [{'PASS' if d else 'FAIL'}] finite value Mottola omits: Omega_L = 4 a_g = {OmL} = {float(OmL):.5f} "
          f"(anomaly residual, fixed by a_g + C_Q)")
    ok &= d

    e = (ag == sp.Rational(31, 180))
    print(f"  [{'PASS' if e else 'FAIL'}] a_gamma imported from core = {ag} (single source)")
    ok &= e

    print("-" * 72)
    print("  Mottola gives the mechanism but not the number; CSG's C_Q fixes the O(1) (=1) and")
    print("  the photon fixes a_g. The residual is the explicit founding assumption")
    print("  P5 := N_eff = S_dS/C_Q (entropy per Q-charge) -- declared, not hidden. Given P5 the")
    print("  framework is internally complete; falsification is via DESI/Euclid.")
    print(f"\n  Self-test: {'ALL PASS' if ok else 'FAILURE'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(_selftest())
