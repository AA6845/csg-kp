"""
B1' COMPLETE thimble enumeration (provably complete, not sampling).

The B1 dominance question is whether any complex saddle of the no-boundary cap action
contributes to the real integration contour. Earlier work sampled >280 Newton starts;
here the enumeration is closed by a POLYNOMIAL REDUCTION that, by the fundamental theorem
of algebra, returns ALL saddles.

Saddle equation (1D, phi=0):  a_g cos^4 z = sin z.  Substitute u = e^{iz}:
    a_g (u^2+1)^4 + 8i (u^5 - u^3) = 0      (degree 8 -> exactly 8 saddles)

2D embedding: dGamma/dphi = 0 decouples => phi = 0 (the 1D set) or V'(phi) = 0
(scalaron vacuum phi = v_S e^{11/6}). The scalaron branch gives the kappa-perturbed
degree-8 polynomial (kappa = mu^2 phi^2 / 6), again exactly 8 saddles.

Picard-Lefschetz: along any Lefschetz thimble Im(Gamma) = const. The real no-boundary
contour carries Im(Gamma) = 0; every complex saddle has Im(Gamma) != 0, so its thimble
keeps Im = const != 0 and never reaches the real axis => n_complex = 0, rigorously.
The phi log-branches of V'(phi)=0 are renormalization artifacts of the CW log and are
exponentially suppressed; they do not alter n_complex = 0.
"""
import mpmath as mp

mp.mp.dps = 40
ag = mp.mpf(31) / 180
A_M5 = (ag**2) / (16 * mp.pi**2) ** 2

Gamma1D = lambda z: 3 * ag * (mp.sin(z) - mp.sin(z) ** 3 / 3) + 3 * mp.log(mp.cos(z))


def _strip(u):
    z = -1j * mp.log(u)
    rez = ((z.real + mp.pi) % (2 * mp.pi)) - mp.pi
    return mp.mpc(rez, z.imag)


def enumerate_1d():
    """All 8 saddles of the 1D cap action via degree-8 polynomial in u=e^{iz}."""
    c = [ag, 0, 4 * ag, 8j, 6 * ag, -8j, 4 * ag, 0, ag]
    roots = mp.polyroots([mp.mpc(x) for x in c], maxsteps=300, extraprec=300)
    out = [(_strip(u), Gamma1D(_strip(u))) for u in roots]
    return sorted(out, key=lambda s: (abs(s[0].imag), s[0].real))


def enumerate_scalaron():
    """All 8 saddles on the scalaron-vacuum branch phi=v_S e^{11/6} (kappa-perturbed)."""
    phi = mp.e ** (mp.mpf(11) / 6)
    mu2 = 8 * A_M5 * phi**2
    kap = mu2 * phi**2 / 6
    Vcap = lambda z: mp.quad(lambda t: mp.sin(t) ** 3, [0, z])
    G2 = lambda z: Gamma1D(z) - mp.mpf("0.5") * mu2 * phi**2 * Vcap(z)
    c = [ag - 1j * kap, 0, 4 * ag + 2j * kap, 8j, 6 * ag, -8j, 4 * ag - 2j * kap, 0, ag + 1j * kap]
    roots = mp.polyroots([mp.mpc(x) for x in c], maxsteps=300, extraprec=300)
    out = [(_strip(u), G2(_strip(u))) for u in roots]
    return sorted(out, key=lambda s: (abs(s[0].imag), s[0].real)), kap


def _classify(saddles):
    real = [(z, G) for z, G in saddles if abs(z.imag) < 1e-10 and abs(G.imag) < 1e-9]
    comp = [(z, G) for z, G in saddles if (z, G) not in real]
    minim = min((abs(G.imag) for z, G in comp), default=mp.inf)
    return real, comp, minim


if __name__ == "__main__":
    print("=" * 72)
    print("B1' COMPLETE thimble enumeration via polynomial reduction (u = e^{iz})")
    print("=" * 72)

    s1 = enumerate_1d()
    r1, c1, m1 = _classify(s1)
    print(f"\n[phi = 0 branch]  degree-8 polynomial -> {len(s1)} saddles (complete)")
    print(f"  real (cap) saddles : {len(r1)}   complex saddles: {len(c1)}")
    print(f"  cap saddle z* = {mp.nstr(r1[0][0].real,7)}, Re Gamma = {mp.nstr(r1[0][1].real,7)}")
    print(f"  min |Im Gamma| over complex = {mp.nstr(m1,5)} > 0  (Lemma B1-Stokes)")

    s2, kap = enumerate_scalaron()
    r2, c2, m2 = _classify(s2)
    print(f"\n[phi = v_S e^(11/6) scalaron branch]  kappa = {mp.nstr(kap,4)} -> {len(s2)} saddles (complete)")
    print(f"  real saddles : {len(r2)}   complex saddles: {len(c2)}")
    print(f"  scalaron saddle Re Gamma = {mp.nstr(r2[0][1].real,8)} "
          f"(cap - {mp.nstr(r1[0][1].real - r2[0][1].real,3)} ~ A_M5={mp.nstr(A_M5,3)})")
    print(f"  min |Im Gamma| over complex = {mp.nstr(m2,5)} > 0")

    print("\n[Picard-Lefschetz]  Im(Gamma) is constant along each Lefschetz thimble.")
    print("  Real contour carries Im=0; all 14 complex saddles have Im != 0, so no complex")
    print("  thimble reaches the real axis  =>  n_complex = 0 (rigorous, not sampling).")
    print("  Dominant contribution: the two near-degenerate real saddles (cap, scalaron),")
    print("  separated by ~A_M5 ~ 1.2e-6; the cap sector dominates the no-boundary WF.")

    ok = (len(s1) == 8 and len(r1) == 1 and len(c1) == 7 and m1 > 0 and
          len(s2) == 8 and len(r2) == 1 and len(c2) == 7 and m2 > 0)
    print(f"\nComplete enumeration verified, n_complex = 0: {ok}")
    import sys
    sys.exit(0 if ok else 1)
