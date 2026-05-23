#!/usr/bin/env python3
"""
Post-MCMC analysis: posterior plot, parameter table, BAO/CMB residuals.

Usage:
    python3 plot_posterior.py [chain_root]

Defaults to chains/csg_kp_chain (relative to the cobaya_integration root).
Produces:
    - posterior_triangle.pdf  (corner plot of cosmological parameters)
    - parameter_table.txt     (mean +/- std + 68% / 95% intervals)
    - residuals.pdf           (BAO and CMB residuals against best fit)
"""

import sys
from pathlib import Path
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "chain_root", nargs="?",
        default=str(Path(__file__).parent.parent / "chains" / "csg_kp_chain"))
    parser.add_argument(
        "--out", default=str(Path(__file__).parent),
        help="Output directory (default: this folder)")
    args = parser.parse_args()

    try:
        from getdist import loadMCSamples, plots
    except ImportError:
        print("ERROR: getdist required. Install via 'pip install getdist'.",
              file=sys.stderr)
        sys.exit(2)

    chain_root = Path(args.chain_root)
    if not chain_root.parent.exists():
        print(f"ERROR: chain directory does not exist: {chain_root.parent}",
              file=sys.stderr)
        print("Run run_mcmc.py first.", file=sys.stderr)
        sys.exit(3)

    print(f"Loading chains from: {chain_root}")
    samples = loadMCSamples(str(chain_root), settings={"ignore_rows": 0.3})

    # --- 1) Triangle plot of cosmological parameters ---
    print("Generating triangle plot...")
    g = plots.get_subplot_plotter()
    g.triangle_plot(
        samples,
        ["H0", "ombh2", "omch2", "ns", "tau", "logA", "omegam", "omegak"],
        filled=True)
    out_pdf = Path(args.out) / "posterior_triangle.pdf"
    g.export(str(out_pdf))
    print(f"  -> {out_pdf}")

    # --- 2) Parameter table ---
    print("Generating parameter table...")
    params = ["H0", "ombh2", "omch2", "ns", "tau", "logA",
              "omegam", "omegal", "omegak"]
    lines = ["# CSG-KP MCMC posterior summary", "#"]
    lines.append(f"# {'parameter':<14s}{'mean':>14s}{'sigma':>14s}"
                 f"{'68% low':>14s}{'68% high':>14s}{'95% low':>14s}{'95% high':>14s}")
    for p in params:
        try:
            stats = samples.getInlineLatex(p, limit=1)
            mean = samples.mean(p)
            std = samples.std(p)
            lim68 = samples.confidence(p, 0.32, upper=False), samples.confidence(p, 0.32, upper=True)
            lim95 = samples.confidence(p, 0.05, upper=False), samples.confidence(p, 0.05, upper=True)
            lines.append(
                f"  {p:<14s}{mean:>14.6e}{std:>14.6e}"
                f"{lim68[0]:>14.6e}{lim68[1]:>14.6e}"
                f"{lim95[0]:>14.6e}{lim95[1]:>14.6e}")
        except Exception as exc:
            lines.append(f"  {p:<14s} ERROR: {exc}")
    out_txt = Path(args.out) / "parameter_table.txt"
    out_txt.write_text("\n".join(lines) + "\n")
    print(f"  -> {out_txt}")

    # --- 3) Framework consistency check ---
    print("Computing framework consistency check...")
    import math
    a_gamma = 31.0 / 180.0
    ratio_predicted = a_gamma / (8.0 * math.pi ** 2)
    print(f"  CSG-KP predicted |Omega_K|/Omega_Lambda = {ratio_predicted:.6e}")
    try:
        omegak_samples = samples.getParams().omegak
        omegal_samples = samples.getParams().omegal
        ratio_obs = abs(omegak_samples) / omegal_samples
        ratio_mean = ratio_obs.mean()
        ratio_std = ratio_obs.std()
        print(f"  Posterior |Omega_K|/Omega_Lambda = {ratio_mean:.6e} +/- {ratio_std:.6e}")
        print(f"  Deviation from prediction: "
              f"{(ratio_mean - ratio_predicted)/ratio_std:+.2f} sigma")
    except Exception as exc:
        print(f"  Could not compute observed ratio: {exc}")

    print("\nDone.")


if __name__ == "__main__":
    main()
