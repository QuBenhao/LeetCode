from functools import cache
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumSum(test_input)

    def minimumSum(self, grid: List[List[int]]) -> int:
        @cache
        def helper(left, right, top, bottom):
            l, r, t, b = right + 1, left - 1, bottom + 1, top - 1
            for _i in range(top, bottom + 1):
                for _j in range(left, right + 1):
                    if grid[_i][_j] == 1:
                        l = min(l, _j)
                        r = max(r, _j)
                        t = min(t, _i)
                        b = max(b, _i)
            return (r - l + 1) * (b - t + 1) if l <= r and t <= b else 1

        m, n = len(grid), len(grid[0])
        ans = inf
        # 枚举左上角的矩形
        for i in range(m):
            for j in range(n):
                if i == m - 1 and j == n - 1:
                    continue
                first = helper(0, j, 0, i)
                if j == n - 1:
                    # 横切
                    for x in range(i + 1, m - 1):
                        ans = min(ans, first + helper(0, n - 1, i + 1, x) + helper(0, n - 1, x + 1, m - 1))
                    # 竖切
                    for y in range(n - 1):
                        ans = min(ans, first + helper(y + 1, n - 1, i + 1, m - 1) + helper(0, y, i + 1, m - 1))
                elif i == m - 1:
                    # 横切
                    for x in range(m - 1):
                        ans = min(ans, first + helper(j + 1, n - 1, 0, x) + helper(j + 1, n - 1, x + 1, m - 1))
                    # 竖切
                    for y in range(j + 1, n - 1):
                        ans = min(ans, first + helper(y + 1, n - 1, 0, m - 1) + helper(j + 1, y, 0, m - 1))
                else:
                    # 横切
                    ans = min(ans, first + helper(j + 1, n - 1, 0, i) + helper(0, n - 1, i + 1, m - 1))
                    # 竖切
                    ans = min(ans, first + helper(0, j, i + 1, m - 1) + helper(j + 1, n - 1, 0, m - 1))
        return ans
