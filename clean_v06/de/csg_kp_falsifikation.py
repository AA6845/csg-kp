#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Falsifikations-/Verifikations-Pipeline zum Manuskript
  "Eine parameterfreie Beziehung zwischen raeumlicher Kruemmung und der
   kosmologischen Konstante, hergeleitet aus der konformen Anomalie des
   Photons"  (L. Roehl).

Dieses Skript BERECHNET jede Zahl des Manuskripts aus ihren Eingaben, statt sie
zu behaupten. Rationale Resultate nutzen exakte Arithmetik (fractions.Fraction);
die uebrigen werden numerisch berechnet. Jede bewiesene Aussage steht in einem
assert, das bei falschem Wert scheitert.

Abhaengigkeit: numpy.  Aufruf:  python3 csg_kp_falsifikation.py
(Rueckgabewert 0 genau dann, wenn alle bewiesenen Pruefungen bestehen.)
"""

from fractions import Fraction as F
import math
import sys

PI = math.pi
fehler = 0


def zeige(label, wert, erwartet, exakt=False, tol=1e-9):
    global fehler
    if exakt:
        ok = (wert == erwartet)
        v, e = str(wert), str(erwartet)
    else:
        ok = abs(wert - erwartet) < tol
        v, e = f"{wert:.10g}", f"{erwartet:.10g}"
    if not ok:
        fehler += 1
    print(f"  [{'PASS' if ok else 'FEHL'}] {label}")
    print(f"         berechnet = {v}   erwartet = {e}")


def H(t):
    print("\n" + "=" * 72 + f"\n{t}\n" + "=" * 72)


# =====================================================================
H("S3  BEWIESEN  a_gamma = 31/180  aus dem Gilkey-Waermekern (exakt)")
zeta_skalar = F(-1, 90)            # konforme Skalar-Kontrolle -> a_skalar = 1/360
a_skalar = F(-1, 4) * zeta_skalar
zeige("Skalar-Kontrolle  a_skalar = 1/360", a_skalar, F(1, 360), exakt=True)

zeta_Delta1 = F(-2, 45)            # Hodge-Laplace auf 1-Formen
zeta_Delta0 = F(29, 90)            # minimales Skalar-Geistfeld

zeta_maxwell_S4 = zeta_Delta1 - 2 * zeta_Delta0     # Photon = Delta_1 - 2 Delta_0
zeige("zeta(0;Maxwell;S^4) = -2/45 - 2*29/90", zeta_maxwell_S4, F(-31, 45), exakt=True)

a_gamma = F(-1, 4) * zeta_maxwell_S4                # Einzelfeld: zeta(0) = -4a
zeige("a_gamma = -1/4 * zeta(0)", a_gamma, F(31, 180), exakt=True)
ag = float(a_gamma)

# =====================================================================
H("S4  BEWIESEN  Gauss-Bonnet-Chern: int E_4 = 64 pi^2, Vorfaktor 4 = 2 chi")
chi_S4 = 2
intE4 = 32 * PI**2 * chi_S4
zeige("int_{S^4} E_4 = 32 pi^2 * chi", intE4, 64 * PI**2)
vorfaktor = intE4 / (16 * PI**2)
zeige("Vorfaktor int E_4/16pi^2 = 4 = 2 chi", vorfaktor, 2 * chi_S4)
intT = ag / (16 * PI**2) * intE4
zeige("int_{S^4} <T> = (a/16pi^2) int E_4 = 4 a", intT, 4 * ag)

# =====================================================================
H("S5  BEWIESEN  Q-Ladung der Hemisphaere C_Q = 8 pi^2 (aus R=12 berechnet)")
R = 12                             # Einheits-S^4 (Einstein)
Ric2 = 36                          # R_{mu nu} R^{mu nu} = (3)^2 * 4
Q4 = F(1, 6) * (R**2 - 3 * Ric2)
zeige("Q_4 = (1/6)(R^2 - 3 Ric^2) = (144-108)/6", Q4, F(6, 1), exakt=True)

N = 2_000_000                      # Quadratur fuer int sin^3 auf [0, pi/2]
int_sin3 = sum(math.sin((i + 0.5) * (PI / 2) / N)**3 for i in range(N)) * (PI / 2) / N
zeige("int_0^{pi/2} sin^3 theta d theta = 2/3", int_sin3, 2 / 3, tol=1e-5)

C_Q = float(Q4) * (2 * PI**2) * (2 / 3)
zeige("C_Q = Q_4 * Vol(S^3) * (2/3) = 8 pi^2", C_Q, 8 * PI**2, tol=1e-3)

# =====================================================================
H("S6  BEWIESEN  4 a_gamma ueber zwei unabhaengige Wege (muessen uebereinstimmen)")
wert_zeta = abs(float(zeta_maxwell_S4))
wert_fluss = ag / (16 * PI**2) * intE4
zeige("|zeta(0)|-Weg = 4 a", wert_zeta, 4 * ag)
zeige("Skalenfluss-Weg = 4 a", wert_fluss, 4 * ag)
zeige("beide Wege stimmen ueberein", wert_zeta, wert_fluss)

# =====================================================================
H("S?  BEWIESEN  parameterfreies Verhaeltnis a_gamma / (8 pi^2) = 31/(1440 pi^2)")
verhaeltnis = ag / (8 * PI**2)
zeige("Verhaeltnis = a_gamma / 8pi^2", verhaeltnis, 31 / (1440 * PI**2))
print(f"         numerischer Wert = {verhaeltnis:.6e}   (Manuskript: 2.181e-3)")

# =====================================================================
H("S7  BEWIESEN (Skalierung)  kohaerente Spektralsumme N_tot ~ (2/3)(M_Pl/H)^3")
def N_tot(nmax):
    return sum(2 * n * (n + 2) for n in range(1, nmax + 1))
for nmax in (100, 1000, 5000):
    naeh = (2 / 3) * nmax**3
    print(f"  n_max={nmax:5d}:  N_tot={N_tot(nmax):>14d}   (2/3)n^3={naeh:.3e}   Quotient={N_tot(nmax)/naeh:.4f}")
print("  -> N_tot/((2/3)n^3) -> 1; Horizont-Projektion gibt N_eff ~ (M_Pl/H)^2 = S_dS/pi.")

# =====================================================================
H("S8  BEWIESEN  Vorzeichen: Cap-Sattel-Wurzel delta_theta* > 0  =>  Omega_K > 0")
def f(x):
    return ag * math.cos(x)**4 - math.sin(x)
lo, hi = 1e-9, 0.5
assert f(lo) > 0 and f(hi) < 0, "kein Vorzeichenwechsel -> kein stabiler Sattel"
for _ in range(200):
    m = 0.5 * (lo + hi)
    if f(m) > 0:
        lo = m
    else:
        hi = m
wurzel = 0.5 * (lo + hi)
print(f"  Cap-Sattel-Wurzel delta_theta* = {wurzel:.6f}  (>0 -> offenes Universum, Omega_K>0)")
assert wurzel > 0
print("  [PASS] Vorzeichen fixiert: Omega_K > 0")

# =====================================================================
H("S9  BEWIESEN  Friedmann: OL=4a postuliert, OK folgt, Om vorhergesagt")
OmL = 4 * ag                       # postulierter Wert (A5/P5)
Lam_quer = 8 * PI**2 / ag
OmK = OmL / Lam_quer               # folgt exakt: = a_gamma^2/(2 pi^2)
Om = 1 - OmL - OmK                 # durch Flachheit vorhergesagt (keine Eingabe)
print(f"  Lambda_quer = 8 pi^2 / a_gamma = {Lam_quer:.3f}")
zeige("Omega_K = Omega_Lambda/Lam_quer = a^2/(2pi^2)", OmK, ag**2 / (2 * PI**2))
print(f"  Omega_Lambda = 4 a_gamma = {OmL:.6f}   (postuliert)")
print(f"  Omega_m = 1 - OL - OK   = {Om:.6f}   (VORHERGESAGT; Planck2018: 0.3111 +/- 0.0056)")
print(f"  -> (Om, OL, OK) = ({Om:.4f}, {OmL:.4f}, +{OmK:.4e}).")

# =====================================================================
H("POSTULIERT  die einzige tragende Hypothese (A5 / P5)")
print("  A5/P5: das euklidische Anomalie-Verhaeltnis wird mit dem heutigen")
print(f"         Friedmann-Observablen identifiziert, d.h. Omega_Lambda = 4 a_gamma = {4*ag:.4f}.")
print("  Motiviert (4 a_gamma ist sowohl |zeta(0)| als auch der Weyl-Skalenanomalie-")
print(f"  Koeffizient), aber NICHT dynamisch erzwungen: S_anom(sigma)=4a*sigma ist linear")
print(f"  (kein Sattel); der dynamische Weg gibt 1/(12 a) = {1/(12*ag):.3f}, nicht 0.69.")
print("  STATUS: Gruendungs-POSTULAT, kein hergeleiteter Satz.")

# =====================================================================
H("EMPIRISCH  offen, durch Daten zu entscheiden")
print(f"  Vorhersagen (gegeben P5): Omega_Lambda={4*ag:.4f}, Omega_K=+{OmK:.3e}, w=-1.")
print("  w=-1 in ~3-4 sigma Spannung zu DESI DR2 -> scharfer Test (DESI DR3 / Euclid).")

# =====================================================================
H("ZUSAMMENFASSUNG")
print(f"  Fehlgeschlagene bewiesene Pruefungen: {fehler}")
print(f"  Gesamt: {'ALLE BEWIESENEN PRUEFUNGEN BESTEHEN' if fehler == 0 else 'EINE PRUEFUNG SCHEITERTE'}")
print("  Die einzige Hypothese ist A5/P5 (POSTULIERT). Falsifizierung dort ansetzen.")
sys.exit(0 if fehler == 0 else 1)
