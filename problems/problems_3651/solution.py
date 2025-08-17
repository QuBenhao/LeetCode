from math import inf

from sortedcontainers import SortedDict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCost(*test_input)

    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[inf] * n for _ in range(m)] for _ in range(k + 1)]
        dp[0][0][0] = 0
        for i in range(m):
            for j in range(n):
                if i + 1 < m:
                    dp[0][i + 1][j] = min(dp[0][i + 1][j], dp[0][i][j] + grid[i + 1][j])
                if j + 1 < n:
                    dp[0][i][j + 1] = min(dp[0][i][j + 1], dp[0][i][j] + grid[i][j + 1])
        sd = SortedDict()
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if -v not in sd:
                    sd[-v] = []
                sd[-v].append((i, j))
        for kk in range(1, k + 1):
            mn = inf
            for v, points in sd.items():
                for i, j in points:
                    mn = min(mn, dp[kk - 1][i][j])
                for i, j in points:
                    dp[kk][i][j] = mn
            for i in range(m):
                for j in range(n):
                    if i + 1 < m:
                        dp[kk][i + 1][j] = min(dp[kk][i + 1][j], dp[kk][i][j] + grid[i + 1][j])
                    if j + 1 < n:
                        dp[kk][i][j + 1] = min(dp[kk][i][j + 1], dp[kk][i][j] + grid[i][j + 1])
        return min(dp[i][m - 1][n - 1] for i in range(k + 1))
