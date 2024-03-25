import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.areSentencesSimilar(*test_input)

    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
                pass