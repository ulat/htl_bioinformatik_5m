# Woche 08: Indexierung mit k-mer-Index und Hashtabelle

Python-Beispiele zum Skriptum *„Indexierung: k-mer-Index, Binärsuche und Hashtabelle“* als Programmieraufgaben. Das
Notebook ergänzt die Übung Ü2 (FASTA parsen) und ist in etwa 100 Minuten lösbar.

## Notebook

`bioinf_w08_index.ipynb`

| Teil | Thema | Funktion(en) | Skriptum |
|---|---|---|---|
| 1 | k-mer-Index als Dictionary | `build_kmer_index` | 3.1 |
| 2 | Abfrage mit Verifikation | `query_kmer_index` | 3.2, 3.3 |
| 3 | Sortierte Liste und Binärsuche (`bisect`) | `build_sorted_index`, `lookup_sorted_index` | 4.1 |
| 4 | Eigene Hashtabelle mit Kollisionen | `kmer_to_number`, `build_hash_table`, `lookup_hash_table` | 4.2 |
| 5 | Index mit jedem n-ten k-mer | `build_sparse_index`, `query_sparse_index` | 5.1 |
| 6 | Messungen an phiX174 und Fragen | | 3.4, 4.3, 6 |
| Bonus | Subsequenz-Index | `subsequence`, `build_subseq_index`, `query_subseq_index` | 5.2 |

Die Werkzeuge aus Woche 6 (`read_genome`, `read_fastq`, `naive_with_counts`) sind fertig vorgegeben. Zum Vergleich
eignet sich das Kursnotebook `2.02_SubstringIndex.ipynb` im Hauptordner.

## Daten

Das Notebook verwendet `phix.fa`, `ERR266411_1.first1000.fastq` und `lambda_virus.fa`. Alle drei liegen im Hauptordner
dieses Repositorys und werden automatisch gefunden (gesucht wird im Notebook-Ordner, in `daten/`, in `../daten/` und
in `..`).

## So arbeitest du

1. Notebook öffnen (Jupyter, VS Code oder Colab) und die Setup-Zelle ausführen. Fehlende Pakete (ipytest, pytest)
   werden dabei installiert.
2. Die Funktionsrümpfe mit `NotImplementedError` durch deine eigene Implementierung ersetzen.
3. Die Test-Zelle (`%%ipytest`) des jeweiligen Teils ausführen, bis alle Tests grün sind.

Der Code ist durchgehend englisch (Funktionen, Variablen, Ausgaben). Kommentare und Tipps, die beim Lernen helfen, sind deutsch.
