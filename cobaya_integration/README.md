# CSG-KP Cobaya plugin

Tests the CSG-KP curvature relation
`Omega_K = sign * (a_gamma/8 pi^2) * Omega_Lambda` against Planck 2018 + DESI DR2
BAO, by FIXING the curvature-to-dark-energy ratio (not letting `Omega_K` float).

## How the constraint is imposed
The ratio is fixed; `Omega_K` is reparametrized in the YAML as a deterministic
function of the sampled cosmology:

```
Omega_K = csg_kp_sign * csg_kp_ratio * (1 - Omega_m) / (1 + csg_kp_sign * csg_kp_ratio)
```

All inputs to `Omega_K` (`csg_kp_ratio`, `csg_kp_sign`, the auxiliary `_omegam_in`)
are INPUT parameters, so the dependency graph resolves before CAMB is called.
This is the robust Cobaya pattern for a hard theoretical constraint; no custom
theory component is required.

## Files
- `csg_kp_theory.py` -- single source of truth for the constants `A_GAMMA`,
  `C_Q`, `L0`, `L1`, `DELTA_THETA_STAR`. Imported by `run_mcmc.py` for preflight;
  runnable standalone (prints the constants). Also contains an OPTIONAL
  `CSGKPTheory` Cobaya class; the shipped YAML does not use it.
- `csg_kp_cobaya.yaml` -- the complete MCMC config. Switches:
  `csg_kp_ratio` = 0.0021812199 (L0) or 0.0020758964 (L1);
  `csg_kp_sign` = +1.0 (open/HH) or -1.0 (closed/Vilenkin).
- `run_mcmc.py` -- driver with preflight checks (`--dry-run`,
  `--test-likelihood`, `--resume`).
- `analysis/plot_posterior.py` -- getdist corner plot + parameter table.

## What is and is not bundled
The CODE is complete. The likelihood DATA are NOT bundled (multi-GB): install
them once with `cobaya-install`.

## Setup
```
pip install cobaya camb getdist
cobaya-install planck_2018_highl_plik.TTTEEE_lite planck_2018_lowl.TT \
               planck_2018_lowl.EE planck_2018_lensing.clik
# DESI DR2 BAO: use the likelihood name present in your Cobaya release
# (e.g. bao.desi_dr2 / bao.desi_2024_bao_all); otherwise substitute an SDSS BAO file.
```

## Run
```
python3 run_mcmc.py --dry-run          # validate config + theory, no sampling
python3 run_mcmc.py --test-likelihood  # one likelihood call at the reference point
python3 run_mcmc.py                     # full MCMC (hours/days)
python3 analysis/plot_posterior.py      # post-processing after the run
```

Set `Rminus1_stop: 0.01` in the YAML for publication-grade chains (template uses
`0.05` for a faster first pass). A correct run should drive `Omega_K` to
`+0.00149 * (1 - Omega_m)/(1 + ratio)`-consistent values and can be compared to a
flat-LambdaCDM baseline (same YAML with `csg_kp_ratio: 0.0`) via Delta chi^2.
