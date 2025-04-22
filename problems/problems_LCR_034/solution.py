import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isAlienSorted(*test_input)

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {c: i for i, c in enumerate(order)}
        return words == sorted(words, key=lambda x: [order_map[c] for c in x])
