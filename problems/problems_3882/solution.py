import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCost(test_input)

    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 用 (1 << 1024) - 1 表达当前格子的值域
        FULL = (1 << 1024) - 1
        def xor(s, a):
            new_s = 0
            while s:
                low = s & -s
                new_s |= 1 << ((low.bit_length() - 1) ^ a)
                s ^= low
            return new_s

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 << grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                v = 0
                if i:
                    v |= dp[i - 1][j]
                if j:
                    v |= dp[i][j - 1]
                if v == FULL:
                    return 0
                dp[i][j] = xor(v, grid[i][j])
        return (dp[m - 1][n - 1] & -dp[m - 1][n - 1]).bit_length() - 1
