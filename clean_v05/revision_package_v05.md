# CSG-KP — Überarbeitungs-Paket (Revision v0.4 → v0.5)

Basis: Peer-Review + harter Prüfdurchgang (formale Kette, A1-Fundament, Selbst-Falsifikation).
Status je Eintrag: **[kritisch]** muss vor Einreichung · **[wichtig]** sollte · **[red.]** Klarheit.
Original-Manuskript bleibt unangetastet; dies ist ein anzuwendender Patch.

---

## 1. [kritisch] Fundament A1 ehrlich als belastet kennzeichnen

**Wo:** Axiom-Liste (A1) und Foundations-Sektion.
**Problem:** A1 (No-Boundary) wird als gegebenes Axiom geführt; die gesamte Lorentzsche
Seite (A5b, A6, FLT) ruht darauf. Feldbrugge–Lehners–Turok (PRL 119, 171301, 2017;
PRD 97, 023509, 2018) zeigen via Picard–Lefschetz instabile, wachsende Fluktuationen
der No-Boundary-Wellenfunktion. Die Kontroverse ist offen (Diaz Dorronsoro et al.,
PRD 96, 043505; Di Tucci–Lehners, PRD bestätigend), aber das Manuskript zitiert
Feldbrugge2017 nur am Rand.
**Änderung:** A1 explizit als *nicht etabliert, in der Literatur bestritten* kennzeichnen.
Einfügen (sinngemäß): „A1 ist kein gesichertes Resultat. Die Lorentzsche Realisierung
der No-Boundary-Wellenfunktion wird durch das FLT-Instabilitätsargument belastet; die
Frage ist offen. Alle in diesem Manuskript als A5b/A6/FLT geführten offenen Punkte sind
gekoppelte Manifestationen genau dieser einen offenen Frage."

## 2. [kritisch] Neues Axiom A6 (Persistenz) explizit benennen

**Wo:** Axiom-Liste, neu nach A5.
**Problem:** Dass das *heute beobachtete* Ω_K/Ω_Λ gleich dem euklidischen ρ_E ist, setzt
voraus, dass die Anomalie-Geometrie die Krümmung bis heute dominiert und nicht von
zwischenzeitlicher Dynamik überschrieben wird (in Standard-Inflation gilt Ω_K→0). Diese
Annahme war implizit. Sie folgt **nicht** aus A1 (die Lorentzsche φ₀ ist frei, vgl.
Selbstkonsistenz-Sektion).
**Änderung:** „**A6 (Persistenz).** Die durch A5 identifizierte Anomalie-Geometrie ist die
dominante Quelle der gegenwärtigen Krümmung; sie wird nicht durch eine zwischenzeitliche
inflationäre oder dynamische Phase auf Ω_K→0 reduziert." Falls eine Ableitung aus A1
gelingt, A6 als Lemma führen; sonst als Postulat ausweisen.

## 3. [kritisch] Status-Korrektur: C_Q-Selektion ist nicht rein Theorem

**Wo:** Lemma 1 / Definition von C_Q.
**Problem:** Der Wert C_Q = 8π² ist Theorem; die *Selektion* (Integration über die
Hemisphäre statt volle Sphäre, Q-Ladung statt Euler-Ladung) als der relevante Nenner ist
DERIVED-given-A1 + Uniqueness-Kriterien (i)–(iv), nicht [THM].
**Änderung:** Statuszeile trennen: „Der Wert ∫_{D⁴}Q₄ = 8π² ist ein Theorem (Chang–Yang).
Dass dieser (Hemisphäre, Q-Ladung) der physikalisch relevante Nenner ist, folgt aus A1
und der Uniqueness-Proposition innerhalb der Kriterien (i)–(iv); es ist kein
unbedingtes Minimalitätsresultat."

## 4. [kritisch] Titel/Abstract entschärfen

**Wo:** Titel + Abstract.
**Problem:** „Resolution of the cosmological constant problem" überschreibt den
Liefergegenstand (falsifizierbares Verhältnis + benannte Postulate A5/P5/A6).
**Änderung:** Titel → z. B. „A parameter-free, falsifiable curvature ratio from the photon
conformal anomaly". „Resolution" entfernen; Abstract-Satz ergänzen: „The empirical content
passes through a single identification postulate (A5) and is sharply falsifiable; the
magnitude and absolute Ω_Λ rest on the separate postulate P5 and remain open."

## 5. [kritisch] Direkte Konkurrenz zitieren und vergleichen

**Wo:** Einleitung / Diskussion, neue Vergleichstabelle.
**Problem:** Boyle–Turok (CPT) und Deng–Handley (PRD 110, 103528, 2024; PRD 113, 023546,
2026) fehlen — die einzigen anderen parameterfreien Ω_K-Vorhersagen.
**Änderung:** Beide zitieren. Tabelle: Vorhersagetyp (CSG fester Einzelwert + Vorzeichen-
*Output* vs. Deng–Handley diskretes, über Versionen wanderndes Spektrum mit gefittetem Δk
und *eingebautem* geschlossenem Vorzeichen). Der Vorzeichen-Kontrast (CSG offen vs. beide
geschlossen) macht die Vorhersagen durch DR3/Euclid gegenseitig diskriminierbar — das
*stärkt* CSG und gehört in den Text.

## 6. [wichtig] Edge-Mode-Anspruch entschärfen

**Wo:** Foundations / P5-Triangulation, Maxwell-EE-Passage.
**Problem:** Die Maxwell-EE-Diskrepanz (−16/45 vs −31/45) und ihre Edge-Mode-Auflösung sind
etablierte Literatur (Casini–Huerta 2015; Donnelly–Wall PRL 114, 2015 — „two-decades old
puzzle"; Casini et al. PRD 101, 2020: Auflösung als „effective correction to the
four-sphere partition function"). CSG *reproduziert* dies, originiert es nicht.
**Änderung:** Von „resolved through / prediction" auf „CSG's spectral machinery
*reproduces* the established Donnelly–Wall/Casini–Huerta resolution — a consistency check
on the apparatus, A5-independent, not a novel prediction." Keinerlei „we solve/resolve".

## 7. [wichtig] w-Spannung als Hauptrisiko führen

**Wo:** Abstract + Falsifikationssektion (aus „robustness #6" herausheben).
**Änderung:** Explizit: „Die Verhältnis-Ableitung setzt w_eff = −1 (konstantes Λ) voraus.
Eine bestätigte DESI-w₀wₐ-Dynamik bedroht diese Voraussetzung; die Anomalie-Stärke
ν ~ a_γ/8π² ist um ~2 Größenordnungen zu klein, um sie zu absorbieren. Ungeklärt."

## 8. [wichtig] Testzahlen-Vorbehalt aus run_all.py ins Manuskript

**Wo:** Code-and-data-Sektion.
**Änderung:** Den Selbst-Vorbehalt übernehmen: welche der 37 Module harte numerische
Assertions tragen und welche Argument-/Reduktions-Essays sind, die „durch Laufen bestehen".

## 9. [wichtig] Λ* < 0 vs. beobachtetes Ω_Λ > 0 klarstellen

**Wo:** Selbstkonsistenz-Sektion.
**Änderung:** Ein Absatz: das bewiesene negative Λ* ist *nicht* die beobachtete positive
Dunkle Energie; letztere bleibt via φ₀ frei (Ω_Λ = (V(φ₀)−Λ*)/3). Verwechslung „Λ fixiert"
= „DE fixiert" ausräumen.

## 10. [red.] Formale Kette als eigene Sektion einbauen

**Wo:** Neue Sektion (vor oder nach der Hauptableitung).
**Änderung:** `formal_derivation_skeleton.tex` integrieren. Sie ersetzt verstreute verbale
Übergänge durch eine Kette S1–S7 mit Status je Schritt und isoliert den einen
nicht-deduktiven Sprung (A5b: erhält die Wick-Map Φ den skalenfreien Quotienten?).

## 11. [red.] Offene Punkte konsolidieren

**Wo:** Mehrere „honest status"-Absätze (sec:psf, sec:ladder, sec:coherence, sec:found).
**Änderung:** In *einen* Abschnitt zusammenführen, strukturiert als: A5b/A6/FLT =
gekoppelte Manifestationen der einen offenen Frage (Lorentzsche Realisierung von A1);
P5 = separater Magnitude-Postulateintritt; absolutes Ω_Λ = Konjektur (Ladder). ~30 %
Redundanz kürzbar.

---

## Was NICHT geändert werden darf
Status-Ledger, retrahierte Artefakte (mean_R_over_4, c=1.86), die „sobering picture"-
Ehrlichkeit der Selbstkonsistenz-Sektion. Das ist der Aktivposten; Glätten schwächt die Arbeit.

## Nicht aufnehmen (von der Selbst-Falsifikation verworfen)
- „A5b/A6/FLT sind *ein* Problem" — sie sind gekoppelt, nicht identisch.
- „A1 ist widerlegt" — A1 ist umstritten, nicht widerlegt.
- „CSGs Robin-BC = FLT-Rettungs-Robin-BC" — verschiedene Objekte; ungeprüft; nicht behaupten.
