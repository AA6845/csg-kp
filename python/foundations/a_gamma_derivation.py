"""
First-principles derivation of the photon type-A conformal anomaly coefficient
a_gamma = 31/180, from the Gilkey--Seeley--DeWitt heat-kernel coefficient b_4 (= a_4).

Gilkey's integrated a_4 for a Laplace-type operator D = -(nabla^2 + E) on a closed
4-manifold (total-derivative terms dropped):

  Int a_4 = (4pi)^-2 /360 * Int sqrt(g) * tr{ 60 R E + 180 E^2 + 30 Omega_mn Omega^mn
                                              + 1_bundle * (5 R^2 - 2 Ric^2 + 2 Riem^2) }

On S^4 (maximally symmetric): Ric^2 = R^2/4, Riem^2 = R^2/6, Euler density
E4 = R^2-4Ric^2+Riem^2 = R^2/6, with Int E4 = 64 pi^2 (chi=2) => Int R^2 sqrt g = 384 pi^2.
W^2 = 0, so only the type-A (Euler) part survives and Int<T> = -4 a_field on S^4.

Maxwell field = Hodge Laplacian Delta_1 on 1-forms MINUS two minimal scalar ghosts
(Faddeev--Popov):  zeta(0;Maxwell) = zeta(0;Delta_1) - 2 zeta(0;Delta_0^min).
"""
import sympy as sp

R = sp.symbols('R', positive=True)
Ric2 = R**2/sp.Integer(4)      # R_{mu nu}^2 on S^4
Riem2 = R**2/sp.Integer(6)     # R_{mu nu rho sigma}^2 on S^4
E4 = R**2 - 4*Ric2 + Riem2     # = R^2/6
# Int E4 sqrt g = 64 pi^2  =>  Int R^2 sqrt g = 384 pi^2  (homogeneous, so Int X = X * V)
IntR2 = sp.Integer(384)*sp.pi**2 / (E4/R**2*6)   # = 384 pi^2 since E4/R^2 = 1/6
# integrated <T> = (4pi)^-2/360 * [ 60 R trE + 180 trE2 + 30 trOmega2 + dim*(5R^2-2Ric2+2Riem2) ] * (IntR2/R^2 normalisation)
# We integrate constant densities: Int(coeff * R^2) = coeff * IntR2.

def integrated_anomaly(trE, trE2, trOmega2, dim):
    grav = dim*(5*R**2 - 2*Ric2 + 2*Riem2)
    density_over_R2 = (60*R*trE + 180*trE2 + 30*trOmega2 + grav)/R**2  # coefficient of R^2
    A = sp.Rational(1,360)/(16*sp.pi**2) * density_over_R2 * IntR2
    return sp.nsimplify(sp.simplify(A))

print("="*70)
print("Derivation of a_gamma from Gilkey b_4 on S^4")
print("="*70)

# (1) Conformally coupled scalar: D = -nabla^2 + R/6  => E = -R/6, dim 1, Omega=0
A_scalar = integrated_anomaly(trE=-R/6, trE2=(R/6)**2, trOmega2=0, dim=1)
a_scalar = -A_scalar/4
print(f"\nZE1 scalar (conformal): Int<T> = {A_scalar}  -> a_scalar = {a_scalar}")
print(f"     SANITY CHECK: expected a_scalar = 1/360  -> {'OK' if a_scalar==sp.Rational(1,360) else 'FAIL'}")

# (2) Hodge Laplacian Delta_1 on 1-forms: E = -Ric (trE=-R), trE^2 = Ric^2 = R^2/4,
#     dim 4, tr(Omega_mn Omega^mn) = -Riem^2 = -R^2/6  (tangent-bundle curvature)
A_d1 = integrated_anomaly(trE=-R, trE2=R**2/4, trOmega2=-R**2/6, dim=4)
# (3) minimal scalar ghost: E=0, dim 1, Omega=0
A_gh = integrated_anomaly(trE=0, trE2=0, trOmega2=0, dim=1)
print(f"\nZE2 Delta_1 (vector): Int<T> = {A_d1}")
print(f"ZE3 minimal scalar ghost: Int<T> = {A_gh}")

# (4) Maxwell = Delta_1 - 2*ghost
A_max = sp.nsimplify(A_d1 - 2*A_gh)
a_gamma = -A_max/4
print(f"\nZE4 Maxwell = Delta_1 - 2*ghost:")
print(f"     zeta(0;Maxwell;S^4) = Int<T> = {A_max}   (paper R1: -31/45)")
print(f"     a_gamma = -Int<T>/4 = {a_gamma}")
print(f"     TARGET a_gamma = 31/180  -> {'OK' if a_gamma==sp.Rational(31,180) else 'FAIL'}")
print(f"\nResult: a_gamma = {a_gamma} = {float(a_gamma):.6f}, derived from heat-kernel b_4.")
import sys as _sys
_sys.exit(0 if (a_gamma==sp.Rational(31,180) and a_scalar==sp.Rational(1,360)) else 1)
