#!/usr/bin/env python3
"""
action_density_bridge.py  --  Computing the action-vs-density bridge prefactor.

The manuscript (line 927-930) flags one open step: the dark-energy density
FRACTION should equal the integrated anomaly ACTION on the full sphere
(Omega_L = int_{S^4}<T> = 4 a_g), and states "an action/topological identification
of the dark energy is required, which A5 does not provide" -- with the lift
prefactor uncomputed. This module computes that prefactor and states honestly
what is settled and what remains.

FIXED ANCHORS (none fit):
    a_gamma = 31/180                                    (sec:anomaly)
    rho_anom = (a_g/8 pi^2) * 3 H^4   (local photon anomaly density, spectral_coherence)
    rho_crit = 3 M_Pl^2 H^2
    Bekenstein-Hawking horizon dof:  N_surf = A/G, A = 4 pi/H^2, 1/G = 8 pi M_Pl^2

================================================================================
RESULT 1 -- the lift prefactor is COMPUTED, not identified.
  Omega_L = 4 a_g requires a lift  N = rho_L/rho_anom = 32 pi^2 (M_Pl/H)^2.
  This is EXACTLY the Bekenstein-Hawking horizon degree-of-freedom count
      N_surf = A/G = 4 pi/H^2 * 8 pi M_Pl^2 = 32 pi^2 (M_Pl/H)^2 = 4 S_dS .
  The manuscript's "bridge factor 32 pi^2" (spectral_coherence) is therefore the
  standard horizon dof count A/G -- not a free or chosen normalization. With it,
      Omega_L = (A/G) * rho_anom / rho_crit = 4 a_gamma   (exact, prefactor falls out).
  The (M_Pl/H)^2 in A/G is exactly the power that lifts rho_anom ~ H^4 to
  rho_crit ~ M_Pl^2 H^2, which is why the result is scale-free.

RESULT 2 -- coherence (xN) is FORCED by scale-freeness, not assumed freely.
  Incoherent sqrt(N) accumulation gives Omega_L ~ (H/M_Pl) -- scale-dependent and
  vanishing. Only coherent xN accumulation yields a pure number (4 a_g). So a
  finite, H-independent Omega_L SELECTS coherent accumulation uniquely. (Physical
  motivation: the anomaly vacuum energy is a 4-form condensate, coherence_from_
  condensate.py; here it is additionally forced by scale-freeness.)

STATUS (honest, point a):
  COMPUTED, no longer "uncomputed": the lift prefactor = A/G (Bekenstein-Hawking
  horizon dof). The "why 32 pi^2" question is answered (horizon dof count), and
  Omega_L = 4 a_g falls out exactly with coherent accumulation forced.

  TWO honest caveats a reviewer will raise, stated up front:
  (W1) The A/G route is NOT independent of the chi-topology route. Both share the
       int E_4 / C_Q structure: topological 4 = int_{S^4}E_4/16pi^2 = 64pi^2/16pi^2,
       holographic 4 = int_{D^4}E_4/C_Q = 32pi^2/8pi^2, and 64pi^2=2*32pi^2,
       16pi^2=2*8pi^2 -> the same "4". So A/G is a consistent physical RE-EXPRESSION
       of the topological factor (identifying 32pi^2 as the horizon dof A/G), NOT a
       second independent derivation of 4 a_g.
  (W2) The factor 4 = A/G vs S_dS is a CHOICE of accumulation carrier: N=S_dS gives
       a_g, N=2 S_dS gives 2 a_g, N=A/G=4 S_dS gives 4 a_g. A/G is Padmanabhan's
       standard surface dof N_surf=A/L_P^2, but that the accumulation runs over the
       dof count (A/G) rather than the entropy (S_dS) is PART of the P5 assumption,
       not independently established.

  REMAINS a physical assumption (NOT a theorem): the holographic accumulation
  PRINCIPLE -- that the DE vacuum density IS the coherent accumulation of the local
  anomaly density over the horizon dof, rho_L = (A/G) rho_anom. This is P5, the
  framework's single founding assumption. Computing the prefactor removes the
  "uncomputed prefactor" residue and reduces the open step to that one principle
  (with forced coherence, W1, W2 made explicit). The theorem-level ratio
  Omega_K/Omega_L = a_g/8 pi^2 is untouched.
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
from csg_kp_core import A_GAMMA_NUM, A_GAMMA_DEN  # single source -- NOT a local hardcode

ag = sp.Rational(A_GAMMA_NUM, A_GAMMA_DEN)
H, Mpl = sp.symbols('H M_Pl', positive=True)
PI = sp.pi


def lift_required():
    """Lift N = rho_L/rho_anom that Omega_L = 4 a_g demands."""
    rho_anom = ag / (8 * PI**2) * 3 * H**4
    rho_crit = 3 * Mpl**2 * H**2
    return sp.simplify(4 * ag * rho_crit / rho_anom)


def horizon_dof():
    """Bekenstein-Hawking horizon dof N_surf = A/G (reduced Planck units)."""
    A = 4 * PI / H**2
    inv_G = 8 * PI * Mpl**2
    return sp.simplify(A * inv_G)


def omega_lambda_holographic(coherent=True):
    """Omega_L from rho_L = N * rho_anom, coherent (N) vs incoherent (sqrt N)."""
    rho_anom = ag / (8 * PI**2) * 3 * H**4
    rho_crit = 3 * Mpl**2 * H**2
    N = horizon_dof()
    rho_L = (N if coherent else sp.sqrt(N)) * rho_anom
    return sp.simplify(rho_L / rho_crit)


def main() -> int:
    print("=" * 72)
    print("Action-vs-density bridge: computing the lift prefactor")
    print("=" * 72)

    N_req = lift_required()
    N_surf = horizon_dof()
    print("\nZE1  lift prefactor is the Bekenstein-Hawking horizon dof A/G:")
    print(f"      N required by Omega_L=4a_g : {sp.nsimplify(N_req)}")
    print(f"      N_surf = A/G               : {sp.nsimplify(N_surf)}")
    print(f"      equal? {sp.simplify(N_req - N_surf) == 0}   (= 4 S_dS; standard, not free)")
    assert sp.simplify(N_req - N_surf) == 0

    OmL = omega_lambda_holographic(coherent=True)
    print("\nZE2  Omega_L = (A/G) * rho_anom / rho_crit (coherent xN):")
    print(f"      = {OmL} = 4 a_g = {float(OmL):.4f}   (exact, prefactor falls out)")
    assert OmL == 4 * ag

    OmL_inc = omega_lambda_holographic(coherent=False)
    print("\nZE3  coherence forced: incoherent sqrt(N) gives")
    print(f"      Omega_L = {sp.nsimplify(OmL_inc)} ~ (H/M_Pl)  (scale-dependent -> excluded)")
    print("      only coherent xN yields a pure number; scale-freeness SELECTS coherence.")
    assert OmL_inc != 4 * ag

    print("\nZE4  caveat W1 (not independent): topological 4 = int_S4 E4/16pi^2 = 64/16,")
    print("      holographic 4 = int_D4 E4/C_Q = 32/8 -- same int E_4 / C_Q structure.")
    assert sp.Rational(64, 16) == sp.Rational(32, 8)  # the two "4"s are the same
    print("      => A/G is a physical re-expression of the topological factor, not a 2nd")
    print("         independent derivation of 4 a_g.")

    print("\nZE5  caveat W2 (carrier choice): N=S_dS->a_g, N=2S_dS->2a_g, N=A/G=4S_dS->4a_g.")
    for k in (1, 2, 4):
        print(f"        N={k} S_dS: Omega_L = {sp.Rational(k,1)*ag} = {float(k*ag):.3f}")
    print("      => the factor 4 is the dof-count (A/G) vs entropy (S_dS) choice; running")
    print("         over dof is PART of P5, not independently established.")

    print("\nZE6  STATUS: prefactor COMPUTED (= A/G, horizon dof); coherence FORCED;")
    print("      W1+W2 explicit; remaining assumption = holographic accumulation principle")
    print("      P5, rho_L=(A/G)rho_anom. Ratio Omega_K/Omega_L = a_g/8pi^2 untouched.")
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
