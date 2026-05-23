# Prüfprompt — CSG-KP rigoros falsifizieren (neuer Chat)

> In neuen Chat einfügen und das Paket `csg-kp-clean.zip` anhängen.

---

Du bist ein maximal kritischer Gutachter (Referee-Modus, zero confirmation bias).
Ich hänge ein Paket an (`csg-kp-clean.zip`): ein Manuskript plus Python-Module, das
behauptet, die kosmologische Konstante / Krümmung über eine konforme-Anomalie-Konstruktion
zu erklären, mit der scharfen Vorhersage

    |Ω_K| / Ω_Λ = a_γ / (8π²) = 31/(1440π²) ≈ 2.181e-3,  also Ω_K ≈ +1.49e-3 (offen).

Deine Aufgabe ist **Falsifikation, nicht Bestätigung**. Bewerte beide Seiten gleichwertig,
rede nichts schön, und sage klar, wo die Kette hält und wo sie bricht. Keine Gefälligkeit.

## Vorgehen

1. **Reproduziere die Rechnungen.** Entpacke das Zip, lies `README.md`, führe
   `python3 python/run_all.py` aus (12 Module). Prüfe, ob die Zahlen wirklich aus den
   Rechnungen folgen oder ob irgendwo ein Ergebnis hartcodiert / zirkulär ist. Nimm
   Stichproben: rechne `a_γ = 31/180`, `∫_{D⁴}Q₄ = 8π²`, das Sattel-Polynom (Grad 8) und
   die ζ(0)=−4a_γ-Identität unabhängig nach.

2. **Greife jeden Baustein einzeln an** und urteile „hält / bricht / bedingt":
   - **a_γ = 31/180** aus der Gilkey-b₄-Heat-Kernel-Spur (Maxwell − 2·Ghost auf S⁴).
     Stimmt die Operatorzerlegung? Ist der Skalar-Check 1/360 wirklich unabhängig?
   - **8π² = ∫Q₄** als topologische Q-Krümmungs-Ladung von D⁴ (Chang–Yang). Korrekt?
   - **cap-Stabilität** via Gebietsmonotonie + positives geschlossenes S⁴-Spektrum.
     Ist die Monotonie-Aussage korrekt angewandt? Ist die ℓ=0-Konformmode wirklich die
     einzige negative Richtung?
   - **A2-Kontraktion** L=|1+G′|<1 via G′(Λ)<0. Folgt G′<0 wirklich analytisch, oder ist
     die Monotonie der Spurfunktion eine versteckte Annahme?
   - **B1′ Thimble-Enumeration**: ist die Polynom-Reduktion u=e^{iz} → Grad 8 wirklich
     *vollständig* (alle Sättel), und ist „Im Γ const entlang Thimble ⇒ n_complex=0"
     korrekt argumentiert? Sind die komplexen log-Zweige von V′(φ)=0 zu Recht als
     unphysikalisch abgetan?
   - **Pfadintegral-Synthese**: die Faktorisierung homogen×inhomogen ist nur auf
     quadratischem Niveau exakt. Hält die Behauptung der Ein-Loop-Exaktheit?
   - **all-orders-Stabilität**: die *entscheidende Annahme* ist „CSG = klassische
     Gravitation, keine Graviton-Loops". Ist das physikalisch haltbar? Was bricht, wenn
     die Gravitation doch quantisiert werden muss? Ist die Entkopplung der φ⁴-Borel-Frage
     vom Verhältnis wirklich sauber, oder verschiebt sich das Problem nur?

3. **Attackiere die ehrlich offenen / nicht-bewiesenen Punkte** (im Manuskript als solche
   markiert) am härtesten — hier ist das Framework am verwundbarsten:
   - **A5 (Anomalie-Krümmungs-Korrespondenz)**: die *physikalische* Identifikation der
     Euklidischen Anomalie mit der Lorentzschen Friedmann-Krümmung. Das ist ein Postulat,
     kein Theorem. Ist es zwingend, oder nur konsistent?
   - **A5c (Referenz-Epoche / Datenanker)**: die einzige „echte Wahl". Wie viel
     Fit-Freiheit steckt darin wirklich? Ist Ω_K/Ω_Λ∝(1+z)² eine Ausrede oder ein echter
     Constraint?
   - **KP-Sequestering**: als Axiom adoptiert (nicht aus tieferer Theorie hergeleitet).
   - **Lombriser-Koinzidenz Ω_Λ=0.704**: hängt an y(t₀)=½. Zirkulär?
   - **Vorzeichen / Euklidisch-vs-Lorentz**: HH- vs Vilenkin-Zweig. Ist die HH-Wahl
     erzwungen oder bevorzugt? Die Feldbrugge–Lehners–Turok-Kritik am no-boundary-Maß.

4. **Empirischer Falsifikationstest.** Die Vorhersage Ω_K=+1.49e-3 (offen) ist scharf und
   parameterfrei. Prüfe per Websuche den **aktuellen** Stand: DESI DR2/DR3 und Euclid
   zur Krümmung Ω_K. Liegt die Messung mit der Vorhersage im Konflikt? Schließt das
   geschlossene (Vilenkin-)Vorzeichen schon aus? Wie nah ist die aktuelle Sensitivität an
   ±1.5e-3? (Vorsicht: Ω_K-Constraints sind oft prior-/datensatz-abhängig — sei skeptisch
   gegenüber einzelnen Zahlen.)

5. **Urteil.** Trenne sauber: (a) was ist *Theorem* (Euklidisch-konform-topologisch),
   (b) was ist *bedingt bewiesen* (innerhalb Annahmen wie CSG), (c) was ist *Postulat*
   (A5, A5c, KP), (d) was ist *empirisch entscheidbar*. Nenne den **einen Punkt, dessen
   Fall das ganze Framework fällt**, und sage, ob die aktuellen Daten ihn stützen oder
   gefährden.

Sei konkret, rechne nach wo möglich, und unterscheide „ist falsch" von „ist unbewiesen"
von „ist Geschmackssache". Wenn etwas hält, sag das auch — aber nur nach echtem Angriff.
