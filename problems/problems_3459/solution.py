from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.lenOfVDiagonal(test_input)

    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        DIRS = (1, 1), (1, -1), (-1, -1), (-1, 1)
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(i: int, j: int, k: int, can_turn: bool, target: int) -> int:
            i += DIRS[k][0]
            j += DIRS[k][1]
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != target:
                return 0
            res = dfs(i, j, k, can_turn, 2 - target)
            if can_turn:
                maxs = (m - i - 1, j, i, n - j - 1)  # 理论最大值（走到底）
                k = (k + 1) % 4
                # 优化二：如果理论最大值没有超过 res，那么不递归
                if maxs[k] > res:
                    res = max(res, dfs(i, j, k, False, 2 - target))
            return res + 1

        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x != 1:
                    continue
                maxs = (m - i, j + 1, i + 1, n - j)  # 理论最大值（走到底）
                for k, mx in enumerate(maxs):  # 枚举起始方向
                    # 优化一：如果理论最大值没有超过 ans，那么不递归
                    if mx > ans:
                        ans = max(ans, dfs(i, j, k, True, 2) + 1)
        return ans


