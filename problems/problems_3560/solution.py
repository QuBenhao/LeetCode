import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCuttingCost(*test_input)

    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n <= k and m <= k:
            return 0
        return k * (max(m, n) - k)
