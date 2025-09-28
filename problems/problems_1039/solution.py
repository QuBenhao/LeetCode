from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minScoreTriangulation(test_input)

    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dfs(l, r):
            return min(dfs(l, k) + dfs(k, r) +
                       values[l] * values[r] * values[k] for k in range(l + 1, r)) if r - l >= 2 else 0

        return dfs(0, len(values) - 1)
