# Woche 06: Strings, Reads und exaktes Matching

Python-Beispiele zum Skriptum *„Strings, Reads und das Matching-Problem“* als Programmieraufgaben zum Selbststudium.
In Woche 6 gibt es noch keine Pflichtübung; das Notebook ist in etwa 100 Minuten lösbar.

## Notebook

`bioinf_w06_strings_matching.ipynb`

| Teil | Thema | Funktion(en) | Skriptum |
|---|---|---|---|
| 1 | Präfix, Suffix, reverses Komplement | `prefixes`, `suffixes`, `reverse_complement` | 4.2, 4.3 |
| 2 | Reads als zufällige Teilstrings | `random_dna`, `generate_reads` | 2.2 |
| 3 | Naiver Algorithmus, Vergleiche zählen, Laufzeit | `naive`, `find_all`, `naive_with_counts`, `comparison_bounds`, `estimate_runtime_years` | 5 |
| 4 | FASTA und FASTQ einlesen | `read_genome`, `read_fastq` | 6.2 |
| 5 | Echte Reads gegen phiX174 | `count_matched`, `circularize` | 6.3, 6.4 |

## Daten

Das Notebook verwendet `phix.fa` und `ERR266411_1.first1000.fastq`. Beide liegen im Hauptordner dieses Repositorys
und werden automatisch gefunden (gesucht wird im Notebook-Ordner, in `daten/`, in `../daten/` und in `..`).

## So arbeitest du

1. Notebook öffnen (Jupyter, VS Code oder Colab) und die Setup-Zelle ausführen. Fehlende Pakete (ipytest, pytest)
   werden dabei installiert.
2. Die Funktionsrümpfe mit `NotImplementedError` durch deine eigene Implementierung ersetzen.
3. Die Test-Zelle (`%%ipytest`) des jeweiligen Teils ausführen, bis alle Tests grün sind.

Der Code ist durchgehend englisch (Funktionen, Variablen, Ausgaben). Kommentare und Tipps, die beim Lernen helfen, sind deutsch.
