from functools import cache
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCost(*test_input)

    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        @cache
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return m * n - waitCost[i][j]
            ans = inf
            if i < m - 1:
                ans = min(ans, dfs(i + 1, j) + waitCost[i+1][j])
            if j < n - 1:
                ans = min(ans, dfs(i, j + 1) + waitCost[i][j+1])
            return ans + (i + 1) * (j + 1)

        return dfs(0, 0)
