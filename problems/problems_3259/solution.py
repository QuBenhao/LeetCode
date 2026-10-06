from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxEnergyBoost(*test_input)

    def maxEnergyBoost(self, a: List[int], b: List[int]) -> int:
        c = (a, b)

        @cache  # Cache decorator to avoid recomputing dfs results (memoization)
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return 0
            return max(dfs(i - 1, j), dfs(i - 2, j ^ 1)) + c[j][i]

        return max(dfs(len(a) - 1, 0), dfs(len(a) - 1, 1))
