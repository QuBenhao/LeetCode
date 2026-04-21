import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.twoEditWords(*test_input)

    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def distance(a, b):
            return sum(i != j for i, j in zip(a, b))

        return [word for word in queries if any(distance(word, wd) <= 2 for wd in dictionary)]
