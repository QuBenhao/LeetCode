import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCuttingCost(*test_input)

    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n <= k and m <= k:
            return 0
        if n > k:
            return k * (n-k)
        if m > k:
            return k * (m-k)
        return 0

