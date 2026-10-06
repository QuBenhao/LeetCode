from itertools import accumulate

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumScore(test_input)

    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        col_sum = [list(accumulate(col, initial=0)) for col in zip(*grid)]

        f = [[[0, 0] for _ in range(n + 1)] for _ in range(n)]
        for j in range(n - 1):
            # Optimize with prefix maxima
            pre_max = f[j][0][1] - col_sum[j][0]
            for pre in range(1, n + 1):
                f[j + 1][pre][0] = f[j + 1][pre][1] = max(f[j][pre][0], pre_max + col_sum[j][pre])
                pre_max = max(pre_max, f[j][pre][1] - col_sum[j][pre])

            # Optimize with suffix maxima
            suf_max = f[j][n][0] + col_sum[j + 1][n]
            for pre in range(n - 1, 0, -1):
                f[j + 1][pre][0] = max(f[j + 1][pre][0], suf_max - col_sum[j + 1][pre])
                suf_max = max(suf_max, f[j][pre][0] + col_sum[j + 1][pre])

            # Compute the pre=0 state separately
            f[j + 1][0][0] = suf_max  # No need to consider f[j][0][0], since three consecutive columns cannot all be white
            f[j + 1][0][1] = max(f[j][0][0], f[j][n][0])  # Column j is either entirely white or entirely black

        return max(f[-1][i][0] for i in range(n + 1))
