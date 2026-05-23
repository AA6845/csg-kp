# CSG–KP × Shaw–Barrow: Mechanismus-Übertrag, strukturelle Identität, Hierarchie-Audit

**Sitzungsprotokoll — 2026-05-21**
**Status-Konvention:** [THEOREM] = rigoros · [NUM] = numerisch gestützt, kein formaler Beweis · [POSTULAT] = angenommen, nicht abgeleitet · [INPUT] = von außen gesetzt · [DEAD END] = geprüft und verworfen

Alle Zeilennummern (Z.) beziehen sich auf `manuscript/diss.tex`. Externe Quelle: Shaw & Barrow, *A Testable Solution of the Cosmological Constant and Coincidence Problems*, PRD 83, 043518 (2011), arXiv:1010.4262 (im Folgenden „SB").

---

## 0. Fragestellung

CSG–KP sagt das **Verhältnis** rigoros voraus:

$$\frac{|\Omega_K|}{\Omega_\Lambda} = \frac{a_\gamma}{8\pi^2} = \frac{31}{1440\pi^2} \approx 2.181\times10^{-3} \quad\text{[THEOREM, Euklidisch]}$$

mit $a_\gamma = 31/180$ (Photon-Typ-A-Anomalie) und $8\pi^2 = \int_{D^4}Q_4$ (Chang–Yang). **Nicht** vorhergesagt: der absolute Wert $\Omega_\Lambda \approx 0.685$ (Z.1852, [INPUT]) und die Sattel-Skala-Identifikation $L_{HH}=1/H_0$ (Z.615: „a model-building input, not a theorem").

**Leitfrage der Sitzung:** Kann ein *prior-unabhängiger kausaler* Mechanismus (Shaw–Barrow) diese offene Ecke schließen — übertragen mit CSGs eigenen Werkzeugen?

---

## 1. Lombriser-Zweig — verworfen [DEAD END]

(Aus vorangehenden Sitzungen, hier zur Vollständigkeit.)

- Lombrisers Strukturbildungs-Sequestering ist im Grenzfall $\alpha=0$ **identisch** mit CSGs lokalem Sequestering (strukturell bewiesen, keine Koinzidenz).
- Sein $\Omega_\Lambda = 0.704$ folgt aus einem **uniform-in-$y$ prior** ($\langle y\rangle = \tfrac12$). Sensitivität: $y{=}0.50\to0.704$; $y{=}0.511\to0.685$. Ein 2%-Prior-Shift deckt die Differenz.
- Alle physikalisch motivierten Maße getestet: uniform-in-time $\to 0.99$; $V_4$-Gewichtung $\to 1.0$; objektiver min-$y'$-Punkt $\to 0.659$. Nur der nicht-physikalische uniform-in-$y$ trifft die Beobachtung.
- **Befund:** Der Wert hängt am **Beobachter-Maß** (Maß-Problem). Don Page (1011.4932): keine eindeutige Regel. Astashenok 2012: Volumengewichtung $\to \Lambda=0$ mit Wahrscheinlichkeit 1 (bestätigt unabhängig den $V_4\to1$-Befund). **Kategorisch nicht aus einer Hintergrund-Quantenkosmologie ableitbar.** Lombriser-Zweig geschlossen.

---

## 2. Shaw–Barrow: exakte Herleitung (arXiv:1010.4262)

### 2.1 Grundstruktur
$$G^{\mu\nu} = 8\pi G\,T_{\rm m}^{\mu\nu} - \Lambda g^{\mu\nu}, \qquad \Lambda = \lambda + 8\pi G\rho_{\rm vac}$$

$\lambda$ wird vom Parameter zum **Feld** befördert; die Variation nach $\lambda$ wird **kausal auf den past light cone $M$ restringiert**. Die klassische CC folgt aus (Eq. 1):
$$\frac{dI_{\rm class}(\Lambda;M)}{d\Lambda} = 0$$

### 2.2 Magnitude (SB §II C, S.7) — parameterfrei
Größenordnungsabschätzung mit $\mathrm{tr}\,N \sim \mathrm{tr}\,K \sim H$ und $V_M \sim t_U A_{\partial M}$:
$$\Lambda \sim \frac{H_0\,A_{\partial M}}{V_M} \sim \frac{H_0}{t_U} \sim t_U^{-2}$$
**Rein geometrisch** (Oberfläche/Volumen des Lichtkegels), kein freier Parameter. → liefert $\Omega_\Lambda \sim O(1)$ zu *jeder* Beobachtungszeit (Koinzidenz gelöst).

### 2.3 ζ_b ist eine baryonische Materie-Eigenschaft, kein Anomalie-Koeffizient
SB §III B 3 (S.14–15): Beiträge zu $L_{\rm matter}$ (effektiver, in vacuo verschwindender Lagrangian):
- **Photonen:** $L \approx -F^2/4 = (E^2-B^2)/2$, für Strahlung $E^2=B^2 \Rightarrow L=0$ **(klassisch — Anomalie ignoriert)**
- freie Fermionen: $L=0$; massive/dunkle Materie: unterdrückt $\sim O(H/\omega)$
- **nur Baryonen** überleben (QCD-Bindung, chiral bag model):
$$L_{\rm matter} = -\zeta_b\,\rho_{\rm baryon}, \qquad \zeta_b = 1 - \frac{M_q}{M_N} \approx 0.5$$
$\zeta_b$ ist eine **gemessene** QCD-Materie-Eigenschaft ($\xi_b = \rho_{\rm baryon}/n_\gamma = 0.54$ eV), kein freier theoretischer Koeffizient.

### 2.4 Krümmungs-Constraint (Eq. 26)
$$-\Omega_{k0} = \frac{\zeta_b\Omega_{b0}}{2}\,\mathcal N(\tau_0;\Lambda), \qquad
\mathcal N = \frac{\int_0^{\tau_0} a\,a_0^3(\tau_0-\tau)^3 A\,d\tau}{\int_0^{\tau_0} a^2 a_0^2[\tfrac23(\tau_0-\tau)^3 + \tau(\tau_0-\tau)^2]A\,d\tau}$$
mit $A(\tau) = \mathcal H\int_0^\tau a^2/(6\mathcal H^2)\,d\tau'$. Die Krümmung wird durch den **bulk-Trace** $L_{\rm matter}$ *getrieben*, balanciert gegen den gravitativen $\Gamma$-Term (enthält $2k$). Bei $\Omega_\Lambda{=}0.73$, $\Omega_{b0}{=}0.0423$, $\zeta_b{=}0.5$: $\Omega_{k0} = -0.0056$.

**Wichtig (SB §III C, S.17 ff.):** SB sagen $\Omega_\Lambda$ **nicht** voraus — der Wert ist environmentell (e-folds $N$ der Inflation, $f_N(N)$ = Inflations-Maß-Problem). Wie CSG sagen sie die *Krümmung gegeben* $\Omega_\Lambda$ voraus, nicht $\Omega_\Lambda$ selbst.

---

## 3. Numerische Validierung

### 3.1 $\mathcal N$-Integral reproduziert (`sb_N.py`)
| $\Omega_\Lambda$ | $\mathcal N$ | $\Omega_{b0}$ | $\Omega_{k0}$ |
|---|---|---|---|
| 0.685 | 0.5092 | 0.0493 | −0.00628 |
| 0.730 | 0.5158 | 0.0423 | **−0.00545** |
| 0.800 | 0.5294 | 0.0313 | −0.00415 |

$\mathcal N(0.73)=0.516 \Rightarrow \Omega_{k0}=-0.00545$ gegen SB-Paper $-0.0056$ → **~3% Übereinstimmung** (Differenz aus vernachlässigten $\Phi$-Termen). Maschinerie korrekt reproduziert. $\mathcal N\approx 0.5$ ist ein fast $\Omega_\Lambda$-unabhängiger Lichtkegel-Geometrie-Faktor. [NUM]

### 3.2 Magnitude-Selbstkonsistenz (`plc2.py`)
- Kausale Bedingung $\Lambda = 1/t_U^2$ (Faktor 1) → **$\Omega_\Lambda = 0.489$**
- Bei Beobachtung $\Omega_\Lambda{=}0.685$: $t_\Lambda/t_U = 0.733$ = exakt SBs eigenes Verhältnis (9.7/13.7 Gyr = 0.71). Konsistent.
- **Befund:** Mechanismus liefert die Größenordnung ($\Omega_\Lambda\sim O(1)$), nicht den präzisen Wert (O(1)-Faktor offen). [NUM]

### 3.3 Naive KP-Form über PLC scheitert (`plc.py`)
$\Lambda = \tfrac14\langle R\rangle_{\rm PLC}$ gibt $\langle R\rangle_{\rm PLC}/4 \approx 14$–17 (in $H_0^2$) gegen $\Lambda=3\Omega_\Lambda\approx2$ → Faktor ~7 daneben, kein Fixpunkt. $\langle R\rangle_{\rm PLC}$ ist materie-dominiert (frühe Zeiten, $R\sim a^{-3}$). Die naive $\tfrac14\langle R\rangle$ ist *nicht* SBs Mechanismus. [DEAD END für naive Form]

---

## 4. Übertrag auf CSG — was sich überträgt

### 4.1 a_γ ist präzise lokalisiert
Die exakte Herleitung zeigt: SB setzen den **Photon-Beitrag zu $L_{\rm matter}$ klassisch auf null** (S.14, $E^2=B^2$). Die konforme Anomalie $\langle T^\mu_\mu\rangle = (a_\gamma E_4 + c_\gamma W^2)/16\pi^2$ ist genau die **Quanten-Korrektur** dazu. CSGs $a_\gamma$ füllt eine echte Lücke in SBs Anwendung. CSGs eigenes Komargodski–Schwimmer-Argument (P4) sagt sogar, dass SBs Baryon-Trace im IR *dekoppelt* (massive Hadronen) — die Anomalie *muss* dominieren.

### 4.2 Skala-Ecke geschlossen
SBs $\Lambda\sim t_U^{-2}$ aus $A_{\partial M}/V_M\sim H_0$ ist parameterfrei → erklärt CSGs Input $L_{HH}=1/H_0$ (Z.615). Die kausale Restriktion ist der physikalische Grund, *warum* die Sattel-Skala $1/H_0$ ist.

---

## 5. Die Skalierungs-Hürde — warum der Übertrag nicht *mechanisch* ist [NUM]

Im Lichtkegel-Integral (Eq. 25) skalieren die Trace-Beiträge unterschiedlich (`sb_anom.py`, $\Omega_\Lambda{=}0.685$):

| Trace-Term | Gewichtung im Integral | Median-$a$ | Anteil aus $a<0.1$ |
|---|---|---|---|
| Baryon $a^4\rho_b \sim a$ | spätzeit | 0.42 | 0.5% |
| Anomalie $a^4 H^4$ | **frühzeit** | 0.16 | **32%** |

Ersetzt man in Eq. 26 einfach $\zeta_b\Omega_{b0}\to a_\gamma$, dominiert die strahlungs-/materiedominierte Frühzeit das Integral, und das saubere $\Omega_K\propto a_\gamma\Omega_\Lambda$ kommt **nicht** heraus. → Der naive Übertrag scheitert; die Lorentzsche Lichtkegel-Maschinerie ist für die Anomalie das falsche Werkzeug.

---

## 6. Strukturelle Identität: SB ↔ CSG-cap [THEOREM, strukturell]

Beide Frameworks sind **dasselbe Variations-Prinzip**: *bulk-Trace-drive balanciert gegen boundary/edge-restoring-force, über eine endliche kausal bestimmte Region.*

| | Shaw–Barrow (Lorentzsch) | CSG-cap (Euklidisch) |
|---|---|---|
| Region | past light cone $M$ | $D^4$ = „past light cone topologically a four-ball" (Z.613 ii) |
| bulk-drive | $\int_M[\kappa^{-1}\Gamma + L_{\rm matter}]$ | $d\Gamma_{\rm bulk}/d\delta\theta = 3a_\gamma$ (a₄-heat-kernel, Z.94) |
| edge-restoring | $\partial M_u$, extrinsische Krümmung $\mathrm{tr}\,K$ | DtN-Determinant auf $\partial D^4 = S^3$ |
| Bedingung | $dI_{\rm class}/d\Lambda = 0$ | $\partial\Gamma/\partial\delta\theta = 0$ |
| Trace | klassischer Baryon-QCD ($\zeta_b$) | Quanten-Photon-Anomalie ($a_\gamma$) |
| Geometrie-Faktor | $\mathcal N/2\approx 0.26$ (dynamisch) | $1/8\pi^2\approx 0.0127$ (topologisch) |
| Vorzeichen | $\Omega_{k0}<0$ (geschlossen) | $\Omega_K>0$ (offen, via HH+BGT) |

### 6.1 cap-saddle-Gleichung verifiziert (`cap_saddle`)
$$a_\gamma\cos^4\delta\theta = \sin\delta\theta \;\Rightarrow\; \delta\theta^*_{\rm exact} = 0.16391 \quad(\text{diss: } 0.16391, \checkmark)$$
Linear: drive $3a_\gamma$ = restoring $3\delta\theta$ (Faktor $3=\dim S^3$ kürzt) $\Rightarrow \delta\theta^*=a_\gamma$. WZ-conjugate Bridge: $\delta\theta^*/\int Q_4 = a_\gamma/(8\pi^2)$.
- L0 (linear): $a_\gamma/(8\pi^2) = 2.181\times10^{-3}$
- L1 (cap-exact): $\delta\theta^*/(8\pi^2) = 2.076\times10^{-3}$ (−4.8%)

### 6.2 Warum CSG topologisch sein *muss* (nicht willkürlich)
diss.tex Z.592: der **dynamische** Weg (DtN-Determinant als Riegert-Analogon zu SBs Lorentz-Integral) **scheitert um $10^{240}$** (Mechanism 2, Tabelle Z.5709). Deckt sich exakt mit dem Frühzeit-Befund §5. Nur die **topologische** Auswertung (a₄-drive gegen skaleninvarianten DtN-$\zeta(0)=3$, normiert durch Chang–Yang $\int_{D^4}Q_4=8\pi^2$) gibt $a_\gamma/(8\pi^2)$. SBs dynamischer Weg ist korrekt für den klassischen Baryon-Trace, für die Quanten-Anomalie *muss* man auf den topologischen cap wechseln.

**Netto §6:** SBs kausal-restringierte Variation **legitimiert CSGs cap-Restriktion** ($D^4$ = past light cone = endliche Region, kein Maß nötig) — der vorher ungerechtfertigte Schritt. Die Lorentz-Formeln selbst übertragen sich nicht; das war auch nicht nötig.

---

## 7. Hierarchie-Audit: die $10^{240}$, $10^{122}$, O(1) lösen sich widerspruchsfrei auf

### 7.1 Numerik (`Sanity-Check`)
$M_{\rm Pl}/H_0 \approx 1.6\times10^{60}$ (reduziert) bis $8\times10^{60}$ (voll), also:

| Größe | Wert | Rolle |
|---|---|---|
| $(M_{\rm Pl}/H_0)^2$ | $\sim10^{122}$ | $A_2$ = Horizontfläche = **die Hierarchie** = $N_{\rm eff}$ |
| $(M_{\rm Pl}/H_0)^4$ | $\sim10^{244}$ | $V_4$ = 4-Volumen der Hubble-Patch |
| Mechanism-2-failure | $\sim10^{240}$ | **= $(M_{\rm Pl}/H_0)^4 = V_4$** |

→ Die $10^{240}$ ist $V_4$ (4-Volumen in Planck-Einheiten), **kein** fehlerhaftes $(10^{120})^2$-Wahrscheinlichkeitsquadrat. Numerisch von $(\text{Hierarchie})^2$ ununterscheidbar, aber die Logik ist V₄-Skalierung. [Konsistent, aber im Manuskript ohne explizite Herleitung — Dokumentations-Schwäche.]

### 7.2 Die Hierarchie ist nicht gelöst, sondern in P5 verschoben
Naive single-mode-Anomalie (Z.6065, SB-eigene Rechnung):
$$\Omega_{\rm anom,naive} = \frac{a_\gamma}{8\pi^2}\cdot\frac{H^2}{M_{\rm Pl}^2} \approx 10^{-3}\cdot10^{-122} \approx 10^{-125}$$
— **122 Größenordnungen zu klein**, „fails by the full cosmological-constant hierarchy". Die topologische Eleganz von $a_\gamma/(8\pi^2)$ täuscht: die nackte Anomalie trägt die volle CC-Hierarchie.

**Kompensation durch P5** (holographische Akkumulation, $N_{\rm eff}=M_{\rm Pl}^2/H^2\approx10^{122}$):
$$\rho_{\rm eff} = N_{\rm eff}\cdot\rho_{\rm anom} = \frac{M_{\rm Pl}^2}{H^2}\cdot\frac{3a_\gamma}{8\pi^2}H^4 = \frac{3a_\gamma}{8\pi^2}M_{\rm Pl}^2 H^2 \;\Rightarrow\; \Omega_{\rm eff}=\frac{a_\gamma}{8\pi^2}$$

### 7.3 Dieselbe Hierarchie auf drei Ebenen
- **O(1)** ($\zeta_b\approx\tfrac12$, $a_\gamma/8\pi^2\approx10^{-3}$): dimensionslos/topologisch — sauber.
- **$10^{122}$**: Energiedichte-Ebene ($M_{\rm Pl}^2/H^2$).
- **$10^{240}$**: Volumen-Ebene ($(M_{\rm Pl}/H)^4$). Mechanism 2 scheitert um $V_4$, weil er die holographische Reduktion $V_4\to A_2$ nicht einbaut — genau die Reduktion, die P5 postuliert.

Keine Inkonsistenz: dieselbe 122er-Hierarchie auf drei Ebenen, verbunden durch P5.

---

## 8. Rigorositäts-Audit: was *nicht* theorem-level abgeleitet ist (vollständig)

**Antwort auf die Leitfrage: P5 ist NICHT das einzige.** Vollständige Liste:

| Element | Inhalt | Status | Quelle | Trägt |
|---|---|---|---|---|
| **A2 / KP** | Vakuum-Sequestering | [POSTULAT] „treats KP as an input axiom" | Z.671 | Entfernung von $G$ |
| **A1-Skala** | $L_{HH}=1/H_0$ | [INPUT] „not a theorem" | Z.615 | Sattel↔Hubble — **§4.2/§6 adressiert via SB** |
| **A5** | Anomaly-Curvature-Correspondence | [POSTULAT] „irreducible physical-identification hypothesis" | Z.73, 139 | topolog. Quotient → Krümmung statt Vakuumenergie |
| **B1** | cap-saddle dominance / Picard–Lefschetz | [NUM] „numerically supported, RK45 thimble" | Z.73 | dass der cap-Sattel dominiert |
| **Vorzeichen** | HH- vs Vilenkin-Zweig | [NUM/offen] „strict no-boundary proof remains open" | Z.77 | $\Omega_K>0$ statt $<0$ |
| **P5** | holographische Akkumulation $N_{\rm eff}=M_{\rm Pl}^2/H^2$ | [POSTULAT] „not an independent dynamical proof… remains open" | Z.137 | **die 122er-Hierarchie** |
| **$\Omega_\Lambda$-Wert** | $\approx0.685$ | [INPUT] | Z.1852 | — bei *keinem* prior-unabhängigen Mechanismus ableitbar (§2.4, Lombriser §1) |

**Theorem-level (rigoros):** die Euklidische Seite — $a_\gamma=31/180$ (DeWitt–Schwinger), $\int_{D^4}Q_4=8\pi^2$ (Chang–Yang), die 12 Spektralresultate R1–R12, die cap-saddle-Gleichung, die 26 No-Go-Falsifizierungen. Das Verhältnis $a_\gamma/(8\pi^2)$ ist innerhalb des closed-manifold/WZ-Rahmens bewiesen.

**Nicht theorem-level:** alles, was die Euklidische Zahl mit der **beobachteten Lorentzschen Krümmung** verbindet — A5, B1, Vorzeichen, P5 — plus die beiden Inputs (A1-Skala, $\Omega_\Lambda$) und das Basis-Axiom A2.

### Sonderstellung von P5
P5 ist nicht das *einzige* offene Element, aber das **quantitativ kritischste**: es trägt allein die 122 Größenordnungen. A5/B1/Vorzeichen sind *strukturelle/Identifikations*-Hypothesen (O(1)-Konsequenzen); P5 ist die *Größenordnungs*-Brücke. Deshalb ist die nächste Sitzung (P5-Härtung) der Hebel mit dem höchsten Ertrag.

---

## 9. Stand & nächster Schritt

**Geschlossen/gehärtet diese Sitzung:**
- Lombriser-Zweig verworfen (Maß-Problem kategorisch).
- SB-Mechanismus als kausale Variation extrahiert und numerisch reproduziert.
- a_γ präzise in $L_{\rm matter}$ lokalisiert (der Term, den SB klassisch auf 0 setzen).
- Skala-Ecke $L_{HH}=1/H_0$ via $A/V\sim H_0$ legitimiert.
- Strukturelle Identität SB↔cap etabliert; cap-Restriktion durch SBs kausales Prinzip begründet.
- Dynamischer Weg als untauglich erwiesen (Frühzeit-Divergenz; $10^{240}$-Befund konsistent); topologischer Weg als notwendig.
- $10^{240}$ aufgeklärt: $=V_4$, konsistent; Hierarchie auf 3 Ebenen; in P5 verschoben.

**Offen (Priorität für nächste Sitzung):**
- **P5** — die holographische Akkumulation $N_{\rm eff}=M_{\rm Pl}^2/H^2$. Trägt die gesamte 122er-Hierarchie. Bisher nur durch (1) 't Hooft–Susskind-Bound (sättigt bis Faktor $\pi$), (2) die *triviale* Identität $V_4=A_2^2$ (selbst-deklariert „algebraically trivial", Z.6087), (3) $\pi$-Faktor-Analyse gestützt. Ein strikter Schwinger–Keldysh / BV-Master-Gleichungs-Loop-Beweis fehlt (Z.2554).

**Dokumentations-Korrektur ans Manuskript:** Mechanism-2-Eintrag (Z.5709) „$10^{240}$ in amplitude" entweder mit expliziter $V_4$-Herleitung versehen oder auf $10^{122}$ (Energiedichte-Ebene) vereinheitlichen — der unkommentierte Sprung 120→240 lädt zur Fehlinterpretation ein.
