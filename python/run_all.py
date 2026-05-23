#!/usr/bin/env python3
"""
run_all.py  --  Run every CSG-KP module and report a PASS/FAIL summary.

Executes each standalone module as a subprocess (so each runs its own __main__
self-test and assertions) and prints a one-line verdict per module plus the
headline numbers of the framework.  Exit code is non-zero if any module fails.

Usage:  python3 run_all.py
"""
from __future__ import annotations
import subprocess
import sys
import time
from pathlib import Path

MODULES = [
    ("foundations/a_gamma_derivation.py", "a_gamma = 31/180 derived from Gilkey b_4 (scalar check 1/360)"),
    ("foundations/analytic_closures.py", "cap stability (domain monotonicity) + A2 contraction (G'<0)"),
    ("foundations/thimble_enumeration.py", "B1' complete thimble enumeration (degree-8 reduction; n_complex=0)"),
    ("foundations/full_path_integral.py", "semiclassical embedding into full no-boundary path integral (1-loop exact, Type-A)"),
    ("foundations/all_orders_convergence.py", "all-orders stability of R=a_g/(8pi^2) (CSG no graviton loops; topological ratio)"),
    ("foundations/close_open_points.py", "B1' one-loop + 2D embedding, GHP conformal mode, sign sector, A5c epoch"),
    ("foundations/a3_uniqueness.py", "A3 photon-uniqueness: Banach FP + KS monotonicity + 26-mechanism (given A3.1-3)"),
    ("foundations/shawbarrow_causal.py", "causal legitimation (Shaw-Barrow): scale t_L/t_U=0.73, Omega_k0=-0.0056, hierarchy"),
    ("foundations/lightcone_coefficient.py", "causal closure: apparent-horizon hypersurface FORCED (r*H=1); functional form NOT forced (KP/thermo fail, closures spread 0.49..0.96) -> O(1) band, not a sharp value"),
    ("foundations/coincidence_measure.py", "measure problem: collapse-time lever, recollapse (a_max~6.5e17), HH-measure spread 0..1"),
    ("foundations/kp_volume_selfconsistency.py", "KP four-volume route: topological 4 a_g + <rho_total> a_max-stable (solid); the mean_R_over_4 sharpness proxy is a floored-geometry artefact (see cw_banach_iteration); ratio theorem-level"),
    ("foundations/cw_banach_iteration.py", "correct CW Banach iteration: documents the mean_R_over_4 floored-H^2 bug; Lambda* universal in phi_0 and Om (structure) but amplitude-set, absolute Omega_Lambda (phi_0) free"),
    ("foundations/budget_ladder.py", "geometric 2^n pi^2 ladder: Omega_L=4a_g (leading), Omega_K=a_g^2/2pi^2 (subleading) joined by int E_4(D^4)=32pi^2; ladder exact + Planck match, DE action-identification open (conjecture)"),
    ("foundations/spectral_coherence.py", "coherent spectral accumulation: linear sum over fixed Maxwell eigenmodes (Allen/Higuchi) = coherence; N_eff~(M_Pl/H)^2 lifts local anomaly to N_eff*rho_anom/rho_crit=a_g/8pi^2 (1e-122 gap CLOSED for the testable Omega_K); absolute value via 32pi^2=int E_4(D^4) -> 4a_g, value fixed cutoff-free by zeta(0)+Riegert (prefactor bypassed); identification + epoch OPEN"),
    ("foundations/absolute_value_audit.py", "no-go by exhaustion: every dynamical route to the absolute value gives a different number (1e-122, 1/2, 0.484, 0.93, 14, ...), only the action invariant int<T>=4a_g gives 4a_g -> 4a_g is action-invariant not dynamical; identification sharpened to single normalization N_eff=S_dS/C_Q (entropy per Q-charge); still conjecture, not closed"),
    ("foundations/cross_framework_anchor.py", "reverse bootstrap: CSG supplies the number established frameworks postulate. HDE density form rho=3c^2 M_Pl^2/L^2 + c^2=4a_g + Hubble cutoff -> Omega_L=4a_g as a DENSITY (resolves action-vs-density, point A; caveat: w=0 Hsu, needs DM-DE interaction for w=-1 + coincidence); equipartition factor 4=chi(S^4)^2; CosMIn not extractable (absolute scale, not fraction). 4a_g anchored in 3 independent frameworks"),
    ("foundations/running_vacuum_interaction.py", "the DM-DE interaction is NOT a new parameter: the generalized Bianchi identity forces vacuum-matter exchange once the vacuum runs (Sola-Peracaula RVM; Bilic et al.), strength nu = beta-function coefficient of the running CC = anomaly. CSG: nu = a_g/(8pi^2) = the curvature ratio (no new parameter), inside RVM fit band; bypasses Hsu (w_eff=-1 from running vacuum). Caveats: exact nu_v(massless vector) not yet derived; CMB/LSS test open. Point B reduced to the anomaly number, not closed"),
    ("foundations/unified_open_point.py", "attacking the two open steps shows they are ONE: the massless photon gives NO O(H^2) RVM term (nu_v=0), only the O(H^4) anomaly; the P5 accumulation N_eff=(M_Pl/H)^2 lifts O(H^4)->O(H^2) giving Friedmann fraction a_g/8pi^2 (curvature ratio), and the Hubble cutoff IS that horizon scale. So absolute value (A) and interaction (B) both reduce to the single P5 holographic accumulation; K1-K3 (esp. Riegert flow=4a_g, same int E_4 anchor) support both. Reduction from two assumptions to one, not a closure"),
    ("foundations/coherence_from_condensate.py", "attacking P5 coherence: the xN-vs-sqrt(N) question (P5's substantive part) is reduced to Mottola's anomaly-EFT condensate. The anomaly vacuum energy is a CONDENSATE of a 4-form F=dA (single coherent amplitude, homogeneous) -> adds linearly (xN); sqrt(N) needs random phases a condensate lacks. Accumulation sits at the horizon (IR-relevant action), value set by horizon boundary conditions not UV. Mottola Lambda->0 = sequestering of bare term; finite 4a_g = anomaly residual (consistent). OPEN: exact O(1) of N_eff; CAVEAT: structural argument not explicit SK/BV, conformalon EFT not universal. Coherence reduced from postulate to condensate consequence"),
    ("foundations/horizon_normalization.py", "Mottola's open normalization closed by CSG (reverse): Mottola gives the mechanism but leaves the value as a horizon boundary condition and the conformal theory unspecified. CSG supplies both: N_eff = S_dS/C_Q = (M_Pl/H)^2 with O(1) factor EXACTLY 1 (de Sitter entropy S_dS=8pi^2(M_Pl/H)^2 and Q-charge C_Q=8pi^2 share the 8pi^2 normalization), conformal theory = photon (a_g=31/180), finite value Omega_L=4a_g (anomaly residual Mottola's Lambda->0 omits). P5 := N_eff=S_dS/C_Q is the explicit founding assumption (entropy per Q-charge); given it the framework is internally complete, falsified by DESI/Euclid"),
    ("foundations/p5_entanglement_anchor.py", "P5 anchored in established results: its area scaling N_eff=(M_Pl/H)^2 IS the entanglement area law (Bekenstein-Hawking/Ryu-Takayanagi); its vacuum-entanglement<->CC link IS Jacobson's entanglement equilibrium, EXACT for conformal fields -- and the photon is conformal (Komargodski-Schwimmer IR endpoint), so it applies to CSG's substrate exactly (lifts K1 from motivation to theorem). Max-symmetric causal diamond = de Sitter with CC = cap saddle (Jacobson-Visser, negative temperature = Hartle-Hawking). Coherence = Verlinde's strict-area-law condition. The VALUE 4a_g remains CSG's own (Jacobson leaves Lambda free); an assumption-free theorem-with-value is absent in the literature too. P5 = application of established results to the photon, not an isolated postulate"),
    ("foundations/jacobson_premises.py", "P5 reformulated as Jacobson's entanglement-equilibrium theorem with its premises supplied by CSG: (i) the universal EE coefficient = type-A anomaly (Solodukhin/Casini-Huerta, topological for the spherical hemisphere; Maxwell edge-mode recovery runs through the S^4 partition function = CSG's zeta(0)=-4a_g); (ii) the nonconformal conjecture that Casini-Galante-Myers find conflicts at low Delta is voided because Komargodski-Schwimmer leaves only the conformal photon in the IR. Premise (iii) (vacuum = entanglement equilibrium) is concretized as the cap-saddle and TRIANGULATED by five convergent pipeline results: cap saddle dtheta*, action invariant int<T>=4a_g, Riegert flow=4a_g (independent route, converges), N_eff=S_dS/C_Q, KP constraint = Jacobson-Visser first law. P5 = theorem with (i),(ii) derived and (iii) triangulated -- a qualitative jump from isolated postulate, NOT an assumption-free closure ((iii) stays a physical premise, Maxwell edge modes debated, first order)"),
    ("foundations/desi_w_tension.py", "two honest corrections forced by re-examination: (1) the topologically constant object is the ACTION-PARAMETER ratio R=3|K|/Lambda=a_g/8pi^2, NOT the density parameters -- Omega_K/Omega_L = R/a^2 redshifts as (1+z)^2, so the falsification test is the PRESENT-EPOCH ratio Omega_K^(0)/Omega_L^(0)=R, not a measured redshift dependence (which Friedmann guarantees); (2) the DESI w-dynamics tension is NOT cleared by curvature -- opening to Omega_K=+1.5e-3 shifts effective w0 by only ~2e-3 vs DESI's 0.25..0.6 (factor ~100..300 too small), and nu=a_g/8pi^2 is equally small. TWO DESI tensions: curvature (~1.8sigma) and w (~4sigma if real), the second NOT explained by the first. Open empirical threat, decided by DESI DR3/Euclid. Supersedes the over-claimed objection-6"),
    ("foundations/desitter_saddle.py", "full dS analysis cross-checked vs manuscript: factor 4 over-determined (chi-linear, R1: -2a_g per Euler unit, 2 routes); dynamical route fails = Mechanism 2 (V_4); MEASURE PROBLEM CAUSALLY RESOLVED (sec:causal past light cone = D^4, no anthropic weight) + geometry split A1 (S^4 substrate -> 4a_g, D^4 -> ratio); one open step = action-vs-density on S^4 (line 927-930, A5 does not provide); ratio intact"),
    ("foundations/action_density_bridge.py", "full action-density bridge: lift prefactor COMPUTED = A/G (Bekenstein-Hawking horizon dof, 32pi^2(M_Pl/H)^2=4 S_dS), Omega_L=(A/G)rho_anom/rho_crit=4a_g exact; coherence FORCED by scale-freeness (sqrt(N) gives ~H/M_Pl, excluded); remaining assumption = holographic accumulation principle P5; prefactor no longer uncomputed (manuscript line 927-930); ratio intact"),
    ("foundations/schwinger_keldysh_p5.py", "in-in localization of P5: trace anomaly Adler-Bardeen exact (proven); lift N_eff=(M_Pl/H)^2 is NOT a mode sum but the Cohen-Kaplan-Nelson UV-IR bound; CKN splits into Schwarzschild consistency (follows from gravity, fixes magnitude 10^-122) + saturation (the assumption P5, c^2=4a_g); SK localizes P5 as a named principle, does NOT prove it"),
    ("foundations/ratio_vs_absolute_scope.py", "central re-evaluation: ratio Omega_K/Omega_L=a_g/8pi^2 is scale-invariant (H AND M_Pl cancel) -> theorem core is HOLOGRAPHY-FREE, P5 needed only as existence of lift not its magnitude; absolute Omega_L=4a_g is NOT scale-invariant -> needs P5=CKN saturation; scale-invariance forces only the ratio (deriving saturation from it is a fallacy); falsifiable Euclid prediction robust against unproven holography"),
    ("foundations/branch_from_equilibrium.py", "shrinking the honest boundary: (1) the Hartle-Hawking vs Vilenkin branch is NOT an independent postulate -- given the equilibrium premise the max-symmetric vacuum is Bunch-Davies/HH (Gibbons-Hawking thermal equilibrium; Carroll rho~e^{-beta H} stationary) and Vilenkin is out-of-equilibrium, so HH FOLLOWS (caveat: only given the premise, de Alwis); (2) A5 (anomaly=curvature), (iii) (vacuum=equilibrium) and P5 (N_eff=S_dS/C_Q) are ONE postulate in three faces (absolute_value_audit proved Omega_L=4a_g <=> P5). The no-go (no dynamics gives 4a_g, only the action invariant does) makes the premise NECESSARY IN FORM (must be a stationarity principle), not arbitrary. Ledger: 2 postulates -> 1; smaller honest boundary = ONE equilibrium postulate + one triangulated identity, NOT a first-principles closure"),
    ("foundations/falsification_robustness.py", "robustness against a serious falsification attempt: six of seven objections are forced or cleared, leaving exactly one postulate. (1) sign Omega_K>0 forced by a_g>0 (cap saddle, closed needs a_g<0); (2) factor 4 = zeta(0)/a_g spectrally forced (BFK), not numerology; (3) no-go is a FEATURE -- Omega_K is a topological ratio, Friedmann derivation is a category error; (4) Maxwell -16/45 vs -31/45 = edge mode, measured by DtN det (zeta(0;DtN;Max;S^3)=3=dim S^3, Z_edge), independent lattice-QED prediction; (5) graviton excluded (non-conformal Lichnerowicz + circular geometry + only chi on D^4), photon unique massless conformal field; (6) DESI w0wa = Omega_K=0 artefact via Omega_K-w0 degeneracy, nu=a_g/8pi^2 keeps w_eff=-1 (CAVEAT: full refit open). The one remaining is the single postulate A4=A5=(iii)=P5; falsification confirmed the boundary, did not widen it"),
    ("foundations/falsification_suite.py", "falsification pass: one criterion per claim (PASS=survived)"),
    ("foundations/axiom_status_audit.py", "consistency + completeness + open-point ledger (2 open math; 2 postulates; 1 conv A5c)"),
    ("csg_kp_core.py", "constants + central prediction (L0/L1/L3, DESI pull)"),
    ("q_charge.py", "C_Q = 8 pi^2  and  zeta(0; DtN) = -1"),
    ("cap_saddle.py", "exact saddle + Hessian stability (3 sectors)"),
    ("c1_three_loop.py", "c_1 = 2 zeta(3), A_M5, 3-loop convergence"),
    ("theorem64_fixpoint.py", "KP self-consistency: trace-zero, closed history, CW vacuum"),
    ("lombriser_coincidence.py", "structure-formation averaging -> Omega_Lambda = 0.704"),
]


def run(module: str) -> tuple[bool, float, str]:
    here = Path(__file__).resolve().parent
    t0 = time.time()
    proc = subprocess.run([sys.executable, str(here / module)],
                          capture_output=True, text=True)
    dt = time.time() - t0
    ok = proc.returncode == 0
    tail = (proc.stdout.strip().splitlines() or [""])[-1] if ok else \
        (proc.stderr.strip().splitlines() or [""])[-1]
    return ok, dt, tail


def main() -> int:
    print("=" * 72)
    print("CSG-KP framework: full reproduction run")
    print("=" * 72)
    results = []
    for module, desc in MODULES:
        ok, dt, tail = run(module)
        verdict = "PASS" if ok else "FAIL"
        print(f"  [{verdict}] {module:24s} {dt:6.1f}s  {desc}")
        if not ok:
            print(f"         -> {tail}")
        results.append(ok)

    n_ok = sum(results)
    print("-" * 72)
    print(f"  {n_ok}/{len(results)} modules passed.")
    print("  NB: 'passed' = the module ran and its assertions held WHERE PRESENT. Several")
    print("  foundations modules are argument/reduction essays without numerical assertions")
    print("  (they 'pass' by running); their content is reasoning, not a verified numerical")
    print("  test. The hard numerical checks are concentrated in: csg_kp_core, q_charge,")
    print("  cap_saddle, a_gamma_derivation, analytic_closures, cw_banach_iteration,")
    print("  budget_ladder, desi_w_tension, lombriser_coincidence, falsification_suite.")
    print("\n  Central result (proven ratio):")
    print("    |Omega_K| / Omega_Lambda = a_gamma/(8 pi^2) = 31/(1440 pi^2) ~ 2.181e-3")
    print("  Conditional on postulate A5 (anomaly-curvature correspondence) and the")
    print("  open-branch sign. The MAGNITUDE of this ratio is structural: the")
    print("  coherent spectral sum (linear over the fixed Maxwell eigenmodes) lifts the")
    print("  local anomaly to N_eff*rho_anom/rho_crit = a_g/8pi^2, closing the 1e-122 gap")
    print("  for the testable Omega_K (spectral_coherence). The ABSOLUTE Omega_Lambda is")
    print("  NOT fixed: the volume/self-consistency route gives a universal but")
    print("  amplitude-set Lambda* with phi_0 free (cw_banach_iteration); the geometric")
    print("  budget ladder (Omega_L=4a_g) matches Planck but rests on the open DE")
    print("  action-identification Omega_L=|zeta(0)| (budget_ladder/spectral_coherence)")
    print("  and the epoch coincidence -- a conjecture, not a proof, and not a DESI question.")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
