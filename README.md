# CSG-KP: A Conformal-Anomaly Resolution of the Cosmological Constant Problem

A self-contained package addressing the three faces of the cosmological constant
problem -- magnitude, value, and coincidence -- with a parameter-free curvature
fingerprint as the sharp falsifiable output:

```
|Omega_K| / Omega_Lambda  =  a_gamma / (8 pi^2)  =  31 / (1440 pi^2)  ~  2.181e-3
```

The magnitude problem is handled by Kaloper-Padilla sequestering; the value
problem by a self-consistency result (Lambda is a fixed point of the
four-volume averaging map, not a free parameter; uniqueness rests on a Banach
contraction established numerically); the coincidence problem by
structure-formation (halo-weighted) averaging following Lombriser, which returns
Omega_Lambda ~ 0.704 conditional on an anthropic-like prior. That value is Lombriser's
own mechanism, not the CSG prediction: the framework's own budget
ladder points to Omega_Lambda = 4 a_gamma = 0.6889, coinciding with Planck+BAO to
four decimals -- an empirical coincidence, not a proof; the absolute value rests on
the open holographic-saturation conjecture P5 (see manuscript).
The two inputs of the ratio -- the photon type-A anomaly `a_gamma = 31/180` and the
hemisphere Q-curvature charge `8 pi^2` -- contain no scale, no Newton constant, no
Planck mass. The manuscript integrates the rigorous spectral backbone (twelve
results R1-R12, the BFK gluing identity, cap-saddle stability, boundary refinement)
and an independent recomputation (M1) directly into a single coherent document.

## Contents

```
manuscript/
  csg_kp_facharbeit.tex     LaTeX source (article, self-contained bibliography)
  csg_kp_facharbeit.pdf     compiled manuscript (40 pp; single coherent document, all rigorous calculations integrated into the main text, no separate appendix)

python/
  csg_kp_core.py            constants + central prediction (L0/L1/L3), DESI pull
  q_charge.py               C_Q = 8 pi^2 (sympy); zeta(0; DtN) = -1 (direct cap spectrum + BFK cross-check)
  cap_saddle.py             exact cap-saddle + Hessian stability (3 sectors)
  c1_three_loop.py          c_1 = 2 zeta(3), A_M5, three-loop convergence bound
  theorem64_fixpoint.py     KP self-consistency: trace-zero, closed history, CW vacuum
  lombriser_coincidence.py  structure-formation averaging -> Omega_Lambda = 0.704
  run_all.py                runs every module and prints a PASS/FAIL summary
  foundations/
    a_gamma_derivation.py     a_gamma = 31/180 from Gilkey b_4 on S^4 (scalar check 1/360)
    analytic_closures.py      cap stability (domain monotonicity) + A2 contraction (G'<0)
    thimble_enumeration.py    B1' complete thimble enumeration (degree-8 reduction; n_complex=0)
    full_path_integral.py     semiclassical embedding into full no-boundary path integral
    all_orders_convergence.py all-orders stability of R=a_gamma/(8pi^2) (CSG; topological ratio)
    close_open_points.py      B1' one-loop + 2D embedding, GHP conformal mode, sign sector, A5c
    a3_uniqueness.py          A3 photon-uniqueness: Banach FP + KS monotonicity + 26-mechanism
    shawbarrow_causal.py      causal legitimation (Shaw-Barrow): scale t_L/t_U=0.73, Omega_k0, hierarchy
    coincidence_measure.py    measure problem: collapse-time lever, recollapse (a_max~6.5e17), HH spread 0..1
    kp_volume_selfconsistency.py  KP four-volume route: topological 4 a_g + <rho_total> a_max-stable (solid); mean_R_over_4 sharpness proxy is a floored-geometry artefact (retracted)
    cw_banach_iteration.py    correct CW dynamics: documents the mean_R_over_4 bug; Lambda* universal in phi_0 and Om (structure) but amplitude-set, absolute Omega_Lambda (phi_0) free
    budget_ladder.py          geometric 2^n pi^2 ladder: Omega_L=4a_g (leading), Omega_K=a_g^2/2pi^2 (subleading) joined by int E_4(D^4)=32pi^2; ladder exact + Planck match, DE action-identification open (conjecture)
    lightcone_coefficient.py  causal closure: apparent-horizon hypersurface forced (r*H=1); functional form NOT forced (KP/thermo fail, closures spread 0.49..0.96) -> O(1) band
    schwinger_keldysh_p5.py   in-in localization of P5: anomaly Adler-Bardeen exact (proven); lift N_eff=(M_Pl/H)^2 = Cohen-Kaplan-Nelson UV-IR bound, NOT a mode sum; CKN = Schwarzschild consistency (gravity, fixes 10^-122 magnitude) + saturation (assumption P5, c^2=4a_g); localizes P5, does not prove it
    ratio_vs_absolute_scope.py CENTRAL re-evaluation: ratio Omega_K/Omega_L=a_g/8pi^2 scale-invariant (H,M_Pl cancel) -> theorem core HOLOGRAPHY-FREE; absolute Omega_L=4a_g not scale-invariant -> needs P5=CKN saturation; falsifiable Euclid prediction robust against unproven holography; conjectural bonus flagged
    action_density_bridge.py  lift prefactor COMPUTED = A/G (Bekenstein-Hawking horizon dof); Omega_L=(A/G)rho_anom/rho_crit=4a_g exact; coherence FORCED (sqrt(N) excluded); P5 accumulation principle remains; prefactor no longer uncomputed (line 927-930)
    desitter_saddle.py        full dS analysis vs manuscript: 4 over-determined (chi-linear R1); dynamical route = Mechanism 2; MEASURE PROBLEM causally resolved (sec:causal+A1); open = action-vs-density on S^4 (line 927-930); ratio intact
    falsification_suite.py    one falsification criterion per claim (PASS = survived; not proof)
    axiom_status_audit.py     consistency + completeness + open-point ledger

cobaya_integration/
  csg_kp_theory.py          constants module (a_gamma, C_Q, L0, L1); curvature
                            enforced via YAML reparametrization (see folder README)
  csg_kp_cobaya.yaml        MCMC config (Planck 2018 plik_lite + DESI DR2 BAO, CAMB)
  run_mcmc.py               driver (--dry-run / --test-likelihood / --resume)
  analysis/plot_posterior.py  getdist post-processing
```

## Running

```
pip install -r requirements.txt   # Python 3.10+ required; verified on 3.12.3

cd python
python3 run_all.py                 # all modules; expects 37/37 PASS (~3 min; cap_saddle.py alone ~100 s)
python3 verify_clean_pipeline.py   # independent re-verification + proven/assumed dependency graph
python3 foundations/falsification_suite.py   # 16/16 falsification checks
```

Dependencies: `numpy`, `scipy`, `sympy`, `mpmath`. The Cobaya plugin additionally
requires `cobaya`, `camb`, `getdist` and the Planck/DESI likelihood data (see
`cobaya_integration` and `run_mcmc.py --dry-run`).

The manuscript compiles with `pdflatex` (run twice to resolve all cross-references);
it uses only standard packages and an embedded
bibliography, so no `bibtex` step is needed.

## Honest status ledger

The package separates what is proven from what is assumed. Each Python module
ends with a STATUS block stating the same.

| Component | Status |
|---|---|
| Q-charge `int_{D^4} Q_4 = 8 pi^2` | proven (elementary) |
| Spectral results R1-R12 | proven (spectral computation) |
| DtN zeta values (R2/R4/R8) | scalar DtN `mu_l=l(l+2)/(l+1)`, mult `(l+1)^2` -> `zeta(0)=-1` (direct + BFK cross-check); transverse 1-form `mu_l=l+1`, mult `2l(l+2)` -> `zeta(0)=1`; gauge-fixed Maxwell = 1-form - 2 ghost -> `zeta(0)=3` (R4), `det'=1/(2pi^3)` (R8). Manuscript spectrum statements corrected: R2 was `l` (gives -2/3, wrong), R8 stated Maxwell as the single 1-form spectrum (gives `zeta(0)=1`, `det'~0.169`, wrong) -- values 3 and 1/(2pi^3) hold only via the combination. None enter the central ratio. |
| Hemisphere ratio `a_gamma/(8 pi^2)` (L0) | proven (topological identity) |
| Exact cap-saddle `dtheta* = 0.16391` (L1) | proven (saddle equation) |
| Cap-saddle stability (all sectors) | proven analytically (domain monotonicity + closed-S^4 spectrum) |
| Boundary refinement (BFK odd-function symmetry) | proven |
| Uniqueness of the invariant (26-mechanism exhaustion) | proven within criteria (i)-(iv); full minimality open |
| KP sequestering (magnitude problem) | derived within CSG (Built-in via Stueckelberg compensator, proof sketch); full all-orders rigor pending |
| KP self-consistency: trace-zero, closed history, CW vacuum | numerically established (structural; sign G'<0 analytic, |G'| bound numerical) |
| Three-loop convergence bound `~4.3e-14` | proven |
| `a_gamma = 31/180` | derived (Gilkey b_4 on S^4; scalar check 1/360) |
| `c_1 = 2 zeta(3)` | literature-supported (Mottola-Vaulin 2006) |
| KP fixed point `Lambda*` (3H0^2 units) | universal in phi_0/Om (structure proven, cw_banach_iteration) but amplitude-set (~-0.10 for A_CW, not -0.691); the mean_R_over_4 sharpness proxy was a floored-geometry artefact (retracted) |
| Absolute `Omega_Lambda` (homogeneous average) | NOT fixed by the volume/self-consistency route (phi_0 free); calibrated only |
| `Omega_Lambda = 0.704` (Lombriser halo-weighted) | Lombriser's own mechanism, conditional on `y(t_0)=1/2` -- not the CSG prediction |
| Geometric budget ladder `Omega_L=4a_g`, `Omega_K=a_g^2/2pi^2` | conjecture: ladder algebra exact (`Omega_K*32pi^2=Omega_L^2`, `32pi^2=int E_4(D^4)`), Planck match within 1 sigma; rests on the open DE action-identification `Omega_L=int<T>(S^4)` (not derived; energy-density route gives only the ratio) |
| A5a (topological ratio `a_gamma/8pi^2`) | theorem (Cauchy + Chern-Weil + APS) |
| A5b (Wick-rotation kinematics) | derived (saddle-point, conditional on B1) |
| A5c (reference-state choice) | specification: the only genuinely chosen element, data-anchored |
| Scope split (core vs bonus) | CC-problem splits cleanly: CORE = ratio Omega_K/Omega_L=a_g/8pi^2 is scale-invariant (H AND M_Pl cancel), epoch-invariant, value topological (A5a theorem), needs P5 only as EXISTENCE of the (M_Pl/H)^2 lift not its magnitude -> HOLOGRAPHY-FREE, Euclid-falsifiable; BONUS = absolute Omega_L=4a_g is NOT scale-invariant (epoch-dependent, carries phi_0), needs P5=CKN saturation. Holography problem confined to the BONUS only. Scale-invariance forces only the ratio; deriving absolute-value saturation from it is a fallacy. (ratio_vs_absolute_scope.py) |
| P5 localization (Schwinger-Keldysh) | in-in trace anomaly Adler-Bardeen one-loop exact (proven); local fraction (a_g/8pi^2)(H/M_Pl)^2 ~ 10^-125 (122 orders too small); lift N_eff=(M_Pl/H)^2 is the Cohen-Kaplan-Nelson UV-IR bound (rho_L<=M_Pl^2/L^2), NOT an in-in mode sum. CKN = (i) Schwarzschild consistency (follows from gravity, fixes the 10^-122 magnitude, NOT a postulate) + (ii) saturation (the assumption P5, c^2=4a_g). SK PROVES (i), localizes P5 as named CKN principle (ii); does NOT prove saturation -- that is the microscopic-holography problem of all physics. Progress, not closure. (schwinger_keldysh_p5.py) |
| Holography problem (P5/CKN saturation) | NOT solvable within CSG: it is the general emergent-gravity/holography problem. CSG can only (a) confine it to the absolute-value bonus (core is free of it) and (b) reframe it (emergent M_Pl makes CKN the content of gravity, not external) -- shifting "why saturation" to "is gravity emergent-holographic", an independent active hypothesis (Padmanabhan/Verlinde), not decidable in CSG alone. (ratio_vs_absolute_scope.py, schwinger_keldysh_p5.py) |
| Absolute value 4 a_gamma (full dS + action-density bridge, vs manuscript) | factor 4 chi-linear (R1: -2a_g per Euler unit); |zeta(0)|=int<T>=2a_g*chi is ONE invariant computed two ways (spectral zeta = topological Euler), a consistency check NOT an independent over-determination; D^4->2a_g, S^4->4a_g; dynamical action saddle = Mechanism 2 (V_4); MEASURE PROBLEM CAUSALLY RESOLVED (sec:causal past light cone = D^4 needs no anthropic weighting) + no-boundary geometry split A1 (S^4 substrate -> absolute Omega_L, D^4 -> ratio); ACTION-DENSITY BRIDGE PREFACTOR COMPUTED = A/G (Bekenstein-Hawking horizon dof, 32pi^2(M_Pl/H)^2 = 4 S_dS), Omega_L=(A/G)rho_anom/rho_crit = 4a_g exact, coherence FORCED by scale-freeness (sqrt(N) ~ H/M_Pl excluded). HONEST caveats: (W1) A/G is NOT independent of the chi route -- both share int E_4/C_Q (64/16=32/8), so A/G is a physical re-expression, not a 2nd derivation; (W2) factor 4 = dof-count A/G vs entropy S_dS is part of P5 (N=S_dS->a_g, A/G=4S_dS->4a_g). The manuscript-flagged uncomputed prefactor (line 927-930) is now computed; REMAINS assumption: the holographic accumulation principle P5 (rho_L=(A/G)rho_anom). NOT a theorem. Ratio a_g/8pi^2 untouched (desitter_saddle.py, action_density_bridge.py) |
| A2 (IR fixed point) | numerically established (Banach contraction; sign G'<0 analytic, |G'|<2 bound numerical) |
| A2 as an RG-flow attractor | retracted (not required; topology replaces it) |
| Curvature sign `Omega_K > 0` (open) | forced by sign(a_gamma)>0: unique cap saddle dth*>0, weighting-independent |
| Euclidean fluctuation stability | resolved (GHP rotation): conformal mode rotated, transverse modes positive (B1') |
| Euclidean vs Lorentzian definition | open (interpretational): FLT debate; not CSG-KP-specific |
| B1 (cap dominance, reduced action) | established analytically (n_complex=0; no Stokes line; gap >7e5) |
| B1' (cap + scalar embedding) | complete (degree-8 polynomial reduction, both phi-branches; Picard-Lefschetz => n_complex=0 rigorous) |
| Full no-boundary path integral | assembled semiclassically (1-loop det = -4 a_gamma; Type-A Adler-Bardeen exact; n_complex=0) |
| All-orders stability of R=a_gamma/(8pi^2) | proven within CSG (no graviton loops; ratio of hbar-independent invariants); absolute phi^4 Borel decoupled/open |

After the A5 decomposition the observable prediction reduces to a single genuinely
chosen element (the data-anchored reference state A5c) plus the embedding B1'. The
topological core (A5a, the self-consistency fixed point A2, cap dominance B1 on the
reduced action) is theorem-level; the redshift-constancy of the ratio is topological
(Komargodski-Schwimmer), so the retracted RG-attractor reading of A2 does not bear on it.

## Falsifiability

- `Omega_K` outside +/- 3 sigma of `a_gamma * Omega_Lambda / (8 pi^2)` refutes the relation.
- A robust detection of a closed universe (`Omega_K < 0`) refutes the sign prediction.
- A measured redshift dependence of `Omega_K(z)/Omega_Lambda(z)` refutes its topological constancy.

Current status: DESI DR2 + Planck give `Omega_K = +0.0023 +/- 0.0011`, a 0.72 sigma
(L0) / 0.79 sigma (L1) pull, on the open side. DESI DR3 (~2027) reaches the
decisive `~5 sigma` test of the central value.
