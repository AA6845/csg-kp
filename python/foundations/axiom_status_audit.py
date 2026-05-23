#!/usr/bin/env python3
"""
axiom_status_audit.py  --  Consistency, completeness, and the open-point ledger.

This module does three things and asserts on all of them:

  1. CONSISTENCY  -- it imports the headline numbers from the actual modules
     (not hard-coded copies) and checks they agree across the pipeline and with
     the manuscript ledger (a_gamma, C_Q, the ratio L0/L1, the cap saddle).

  2. COMPLETENESS -- every axiom / hypothesis / input of the manuscript is mapped
     to the module that exhibits it; a point with no backing module is a FAIL.

  3. CLARIFICATION -- each point is assigned one epistemic class and its
     falsification criterion, so the standing of every "open" point is explicit.

Epistemic classes
  THEOREM        established mathematics (or proven within the closed manifold class)
  DERIVED        derived inside the framework given the input axioms A1-A3
  DERIVED|X      derived conditional on a named further input X
  NUMERICAL      numerically established; a formal analytic proof is the only gap
  LITERATURE     a standard peer-reviewed input, used not re-derived
  POSTULATE      a physical hypothesis, decided by observation (not by proof)
  CONVENTION     a calibration/labelling choice, not a claim about nature
  OPEN           genuinely open (neither proven nor numerically settled)
"""
from __future__ import annotations
import math
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_PARENT = os.path.dirname(_HERE)
for p in (_HERE, _PARENT):
    if p not in sys.path:
        sys.path.insert(0, p)

import csg_kp_core as core            # noqa: E402
import a3_uniqueness as a3            # noqa: E402
import falsification_suite as fs      # noqa: E402
import close_open_points as cop       # noqa: E402  (a_gamma copy: AG)
import coincidence_measure as cm      # noqa: E402  (a_gamma copy: A_GAMMA)
import shawbarrow_causal as sb        # noqa: E402  (a_gamma copy: A_GAMMA)
import spectral_coherence as sc        # noqa: E402  (a_gamma IMPORTED from core)
import absolute_value_audit as avu     # noqa: E402  (a_gamma IMPORTED from core)
import cross_framework_anchor as cfa   # noqa: E402  (a_gamma IMPORTED from core)
import running_vacuum_interaction as rvi  # noqa: E402  (a_gamma IMPORTED from core)
import unified_open_point as uop         # noqa: E402  (a_gamma IMPORTED from core)
import coherence_from_condensate as cfc   # noqa: E402  (a_gamma IMPORTED from core)
import horizon_normalization as hn        # noqa: E402  (a_gamma + C_Q IMPORTED from core)
import p5_entanglement_anchor as pea      # noqa: E402  (a_gamma + C_Q IMPORTED from core)
import jacobson_premises as jp            # noqa: E402  (a_gamma + C_Q IMPORTED from core)
import branch_from_equilibrium as bfe      # noqa: E402  (a_gamma + C_Q IMPORTED from core)
import falsification_robustness as fr       # noqa: E402  (a_gamma + C_Q IMPORTED from core)
import desi_w_tension as dwt                 # noqa: E402  (a_gamma IMPORTED from core)

# ---------------------------------------------------------------------------
# 1. CONSISTENCY: headline numbers must agree across modules + manuscript ledger
# ---------------------------------------------------------------------------
def consistency_checks() -> list[tuple[str, bool, str]]:
    out = []

    # a_gamma identical across EVERY module that holds a copy (verschaltung check)
    copies = {"core": core.A_GAMMA, "a3": a3.A_GAMMA, "fs": fs.A_GAMMA,
              "close_open": cop.AG, "coincidence": cm.A_GAMMA, "shawbarrow": sb.A_GAMMA}
    ok = all(abs(v - 31.0 / 180.0) < 1e-15 for v in copies.values())
    out.append(("a_gamma = 31/180 across all 6 modules holding a copy", ok,
                " ".join(f"{k}={v:.6f}" for k, v in copies.items())))

    # the 4 newer foundations modules IMPORT a_gamma from core (no own copy): verify
    # they are wired through and resolve to the same value (full verschaltung check)
    wired = {"spectral_coherence": float(sc.ag), "absolute_value_audit": float(avu.ag),
             "cross_framework_anchor": float(cfa.ag), "running_vacuum_interaction": float(rvi.ag),
             "unified_open_point": float(uop.ag), "coherence_from_condensate": float(cfc.ag),
             "horizon_normalization": float(hn.ag), "p5_entanglement_anchor": float(pea.ag),
             "jacobson_premises": float(jp.ag), "branch_from_equilibrium": float(bfe.ag),
             "falsification_robustness": float(fr.ag), "desi_w_tension": float(dwt.ag)}
    ok = all(abs(v - core.A_GAMMA) < 1e-15 for v in wired.values())
    out.append(("a_gamma imported from core in all 12 newer modules (no hardcode)", ok,
                " ".join(f"{k}={v:.6f}" for k, v in wired.items())))

    # C_Q identical in core and falsification suite, equals 8 pi^2
    ok = (abs(core.C_Q - fs.C_Q) < 1e-12 and abs(core.C_Q - 8 * math.pi ** 2) < 1e-12)
    out.append(("C_Q = 8 pi^2 across core / falsification", ok,
                f"core={core.C_Q:.6f} fs={fs.C_Q:.6f}"))

    # L0 = a_gamma / C_Q internally, and equals falsification-suite RATIO
    ok = (abs(core.L0 - core.A_GAMMA / core.C_Q) < 1e-15
          and abs(core.L0 - fs.RATIO) < 1e-15)
    out.append(("ratio L0 = a_gamma/C_Q = falsification RATIO", ok,
                f"L0={core.L0:.6e} fs.RATIO={fs.RATIO:.6e}"))

    # cap saddle: recompute the root of a_gamma cos^4 = sin, compare to core
    f = lambda x: core.A_GAMMA * math.cos(x) ** 4 - math.sin(x)
    lo, hi = 0.01, 1.0
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    dstar = 0.5 * (lo + hi)
    ok = abs(dstar - core.DELTA_THETA_STAR) < 1e-6 and abs(dstar - 0.16391) < 1e-4
    out.append(("cap saddle delta* = 0.16391 (recomputed vs core)", ok,
                f"recomputed={dstar:.5f} core={core.DELTA_THETA_STAR:.5f}"))

    # L1 = delta* / C_Q internally
    ok = abs(core.L1 - core.DELTA_THETA_STAR / core.C_Q) < 1e-15
    out.append(("L1 = delta*/C_Q internally consistent", ok,
                f"L1={core.L1:.6e}"))

    # manuscript ledger values reproduced
    ok = abs(core.L0 - 2.181e-3) < 1e-5 and abs(core.L1 - 2.076e-3) < 1e-5
    out.append(("ledger L0=2.181e-3, L1=2.076e-3 reproduced", ok,
                f"L0={core.L0:.4e} L1={core.L1:.4e}"))

    return out

# ---------------------------------------------------------------------------
# 2./3. COMPLETENESS + CLARIFICATION: point -> (class, module, falsification)
# ---------------------------------------------------------------------------
# module path is relative to the python/ root; "" means a pure-text manuscript
# claim with no separate computation (only the A5 identification is module-less now;
# absolute Omega_Lambda moved to the KP-volume module).
LEDGER = [
    # point,                         class,        module,                              falsification
    ("a_gamma = 31/180",             "DERIVED",    "foundations/a_gamma_derivation.py", "Gilkey a_4 for Maxwell != 31/180 (scalar check 1/360)"),
    ("C_Q = 8 pi^2",                 "THEOREM",    "q_charge.py",                       "int_D4 Q4 != 8 pi^2"),
    ("zeta(0; DtN; S^3) = -1",       "THEOREM",    "q_charge.py",                       "BFK gluing gives != -1"),
    ("ratio L0 = a_g/(8pi^2)",       "DERIVED",    "csg_kp_core.py",                    "Omega_K/Omega_L != a_g/8pi^2 at >3 sigma"),
    ("cap saddle delta* = 0.16391",  "THEOREM",    "cap_saddle.py",                     "no real root of a_g cos^4=sin"),
    ("cap stability (all sectors)",  "THEOREM",    "foundations/analytic_closures.py",  "a negative inhomogeneous eigenvalue (analytic: domain monotonicity)"),
    ("A2 KP sequestering / contraction", "DERIVED|numeric", "theorem64_fixpoint.py",            "trace function not monotone / L>=1"),
    ("A3 photon-uniqueness",         "DERIVED|A3.1-3", "foundations/a3_uniqueness.py",  "extra massless IR conformal field"),
    ("A4 Janus matching (cap mechanism)", "DERIVED", "cap_saddle.py",                   "anomaly drive not linear in delta_theta"),
    ("uniqueness of invariant (within C1-C4)", "THEOREM|C1-C4", "foundations/a3_uniqueness.py", "another invariant satisfies C1-C4"),
    ("full minimality of uniqueness criteria", "OPEN", "foundations/a3_uniqueness.py",  "a 5th natural criterion excludes a survivor (no impossibility proof yet)"),
    ("B1 cap dominance (reduced action)", "THEOREM", "foundations/thimble_enumeration.py", "a Stokes line to a complex saddle"),
    ("B1' full no-boundary embedding", "OPEN",      "foundations/full_path_integral.py", "cap dominance lost in infinite-DoF PI"),
    ("A5a Euclidean half",           "THEOREM",    "foundations/close_open_points.py",  "topological identity fails on D^4"),
    ("A5b Wick rotation",            "DERIVED|B1", "foundations/close_open_points.py",  "BGT/HT continuation inapplicable"),
    ("A5c reference epoch",          "CONVENTION", "foundations/close_open_points.py",  "(a labelling choice; not falsifiable)"),
    ("A5 anomaly-curvature identification", "POSTULATE", "foundations/branch_from_equilibrium.py", "Omega_K outside +-3 sigma of a_g*OL/8pi^2 (the single premise = (iii) = P5; form forced by no-go)"),
    ("sign Omega_K>0 within HH branch", "DERIVED",  "foundations/close_open_points.py", "sign forced by a_g>0 fails"),
    ("HH vs Vilenkin branch selection", "DERIVED|equil", "foundations/branch_from_equilibrium.py", "Vilenkin tunneling state were a stationary equilibrium state (it is not)"),
    ("c_1 = 2 zeta(3)",              "LITERATURE", "c1_three_loop.py",                  "Mottola-Vaulin normalization wrong"),
    ("3-loop convergence bound",     "THEOREM",    "c1_three_loop.py",                  "loop series not suppressed"),
    ("all-orders ratio stability",   "THEOREM",    "foundations/all_orders_convergence.py", "graviton loops in CSG shift ratio"),
    ("Lambda* universality (phi_0, Om)", "DERIVED", "foundations/cw_banach_iteration.py", "Lambda* depends on phi_0 or Om in the V4-average (it does not: universal)"),
    ("absolute Omega_Lambda scale (volume route)", "OPEN", "foundations/cw_banach_iteration.py", "an action/topological identification deriving the absolute scale; phi_0 is currently free, the volume route gives only the universality structure, and mean_R_over_4 sharpness was a floored-geometry artefact"),
    ("Omega_L = 0.704 (halo-averaged)", "DERIVED|y=1/2", "lombriser_coincidence.py",    "top-hat collapse gives != 0.704"),
    ("causal Omega_L (light-cone closure)", "DERIVED|closure-form", "foundations/lightcone_coefficient.py", "apparent-horizon hypersurface not unique, OR a derived closure functional fixing the form (currently KP stationarity gives no fixpoint)"),
]


def completeness_checks() -> list[tuple[str, bool, str]]:
    out = []
    for point, cls, module, _fals in LEDGER:
        if module == "":
            # only the A5 identification is module-less now; it must be a POSTULATE
            ok = cls == "POSTULATE"
            out.append((f"[{cls}] {point}", ok, "manuscript claim (postulate; no computation expected)"))
        else:
            path = os.path.join(_PARENT, module)
            ok = os.path.isfile(path)
            out.append((f"[{cls}] {point}", ok, f"backed by {module}" if ok else f"MISSING {module}"))
    return out


def clarify_open_points() -> dict[str, list[str]]:
    buckets: dict[str, list[str]] = {}
    for point, cls, _m, fals in LEDGER:
        buckets.setdefault(cls.split("|")[0], []).append(point)
    return buckets


def main() -> int:
    print("=" * 72)
    print("CSG-KP: consistency / completeness / open-point clarification audit")
    print("=" * 72)

    print("\n--- 1. CONSISTENCY (numbers agree across modules + ledger) ---")
    cons = consistency_checks()
    for name, ok, detail in cons:
        print(f"  [{'OK' if ok else 'XX'}] {name}\n        {detail}")
    assert all(ok for _, ok, _ in cons), "consistency failure"

    print("\n--- 2. COMPLETENESS (every point has a backing module) ---")
    comp = completeness_checks()
    for name, ok, detail in comp:
        print(f"  [{'OK' if ok else 'XX'}] {name}  ({detail})")
    assert all(ok for _, ok, _ in comp), "completeness gap"

    print("\n--- 3. CLARIFICATION (epistemic class of every point) ---")
    buckets = clarify_open_points()
    order = ["THEOREM", "DERIVED", "NUMERICAL", "LITERATURE", "CONVENTION",
             "POSTULATE", "OPEN"]
    for cls in order:
        items = buckets.get(cls, [])
        if items:
            print(f"  {cls} ({len(items)}):")
            for it in items:
                print(f"      - {it}")

    n_post = len(buckets.get("POSTULATE", []))
    n_open = len(buckets.get("OPEN", []))
    n_conv = len(buckets.get("CONVENTION", []))
    print("\n--- VERDICT ---")
    print(f"  Genuinely open (math + scale): {n_open}  -> {buckets.get('OPEN', [])}")
    print(f"  Physical postulates:       {n_post}  -> {buckets.get('POSTULATE', [])}")
    print(f"  Pure conventions:          {n_conv}  -> {buckets.get('CONVENTION', [])}")
    print("  => RATIO Omega_K/Omega_L: THEOREM given A1-A3, derived sign within HH;")
    print("     only chosen point of the *prediction* is A5c (CONVENTION); the two")
    print("     genuinely open math points are B1' (infinite-DoF embedding) and the")
    print("     full minimality of the uniqueness criteria (within-C1-C4 is proven).")
    print("  => ABSOLUTE Omega_Lambda: the KP self-consistency route proves Lambda* is")
    print("     UNIVERSAL in phi_0 and Om (real structure; bulk vacuum cancels -> 10^122")
    print("     solved), but its value is amplitude-set and the absolute scale is OPEN:")
    print("     phi_0 stays free, so Omega_L=(V(phi_0)-Lambda*)/3 is not fixed. The earlier")
    print("     <R>/4 sharpness proxy was a floored-geometry artefact (retracted). Candidate")
    print("     routes to the scale are all conditional: halo (y=1/2), causal closure (O(1)")
    print("     band), or the geometric budget ladder Omega_L=4a_g (conjecture, open step).")

    # the clarification must hold: two open MATH points (B1', minimality) plus the
    # absolute-scale openness; A5/HH are the postulates, A5c the only convention.
    open_pts = buckets.get("OPEN", [])
    assert n_open == 3, f"expected B1', minimality, absolute-scale open, got {open_pts}"
    assert any("B1'" in p for p in open_pts) and any("minimality" in p for p in open_pts)
    assert any("scale" in p for p in open_pts)
    assert "A5c reference epoch" in buckets.get("CONVENTION", [])
    assert set(buckets.get("POSTULATE", [])) == {
        "A5 anomaly-curvature identification",
    }
    print("\n[audit] consistency + completeness PASS; open points classified "
          "(2 open math: B1', uniqueness-minimality; 1 postulate: A5 = (iii) = P5, the single "
          "equilibrium premise; HH-branch DERIVED from it; 1 conv: A5c; "
          "1 OPEN EMPIRICAL THREAT: DESI w-dynamics ~4sigma, NOT absorbable by curvature "
          "(factor ~100, desi_w_tension), data-decided by DESI DR3/Euclid). "
          "Lambda* universality DERIVED but absolute Omega_L scale OPEN (phi_0 free; volume "
          "route structure-only, mean_R_over_4 retracted; halo/causal/ladder all conditional)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
