from functools import cache
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxProductPath(test_input)

    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i, j):
            val = grid[i][j]
            if i == m - 1 and j == n - 1:
                return val, val
            ans_mn, ans_mx = inf, -inf
            if i < m - 1:
                mn, mx = dfs(i + 1, j)
                a, b = mn * val, mx * val
                ans_mn = min(a, b)
                ans_mx = max(a, b)
            if j < n - 1:
                mn, mx = dfs(i, j + 1)
                a, b = mn * val, mx * val
                ans_mn = min(ans_mn, a, b)
                ans_mx = max(ans_mx, a, b)
            return ans_mn, ans_mx

        _, ans = dfs(0, 0)
        return ans % MOD if ans >= 0 else -1

MOD = 10**9 + 7
