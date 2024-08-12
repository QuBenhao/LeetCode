from itertools import accumulate

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largest1BorderedSquare(test_input)

    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pre_row = [list(accumulate(row, initial=0)) for row in grid]
        pre_col = [list(accumulate(col, initial=0)) for col in zip(*grid)]
        for d in range(min(m, n), 0, -1):
            for i in range(m - d + 1):
                for j in range(n - d + 1):
                    if pre_row[i][j + d] - pre_row[i][j] == d and \
                            pre_col[j][i + d] - pre_col[j][i] == d and \
                            pre_row[i + d - 1][j + d] - pre_row[i + d - 1][j] == d and \
                            pre_col[j + d - 1][i + d] - pre_col[j + d - 1][i] == d:
                        return d * d
        return 0
