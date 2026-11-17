# Woche 07: Boyer-Moore und Preprocessing

Python-Beispiele zum Skriptum *„Boyer-Moore und Preprocessing“* als Programmieraufgaben. Das Notebook ergänzt die
Übung Ü1 (DNA-Strings) und ist in etwa 100 Minuten lösbar.

## Notebook

`bioinf_w07_boyer_moore.ipynb`

| Teil | Thema | Funktion(en) | Skriptum |
|---|---|---|---|
| 1 | Bad-Character-Regel und Tabelle | `bad_character_shift`, `bad_character_table` | 3, 6.1 |
| 2 | Good-Suffix-Regel, Verschiebung nach einem Treffer | `good_suffix_shift`, `match_shift` | 4 |
| 3 | Preprocessing und Boyer-Moore mit Zählern | `preprocess`, `boyer_moore_with_counts` | 5, 6 |
| 4 | Naiv gegen Boyer-Moore an phiX174 und echten Reads | `compare_algorithms` | 7 |
| 5 | Fragen zu Laufzeit, online/offline und Alphabet | | 6.3, 7, 8 |

Die Werkzeuge aus Woche 6 (`read_genome`, `read_fastq`, `reverse_complement`, `naive_with_counts`) sind fertig
vorgegeben. Zum Vergleich liegt Langmeads Implementierung als `BoyerMoore.py` im Hauptordner (siehe auch
`2.01_BoyerMoore.ipynb`).

## Daten

Das Notebook verwendet `phix.fa` und `ERR266411_1.first1000.fastq`. Beide liegen im Hauptordner dieses Repositorys
und werden automatisch gefunden (gesucht wird im Notebook-Ordner, in `daten/`, in `../daten/` und in `..`).

## So arbeitest du

1. Notebook öffnen (Jupyter, VS Code oder Colab) und die Setup-Zelle ausführen. Fehlende Pakete (ipytest, pytest)
   werden dabei installiert.
2. Die Funktionsrümpfe mit `NotImplementedError` durch deine eigene Implementierung ersetzen.
3. Die Test-Zelle (`%%ipytest`) des jeweiligen Teils ausführen, bis alle Tests grün sind.

Der Code ist durchgehend englisch (Funktionen, Variablen, Ausgaben). Kommentare und Tipps, die beim Lernen helfen, sind deutsch.
