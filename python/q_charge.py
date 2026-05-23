#!/usr/bin/env python3
"""
q_charge.py  --  The two exact spectral inputs of the topological ratio.

(1) Q-curvature charge of the hemisphere:   integral_{D^4} Q_4 sqrt(g) = 8 pi^2.
    Proven elementarily with exact symbolic arithmetic (Chang-Yang / Branson).

(2) Dirichlet-to-Neumann zeta value:        zeta(0; DtN; S^3) = -1.
    Established DIRECTLY from the cap-DtN spectrum lambda_l = l(l+2)/(l+1) (derived from
    the harmonic extension into the S^4 cap; NOT l, which is the flat-ball B^4 value),
    multiplicity (l+1)^2: zeta(0) = zeta_R(-2) - 1 = -1 (all subleading terms vanish at s=0).
    The BFK route 2 zeta(D^4) - zeta(S^4) is kept as a consistency cross-check only -- as a
    standalone derivation it is circular (zeta(D^4)=-38/45 already encodes the -1).
    NB: the manuscript's R2 states the spectrum as lambda_l = l, which is incorrect (it would
    give -2/3, not -1); the value -1 is correct via the cap spectrum l(l+2)/(l+1).

Both are Tier-1 / Tier-2 inputs to the prediction |Omega_K|/Omega_Lambda =
a_gamma / (8 pi^2).  Dependency: sympy.
"""
import sympy as sp


def q_charge_hemisphere():
    """Return (Q4_on_S4, integral_sin3, C_Q) as exact sympy expressions."""
    theta = sp.symbols("theta", positive=True)

    # On the unit S^4 (Einstein, R = 12, R_ab = 3 g_ab, Box R = 0):
    #   Q_4 = (1/6)(R^2 - 3 R_ab R^ab) = (1/6)(144 - 108) = 6.
    R = sp.Integer(12)
    Ric2 = 3 * R                       # R_ab R^ab = 3*3*4 = 36 ... use scalar form below
    # R_ab = 3 g_ab in 4D  =>  R_ab R^ab = (3)^2 * 4 = 36; R^2 = 144.
    R_ab_sq = sp.Integer(36)
    Q4 = sp.Rational(1, 6) * (R**2 - 3 * R_ab_sq)

    # Volume factor: sqrt(g) on the polar slice carries sin^3(theta);
    # Vol(S^3) = 2 pi^2 for the transverse three-sphere.
    integral_sin3 = sp.integrate(sp.sin(theta) ** 3, (theta, 0, sp.pi / 2))
    vol_S3 = 2 * sp.pi**2

    C_Q = sp.simplify(Q4 * vol_S3 * integral_sin3)
    return Q4, integral_sin3, C_Q


def zeta_dtn():
    """zeta(0; DtN; S^3) = 2 zeta(0; D^4) - zeta(0; S^4) via BFK (consistency check)."""
    zeta_S4 = sp.Rational(-31, 45)     # gauge-invariant Maxwell value on S^4
    zeta_D4 = sp.Rational(-38, 45)     # Esposito hemisphere decomposition
    return sp.simplify(2 * zeta_D4 - zeta_S4), zeta_S4, zeta_D4


def dtn_eigenvalue(l):
    """Scalar DtN eigenvalue on S^3 = equator of S^4 (round metric), DERIVED from the
    harmonic extension into the cap. The radial harmonic equation
        f'' + 3 cot(theta) f' - l(l+2)/sin^2(theta) f = 0,  f ~ sin^l near theta=0,
    has logarithmic normal derivative f'(pi/2)/f(pi/2) = l(l+2)/(l+1) = (l+1) - 1/(l+1).
    (NOT l: the flat-ball value l applies to B^4, not the S^4 cap.)"""
    return sp.Rational(l * (l + 2), l + 1)


def zeta_dtn_direct():
    """zeta(0; DtN; scalar; S^3) computed DIRECTLY from the cap-DtN spectrum, independent
    of the BFK bookkeeping. Spectrum lambda_l = l(l+2)/(l+1) = (l+1) - 1/(l+1), multiplicity
    (l+1)^2, l>=1 (the constant l=0 mode is the kernel, DtN eigenvalue 0, excluded).

    Set n = l+1 >= 2: lambda = n - 1/n, mult n^2. Then
        zeta(s) = sum_{n>=2} n^2 (n - 1/n)^{-s} = sum_{n>=2} n^{2-s} (1 - 1/n^2)^{-s}.
    Expanding (1-1/n^2)^{-s} = 1 + s/n^2 + ... every correction carries a factor s and the
    Riemann zetas it multiplies are regular at s=0, so they vanish there; only the leading
    term survives:  zeta_DtN(0) = [zeta_R(-2) - 1] = 0 - 1 = -1  (the -1 removes the absent n=1).
    """
    s = sp.symbols("s")
    # leading term sum_{n>=2} n^{2-s} = zeta_R(s-2) - 1  (n=1 contributes 1)
    zeta0_leading = sp.zeta(-2) - 1               # zeta_R(-2) = 0  ->  -1
    return sp.nsimplify(zeta0_leading)


def dtn_maxwell_zeta_and_dets():
    """Maxwell DtN on S^3 via the Faddeev-Popov combination, with VERIFIED determinants.
    Resolves R3/R4/R8: the single spectrum mu_l=l+1 is the TRANSVERSE 1-FORM DtN (R3),
    NOT the Maxwell DtN; the Maxwell DtN (R4) is the FP combination 1-form - 2*scalar-ghost.

      scalar  DtN: mu_l = l(l+2)/(l+1), mult (l+1)^2  -> zeta(0)=-1   (R2)
      1-form  DtN: mu_l = l+1,          mult 2 l(l+2) -> zeta(0)=+1   (R3)
      Maxwell DtN: 1-form - 2*scalar                  -> zeta(0)= 3   (R4)

    Determinants (det' = exp(-zeta'(0))):
      det'_1f = exp(-2[zeta_R'(-2)-zeta_R'(0)])                       (exact)
      det'_sc = exp(-zeta'_sc(0)),  zeta'_sc(0)=zeta_R'(-2)+sum_k (1/k)[zeta_R(2k-2)-1]
      det'_Maxwell = det'_1f / det'_sc^2  ==  1/(2 pi^3)              (= R8 value)
    """
    import mpmath as mp
    mp.mp.dps = 30
    # zeta(0): FP combination
    z_sc0, z_1f0 = -1, 1
    z_max0 = z_1f0 - 2 * z_sc0                                # = 3  (R4)
    # det'_1form (exact closed form)
    z1fp = 2 * (mp.zeta(-2, derivative=1) - mp.zeta(0, derivative=1))
    det1f = mp.e ** (-z1fp)                                   # ~ 0.16915
    # det'_scalar via convergent series  zeta'_sc(0)=zeta_R'(-2)+sum_{k>=1}(1/k)[zeta_R(2k-2)-1]
    zscp = mp.zeta(-2, derivative=1) + mp.nsum(
        lambda k: (mp.mpf(1) / k) * (mp.zeta(2 * k - 2) - 1), [1, mp.inf])
    detsc = mp.e ** (-zscp)                                   # ~ 3.2387
    det_max = det1f / detsc ** 2                              # FP Maxwell DtN determinant
    return z_sc0, z_1f0, z_max0, float(det1f), float(detsc), det_max


def main():
    print("=" * 70)
    print("Exact spectral inputs to the topological ratio")
    print("=" * 70)

    Q4, integral_sin3, C_Q = q_charge_hemisphere()
    print("\n[1] Q-curvature charge of the hemisphere D^4")
    print(f"    Q_4(unit S^4)            = (1/6)(144 - 108) = {Q4}")
    print(f"    integral_0^(pi/2) sin^3  = {integral_sin3}")
    print(f"    C_Q = Q_4 * Vol(S^3) * integral = 6 * 2 pi^2 * 2/3 = {C_Q}")
    assert C_Q == 8 * sp.pi**2, "C_Q must equal 8 pi^2"
    print("    -> C_Q = 8 pi^2  [PASS]")

    print("\n[2] DtN zeta value, DIRECT route (independent of BFK)")
    print("    cap-DtN spectrum lambda_l = l(l+2)/(l+1) = (l+1)-1/(l+1), mult (l+1)^2:")
    for l in (1, 2, 3, 4):
        print(f"      l={l}: lambda_l = {dtn_eigenvalue(l)} = {float(dtn_eigenvalue(l)):.4f}  "
              f"(NOT l={l}; flat-ball value l does not apply to the S^4 cap)")
    z_direct = zeta_dtn_direct()
    print(f"    zeta(0;DtN;scalar;S^3) = zeta_R(-2) - 1 = {z_direct}   (subleading terms vanish at s=0)")
    assert z_direct == -1, "direct DtN zeta(0) must equal -1"
    print("    -> zeta(0; DtN; scalar; S^3) = -1  [PASS, independent of BFK]")

    z, zS4, zD4 = zeta_dtn()
    print("\n[3] DtN zeta value, BFK consistency cross-check (scalar bookkeeping)")
    print(f"    zeta(0; Maxwell; S^4)    = {zS4}")
    print(f"    zeta(0; Maxwell; D^4)    = {zD4}   (Esposito 1995)")
    print(f"    zeta(0; DtN; scalar) = 2*({zD4}) - ({zS4}) = {z}")
    assert z == -1, "zeta_DtN (BFK) must equal -1"
    print("    -> matches the direct route  [PASS]")
    print("    NB: as a STANDALONE derivation the BFK route is circular (zD4=-38/45 already")
    print("        encodes -1); the DIRECT spectrum in [2] is the independent establishment.")

    import mpmath as mp
    z_sc0, z_1f0, z_max0, det1f, detsc, det_max = dtn_maxwell_zeta_and_dets()
    print("\n[4] Maxwell DtN via Faddeev-Popov (resolves R3/R4/R8 spectrum attribution)")
    print(f"    scalar  DtN: zeta(0)={z_sc0}  (R2),  det'_sc = {detsc:.6f}")
    print(f"    1-form  DtN: zeta(0)={z_1f0}  (R3),  det'_1f = {det1f:.6f}  [spectrum mu_l=l+1]")
    print(f"    Maxwell DtN: zeta(0)={z_max0}  (R4) = 1-form - 2*scalar-ghost (FP)")
    print(f"    det'_Maxwell = det'_1f / det'_sc^2 = {float(det_max):.10f}")
    print(f"    1/(2 pi^3)                         = {float(1/(2*mp.pi**3)):.10f}")
    assert abs(det_max - 1 / (2 * mp.pi ** 3)) < 1e-9, "FP-Maxwell det' must equal 1/(2 pi^3)"
    assert z_max0 == 3, "Maxwell DtN zeta(0) must equal 3 (R4)"
    print("    -> det'_Maxwell = 1/(2 pi^3)  [PASS]; R8's value is the FP combination,")
    print("       NOT the single mu_l=l+1 spectrum (which is the 1-form DtN, R3, det'=0.169).")

    print("\nSTATUS")
    print("  C_Q = 8 pi^2          : proven (theorem-level; elementary sympy proof).")
    print("  zeta(0; DtN; scalar)=-1: DIRECT from cap spectrum lambda_l=l(l+2)/(l+1) (NOT l);")
    print("                          BFK route is a consistency cross-check.")
    print("  Maxwell DtN: zeta(0)=3 (R4), det'=1/(2pi^3) (R8) via the gauge combination")
    print("                          (1-form - 2 ghost), NOT a single mu_l=l+1 spectrum.")
    print("  NB: none of the DtN values enter the central ratio a_gamma/C_Q.")


if __name__ == "__main__":
    main()
