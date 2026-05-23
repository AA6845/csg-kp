"""
csg_kp_theory.py  --  Cobaya theory class enforcing the CSG-KP curvature relation.

The framework predicts the parameter-free ratio
    |Omega_K| / Omega_Lambda = a_gamma / (8 pi^2),   a_gamma = 31/180,
which turns the LambdaCDM+curvature problem into a flat-LambdaCDM problem with a
single fixed ratio.

ROLE OF THIS MODULE. The curvature constraint is enforced directly in the YAML
config (csg_kp_cobaya.yaml) by reparametrizing Omega_K as a deterministic
function of the sampled cosmology and the fixed ratio:

    Omega_K = sign * ratio * (1 - Omega_m) / (1 + sign * ratio).

All quantities feeding Omega_K there are INPUT parameters, so the dependency
graph resolves before CAMB runs -- the robust Cobaya pattern for a hard
theoretical constraint. This module is the single source of truth for the
constants (A_GAMMA, C_Q, L0, L1, DELTA_THETA_STAR), imported by run_mcmc.py for
preflight checks and runnable standalone. The CSGKPTheory class below is an
OPTIONAL alternative that exposes the same constants as a Cobaya theory
component; the shipped YAML does not use it (the reparametrization is simpler
and version-robust).
"""
from __future__ import annotations
import math

# ---------------------------------------------------------------------------
# Framework constants (importable without Cobaya)
# ---------------------------------------------------------------------------
A_GAMMA = 31.0 / 180.0                       # photon type-A anomaly
C_Q = 8.0 * math.pi ** 2                     # Q-curvature charge of D^4
L0 = A_GAMMA / C_Q                           # = 31/(1440 pi^2) ~ 2.181e-3
DELTA_THETA_STAR = 0.16390621097198063       # exact cap-saddle (a_g cos^4 = sin)
L1 = DELTA_THETA_STAR / C_Q                  # cap-exact refinement ~ 2.076e-3

try:
    from cobaya.theory import Theory
    _COBAYA_AVAILABLE = True
except ImportError:                          # allow standalone import of constants
    Theory = object                          # type: ignore
    _COBAYA_AVAILABLE = False


class CSGKPTheory(Theory):
    """Cobaya theory exposing the CSG-KP ratio and sign as constant derived params."""

    prediction_level: str = "L0"             # 'L0' or 'L1'
    sign: str = "open"                       # 'open' (HH branch) or 'closed'

    @property
    def csg_kp_ratio(self) -> float:
        if self.prediction_level == "L0":
            return L0
        if self.prediction_level == "L1":
            return L1
        raise ValueError(f"Unknown prediction_level {self.prediction_level!r}; use 'L0' or 'L1'.")

    @property
    def csg_kp_sign_factor(self) -> float:
        if self.sign == "open":              # K<0 -> Omega_K > 0
            return +1.0
        if self.sign == "closed":            # K>0 -> Omega_K < 0
            return -1.0
        raise ValueError(f"Unknown sign {self.sign!r}; use 'open' or 'closed'.")

    # ----- Cobaya interface -----
    def initialize(self):
        self.log.info(
            f"CSG-KP: level={self.prediction_level}, sign={self.sign}, "
            f"ratio={self.csg_kp_ratio:.6e}, sign_factor={self.csg_kp_sign_factor:+.0f}")

    def get_requirements(self):
        return {}

    def calculate(self, state, want_derived=True, **params_values_dict):
        """Expose the (constant) ratio, sign factor and cap-saddle shift.

        These derived parameters are independent of the sampled cosmology; the
        YAML config consumes csg_kp_ratio / csg_kp_sign_factor to fix Omega_K.
        """
        state["derived"] = {
            "csg_kp_ratio": self.csg_kp_ratio,
            "csg_kp_sign_factor": self.csg_kp_sign_factor,
            "delta_theta_star": DELTA_THETA_STAR,
        }
        return True

    def get_can_provide_params(self):
        return ["csg_kp_ratio", "csg_kp_sign_factor", "delta_theta_star"]


if __name__ == "__main__":
    # Standalone sanity check (no Cobaya required).
    print(f"a_gamma = 31/180 = {A_GAMMA:.10f}")
    print(f"C_Q     = 8 pi^2 = {C_Q:.6f}")
    print(f"L0      = {L0:.6e}   (leading)")
    print(f"L1      = {L1:.6e}   (cap-exact)")
    print(f"Cobaya available: {_COBAYA_AVAILABLE}")
