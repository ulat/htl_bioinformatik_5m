from BoyerMoore import BoyerMoore
from typing import Callable, List

### Erklärung der Typisierungen:

# 1. **`SearchFunction`**: Eine Typdefinition mittels `Callable[[str, str], List[int]]`, die angibt, 
# dass eine Suchfunktion zwei Zeichenketten (`pattern` und `text`) als Argumente nimmt und eine Liste 
# von Ganzzahlen (`List[int]`) zurückgibt.

# 2. **Funktionale Typisierungen**:
#    - `naive_exact_matching_search()` und `boyer_moore_search()` geben jeweils `SearchFunction`-Typen 
# zurück, das heißt, sie geben eine Funktion zurück, die selbst einen String-Pattern und einen String-Text
# als Argumente akzeptiert und eine Liste von Integer-Offsets zurückgibt.
  
# 3. **`search()` Funktion**:
#    - Diese Funktion ist ebenfalls als `SearchFunction` typisiert. Sie akzeptiert eine andere Suchfunktion
# und gibt eine Closure zurück, die ebenfalls diesen Typ erfüllt.

# Indem Typinformationen hinzugefügt werden, wird die Absicht des Codes klarer und das Risiko von 
# Laufzeitfehlern aufgrund von falschen Typen verringert.
# -------


# Implement Callable `SearchFunction`

# ... your code 


def naive_exact_matching_search() -> SearchFunction:
    # implement function `search` within function `naive_exact_matching_search` that uses 
    # naiveexact matching algorithm.
    
    # ... your code 
    
    return search

def boyer_moore_search(alphabet='ACGT') -> SearchFunction:
    
    # do the same as with exactnaive matching but with BoyerMoore
    
    def _get_pbm(pattern: str) -> BoyerMoore:
        return BoyerMoore(pattern, alphabet)

    def search(pattern: str, text: str) -> List[int]:
        
        # do not forget to generate the BoyerMoore Pattern-Preprocessing Object
        # you could use another function within the `search`-function
        
        # ... your code 
        
        return occurrences
    return search


def search(search_func: SearchFunction) -> SearchFunction:
    def search_closure(pattern: str, text: str) -> List[int]:
        return search_func(pattern, text)
    return search_closure

# Similarly, define the text and pattern
pattern = "ACGT"
text = "ACGTACGTACGTACGTACGTACGTACGTACGTA"

print(f'Searching for pattern: "{pattern}" in text: "{text}"......')

print("First using the Naive Exact Matching Search.....")
naive_search = search(naive_exact_matching_search())
result_naive = naive_search(pattern, text)
print(f'Offsets, using naive exact matching algorithm: {result_naive}')

print("Now using the Boyer Moore Matching Search.....")
bm_search = search(boyer_moore_search())
result_bm = bm_search(pattern, text)
print(f'Offsets, using BoyerMoore matching algorithm: {result_bm}')

print(f'Both should be the same: assert result_naive==result_bm : {result_naive == result_bm}')
assert result_bm == result_naive