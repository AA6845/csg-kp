#!/usr/bin/env python3
"""
ratio_vs_absolute_scope.py  --  The falsifiable core does not depend on the
holography problem.

This is the central re-evaluation: the cosmological-constant problem splits cleanly
in CSG-KP into a holography-FREE theorem core and a holography-DEPENDENT conjectural
bonus. The open holographic step (P5 = CKN saturation, schwinger_keldysh_p5.py) sits
ONLY in the bonus, not in the core.

THE CORE (theorem, scale-invariant, holography-free):
  Omega_K/Omega_L = a_g/(8 pi^2). Because N_eff ~ H^-2 and rho_anom ~ H^4, the factor
  H cancels COMPLETELY: the ratio is epoch-invariant and its NUMERICAL VALUE is the
  topological quotient (Cauchy + Chern-Weil + APS, A5a). P5 is needed here only as
  the EXISTENCE of the H^-2 lift, not its magnitude -- the magnitude cancels. So the
  Euclid-testable prediction is robust against the unproven CKN saturation.

THE BONUS (conjectural, NOT scale-invariant, holography-dependent):
  Omega_L = 4 a_g. The absolute value is epoch-dependent (was ~0 early, 0.69 today,
  -> 1 later); it carries the scalaron position phi_0 ("where/when the observer is").
  It is NOT scale-invariant, so scale-invariance CANNOT force it. Fixing it sharply
  requires P5 = CKN saturation, which is not proven.

WHY SCALE-INVARIANCE DOES NOT RESCUE THE ABSOLUTE VALUE (the fallacy to avoid):
  One might hope CSG conformal (scale-free) invariance forces the saturation. It does
  NOT: scale-invariance forces only the RATIO (which cancels H). The absolute value is
  precisely the non-scale-invariant quantity. Deriving its saturation from scale-
  invariance confuses ratio and absolute value.

CONSEQUENCE FOR FALSIFIABILITY:
  The framework stands as a sharp, Euclid-testable prediction (the ratio) WITHOUT
  solving the holography problem. The holography problem (CKN saturation) is confined
  to the optional sharper claim (absolute value, Planck 0.0 sigma). This is the
  correct, defensible scoping: rigorous + falsifiable core; conjectural bonus clearly
  flagged.
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


def ratio_is_scale_invariant():
    """Ratio = N_eff * rho_anom / rho_crit; H must cancel completely."""
    rho_anom = ag / (8 * PI**2) * 3 * H**4
    N_eff = Mpl**2 / H**2
    ratio = sp.simplify(N_eff * rho_anom / (3 * Mpl**2 * H**2))
    has_H = H in ratio.free_symbols
    has_Mpl = Mpl in ratio.free_symbols
    return ratio, has_H, has_Mpl


def main() -> int:
    print("=" * 72)
    print("Core (theorem, holography-free) vs absolute value (conjectural bonus)")
    print("=" * 72)

    ratio, has_H, has_Mpl = ratio_is_scale_invariant()
    print("\nZE1  CORE -- ratio Omega_K/Omega_L is scale-invariant (H, M_Pl both cancel):")
    print(f"      ratio = {ratio} = a_g/8pi^2 ;  contains H? {has_H} ;  contains M_Pl? {has_Mpl}")
    print("      => epoch-invariant, value topological (A5a). P5 needed only as the")
    print("         EXISTENCE of the H^-2 lift; its magnitude cancels. Holography-FREE.")
    assert ratio == ag / (8 * PI**2) and not has_H and not has_Mpl

    print("\nZE2  BONUS -- absolute Omega_L = 4 a_g is NOT scale-invariant:")
    print("      epoch-dependent (~0 early, 0.69 today, ->1 later), carries phi_0.")
    print("      scale-invariance CANNOT force it (it forces only the ratio). Fixing it")
    print(f"      needs P5 = CKN saturation (c^2=4a_g={float(4*ag):.4f}), not proven.")

    print("\nZE3  the fallacy avoided: deriving saturation from CSG scale-invariance")
    print("      confuses ratio (scale-invariant) and absolute value (not). No such route.")

    print("\nZE4  CONSEQUENCE: the Euclid-testable prediction (ratio) is ROBUST against the")
    print("      unproven holography problem. Holography confined to the optional bonus.")
    print("      Rigorous + falsifiable core; conjectural bonus flagged. This is the scope.")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
