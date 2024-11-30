# Make sure that the file BoyerMoore.py resides within the same folder
from BoyerMoore import BoyerMoore

# ABC --> Abstrac Basic Class
from abc import ABC, abstractmethod

class SearchAlgorithm(ABC):
    @abstractmethod # function decorator for abstract methods
    def search(self, pattern, text):
        pass

# Define 2 classes: one that implements naive exact matching and
# that implements BoyerMoore Algorithm. Make sure that both inherit
# from SearchAlgorithm

# your code ...



# Implement class metho `search` that delegate the search to the
# object containing an instance of `SearchAlgorithm`
class Search:
    # Construtor...
    def __init__(self, search_algo: SearchAlgorithm):
        self.search_algo = search_algo

    # your code ....
    
pattern = "ACGT"
text = "ACGTACGTACGTACGTACGTACGTACGTACGTA"

print(f'Searching for pattern: "{pattern}" in text: "{text}"......')

print("First using the NaivaExactMatching Search.....")

search = Search(NaiveExactMatchingSearch())
result_naive = search.search(pattern, text)
print(f'Offsets, using naive exact matching algorithm: {result_naive}')

print("Now using the BoyerMooretMatching Search.....")
search = Search(BoyerMooreSearch())
result_bm = search.search(pattern, text)
print(f'Offsets, using BoyerMoore matching algorithm: {result_bm}')

print(f'Both should be the same: assert result_naive==result_bm : {result_naive == result_bm}')
assert result_bm == result_naive