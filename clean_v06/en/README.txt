CSG-KP — Manuscript and verification (English)
==============================================

Contents:
  csg_kp_manuscript.pdf     the manuscript (9 pp; lay prologue + first-principles body)
  csg_kp_manuscript.tex     LaTeX source
  csg_kp_falsification.py   computing verification / falsification pipeline
  Anschreiben_Hoever.txt    cover letter to Prof. Hoever (template, German)
  README.txt                this file

Run the pipeline:
  python3 csg_kp_falsification.py      (dependency: numpy)
  exit code 0  <=>  all proved checks pass.

Logical status (short; details in §14):
  proved      a_γ=31/180, ∫E₄=64π², C_Q=8π², R1–R12, 4a_γ (two routes),
              ratio a_γ/8π², sign Ω_K>0, lift scaling
  postulated  Ω_Λ = 4a_γ  (the identification A5/P5, §13)
  empirical   w=-1, numerical Ω values (DESI DR3 / Euclid, open)

Layout: line spacing 1.25; margins 0.96 cm.
