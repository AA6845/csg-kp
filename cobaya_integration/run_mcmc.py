#!/usr/bin/env python3
"""
Driver script for the CSG-KP Cobaya MCMC run.

Usage:
    python3 run_mcmc.py                  # full MCMC (can take hours/days)
    python3 run_mcmc.py --dry-run        # validate config + theory class, no sampling
    python3 run_mcmc.py --resume         # resume existing chain
    python3 run_mcmc.py --test-likelihood   # evaluate likelihood once at reference

The script wraps Cobaya's standard run() entry point with a few
preflight checks and convenient flags.
"""

import sys
import argparse
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))


def preflight():
    """Check that required packages are importable."""
    missing = []
    for pkg in ("cobaya", "camb", "getdist"):
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)
    if missing:
        print(f"ERROR: missing packages: {missing}", file=sys.stderr)
        print("Install via:", file=sys.stderr)
        print("  pip install cobaya camb getdist", file=sys.stderr)
        print("Then:", file=sys.stderr)
        print("  cobaya-install planck_2018_highl_plik.TTTEEE_lite \\", file=sys.stderr)
        print("                 planck_2018_lowl.TT planck_2018_lowl.EE \\", file=sys.stderr)
        print("                 planck_2018_lensing.clik", file=sys.stderr)
        return False

    # Verify theory class is importable.
    try:
        from csg_kp_theory import L0, L1, A_GAMMA, C_Q  # constants module
    except ImportError as exc:
        print(f"ERROR: cannot import csg_kp_theory: {exc}", file=sys.stderr)
        return False

    print(f"Preflight OK. Theory constants:")
    print(f"  a_gamma = 31/180 = {A_GAMMA:.10f}")
    print(f"  C_Q     = 8 pi^2 = {C_Q:.6f}")
    print(f"  L0      = {L0:.6e}   (leading prediction)")
    print(f"  L1      = {L1:.6e}   (cap-exact refinement)")
    return True


def main():
    parser = argparse.ArgumentParser(description="CSG-KP Cobaya MCMC driver")
    parser.add_argument(
        "--config", default=str(HERE / "csg_kp_cobaya.yaml"),
        help="Path to Cobaya YAML config (default: csg_kp_cobaya.yaml)")
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Validate config and theory only; do not run MCMC.")
    parser.add_argument(
        "--resume", action="store_true",
        help="Resume an existing chain.")
    parser.add_argument(
        "--test-likelihood", action="store_true",
        help="Evaluate likelihood once at the reference point and exit.")
    args = parser.parse_args()

    if not preflight():
        sys.exit(2)

    from cobaya.yaml import yaml_load_file
    from cobaya.run import run

    try:
        info = yaml_load_file(args.config)
    except FileNotFoundError:
        print(f"ERROR: config not found at {args.config}", file=sys.stderr)
        sys.exit(3)

    print(f"Loaded config: {args.config}")
    print(f"Theory: {list(info.get('theory', {}).keys())}")
    print(f"Likelihoods: {list(info.get('likelihood', {}).keys())}")

    if args.test_likelihood:
        info = dict(info)
        info["test"] = True
        info["sampler"] = {"evaluate": None}
        print("Mode: evaluate-only (single likelihood call at reference point)")
        try:
            updated_info, products = run(info)
            print("Likelihood evaluation succeeded.")
        except Exception as exc:
            print(f"Likelihood evaluation FAILED: {exc}", file=sys.stderr)
            sys.exit(4)
        return

    if args.dry_run:
        info = dict(info)
        info["test"] = True
        print("Mode: dry-run (validate config only, no sampling)")
        try:
            updated_info, products = run(info)
            print("Config validates successfully.")
        except Exception as exc:
            print(f"Config validation FAILED: {exc}", file=sys.stderr)
            sys.exit(5)
        return

    info = dict(info)
    if args.resume:
        info["resume"] = True
        print("Mode: resuming existing chain")
    else:
        info["force"] = True
        print("Mode: full MCMC run (this may take hours/days)")

    try:
        updated_info, products = run(info)
        print("MCMC completed successfully.")
        print(f"Chains written to: {info.get('output', 'chains/csg_kp_chain')}")
    except KeyboardInterrupt:
        print("\nInterrupted by user.", file=sys.stderr)
        sys.exit(130)
    except Exception as exc:
        print(f"MCMC FAILED: {exc}", file=sys.stderr)
        sys.exit(6)


if __name__ == "__main__":
    main()
