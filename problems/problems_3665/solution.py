from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.uniquePaths(test_input)

    def uniquePaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i, j, d):
            if i == m or j == n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if grid[i][j] == 1:
                if d == 0:
                    return dfs(i + 1, j, 1) % MOD
                else:
                    return dfs(i, j + 1, 0) % MOD
            return dfs(i + 1, j, 1) + dfs(i, j + 1, 0) % MOD

        return dfs(0, 0, 0) % MOD

MOD = 10 ** 9 + 7
