CSG-KP — Manuskript und Verifikation (deutsche Fassung)
=======================================================

Inhalt:
  csg_kp_manuskript.pdf     das Manuskript (9 Seiten, mit Prolog, erste Prinzipien)
  csg_kp_manuskript.tex     LaTeX-Quelltext
  csg_kp_falsifikation.py   rechnende Verifikations-/Falsifikations-Pipeline
  Anschreiben_Hoever.txt    Anschreiben (Vorlage)
  README.txt                diese Datei

Pipeline ausführen:
  python3 csg_kp_falsifikation.py      (Abhängigkeit: numpy)
  Rückgabewert 0  <=>  alle bewiesenen Prüfungen bestehen.

Logischer Status (Kurzfassung, Details in §14 des Manuskripts):
  bewiesen     a_γ=31/180, ∫E₄=64π², C_Q=8π², R1–R12, 4a_γ (zwei Wege),
               Verhältnis a_γ/8π², Vorzeichen Ω_K>0, Lift-Skalierung
  postuliert   Ω_Λ = 4a_γ  (die Identifikation A5/P5, §13)
  empirisch    w=-1, numerische Ω-Werte (DESI DR3 / Euclid, offen)

Layout: Zeilenabstand 1,25; Ränder 0,96 cm.
