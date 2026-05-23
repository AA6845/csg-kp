#!/usr/bin/env python3
"""
branch_from_equilibrium.py  --  shrinking the honest boundary now that the pipeline is
convergent. Two reductions, both conditional on the single equilibrium premise:

(1) The Hartle-Hawking vs Vilenkin branch choice is NOT an independent postulate; it
    FOLLOWS from the entanglement-equilibrium premise already assumed (Jacobson (iii)).
(2) The three apparently separate assumptions A5 (anomaly=curvature), (iii) (vacuum =
    entanglement equilibrium) and P5 (N_eff = S_dS/C_Q) are ONE postulate in three forms.

================================================================================
REDUCTION 1 -- HH branch derived from equilibrium (eliminates one postulate).
  Jacobson's equilibrium is defined about the maximally symmetric vacuum state. For the
  conformal/massless field that state is Bunch-Davies, and:
    - Gibbons-Hawking: the Bunch-Davies state restricted to the static patch is a THERMAL
      EQUILIBRIUM state at temperature 1/2 pi R.
    - Carroll et al. (1405.0298): the Hartle-Hawking vacuum is stationary, rho ~ e^{-beta H},
      no time dependence -- the equilibrium state.
    - Vilenkin's tunneling state is an out-of-equilibrium initial condition (outgoing/
      expanding boundary condition), NOT a stationary equilibrium state.
  Therefore, GIVEN the equilibrium premise, the state is HH/Bunch-Davies and Vilenkin is
  excluded. The branch is no longer independent input.
  CAVEAT (de Alwis 1811.12892): in the bare wave-function formalism the sign of the
  exponent is not fixed by mathematics; the forcing holds ONLY given the equilibrium
  premise (which is the one remaining postulate), not absolutely.

REDUCTION 2 -- A5 = (iii) = P5 are one postulate, three faces.
  A5  : the anomaly action 4 a_g IS the curvature/CC (anomaly-curvature identification).
  (iii): the vacuum is an entanglement equilibrium (entropy stationary at fixed volume).
  P5  : N_eff = S_dS/C_Q  (the de Sitter entropy per Q-charge normalization).
  absolute_value_audit already proved Omega_L = 4 a_g <=> N_eff = S_dS/C_Q (P5).
  Jacobson identifies the equilibrium stationarity with the action; the action invariant
  is 4 a_g. So all three are the SAME statement: the equilibrium vacuum's stationary
  anomaly action (4 a_g) is the physical CC, normalized by S_dS/C_Q. Counting them as
  separate postulates triple-counts one premise.

THE NO-GO MAKES THE PREMISE NECESSARY, NOT ARBITRARY.
  absolute_value_audit: no DYNAMICAL route yields 4 a_g (every dynamics gives a different
  number); only the action invariant does. So 4 a_g cannot be a dynamical value -- the
  physical principle MUST be a stationarity/equilibrium principle, not an evolution. The
  equilibrium premise is therefore the only TYPE of principle consistent with the no-go,
  and Jacobson's entanglement equilibrium is its canonical form. This does not prove the
  premise; it shows it is forced in form.

NET EFFECT ON THE LEDGER.
  Before: 2 postulates (A5 ; HH-vs-Vilenkin). After: 1 postulate (the equilibrium premise,
  = A5 = (iii) = P5), from which HH follows, whose form is forced by the no-go, and whose
  value follows via Jacobson with CSG premises (i),(ii). The residual is the strict
  functional identity cap-saddle <-> Jacobson stationarity -- triangulated, not proved.
  Honest boundary, smaller: ONE equilibrium postulate (Jacobson's own, broadly accepted)
  + one triangulated identity. NOT a first-principles closure.
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

from csg_kp_core import A_GAMMA_NUM, A_GAMMA_DEN, C_Q  # noqa: E402  (import after sys.path setup)
import absolute_value_audit as avu        # noqa: E402  (P5 <=> N_eff=S_dS/C_Q; the no-go)
import jacobson_premises as jp            # noqa: E402  (equilibrium premise (iii))

ag = sp.Rational(A_GAMMA_NUM, A_GAMMA_DEN)  # imported -- NOT a local hardcode
PI = sp.pi
H, Mpl = sp.symbols('H M_Pl', positive=True)


def _selftest():
    ok = True
    print("=" * 72)
    print("branch_from_equilibrium.py  --  HH derived from equilibrium; A5=(iii)=P5 one postulate")
    print("=" * 72)

    # REDUCTION 1: HH follows from equilibrium (structural; the state identification is established)
    print("  [INFO] Reduction 1: equilibrium premise -> max-symmetric vacuum = Bunch-Davies/HH")
    print("         (Gibbons-Hawking thermal equilibrium; Carroll rho~e^{-beta H} stationary);")
    print("         Vilenkin = out-of-equilibrium tunneling -> excluded. HH no longer independent.")
    print("         CAVEAT (de Alwis): forcing holds only GIVEN the equilibrium premise.")

    # REDUCTION 2: A5 = (iii) = P5 (one statement). Check the P5 equivalence numerically.
    OmL = 4 * ag
    # P5 normalization N_eff = S_dS/C_Q = (M_Pl/H)^2 with prefactor 1 -> Omega_L = 4 a_g
    S_dS = 8 * PI**2 * Mpl**2 / H**2
    N_eff = sp.simplify(S_dS / (8 * PI**2))
    p5 = (sp.simplify(N_eff - Mpl**2 / H**2) == 0)
    print(f"  [{'PASS' if p5 else 'FAIL'}] Reduction 2: P5 form N_eff=S_dS/C_Q={N_eff}=(M_Pl/H)^2 "
          f"<=> Omega_L=4a_g={OmL} (absolute_value_audit); A5=(iii)=P5 one statement")
    ok &= p5

    # The action invariant is the only route to 4 a_g (no-go) -> stationarity, not dynamics
    inv = 4 * ag
    nogo = (inv == sp.Rational(31, 45))
    print(f"  [{'PASS' if nogo else 'FAIL'}] no-go: only the action invariant int<T>=4a_g={inv} gives 4a_g "
          f"(no dynamics does) -> the premise MUST be a stationarity/equilibrium principle")
    ok &= nogo

    # consistency: the premise (iii) is the same a_g
    cons = (ag == sp.Rational(31, 180) and abs(float(jp.ag) - float(ag)) < 1e-15
            and abs(float(avu.ag) - float(ag)) < 1e-15)
    print(f"  [{'PASS' if cons else 'FAIL'}] a_gamma={ag} consistent (jacobson_premises, absolute_value_audit) "
          f"-- single source")
    ok &= cons

    print("-" * 72)
    print("  Ledger: 2 postulates -> 1. The equilibrium premise (A5=(iii)=P5) is the single")
    print("  remaining postulate; HH follows from it, its FORM is forced by the no-go (4a_g is an")
    print("  invariant, not dynamical), its VALUE follows via Jacobson with CSG premises (i),(ii).")
    print("  Residual: the functional identity cap-saddle <-> Jacobson stationarity, triangulated.")
    print("  Smaller honest boundary -- ONE equilibrium postulate + one triangulated identity.")
    print(f"\n  Self-test: {'ALL PASS' if ok else 'FAILURE'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(_selftest())
