# Woche 05: Statistik in der Genomik

Python-Beispiele zum Skriptum *„Statistik in der Genomik: Warum gute Daten allein nicht reichen“* zum Selbststudium.
In Woche 5 gibt es keine Pflichtübung.

## Notebook

`bioinf_w05_statistik.ipynb`

| Teil | Thema | Funktion(en) | Skriptum |
|---|---|---|---|
| 1 | Tidy Data mit pandas | `wide_to_tidy` | 4.2 |
| 2 | Anscombes Quartett | `summary_stats` | 5.1 |
| 3 | Welch-t-Statistik und Permutationstest | `welch_t`, `perm_p`, `exact_perm_p` | 6.1 bis 6.4 |
| 4 | Multiples Testen: Bonferroni und Benjamini-Hochberg | `bonferroni`, `benjamini_hochberg` | 7 |

## So arbeitest du

1. Notebook öffnen (Jupyter, VS Code oder Colab) und die Setup-Zelle ausführen. Fehlende Pakete
   (numpy, scipy, pandas, statsmodels, matplotlib, ipytest, pytest) werden dabei installiert.
2. Die Funktionsrümpfe mit `NotImplementedError` durch deine eigene Implementierung ersetzen.
3. Die Test-Zelle (`%%ipytest`) des jeweiligen Teils ausführen, bis alle Tests grün sind.

Die Beispieldaten in Teil 1 und 3 sind fiktiv. Die Simulation in Teil 4 liefert dieselben Zahlen wie im Skriptum.

Der Code ist durchgehend englisch (Funktionen, Variablen, Spaltennamen, Ausgaben). Kommentare und Tipps, die beim Lernen helfen, sind deutsch.
