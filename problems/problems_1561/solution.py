import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxCoins(test_input)

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        return sum(piles[len(piles) // 3:][::2])

