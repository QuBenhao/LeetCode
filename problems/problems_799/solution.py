import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.champagneTower(*test_input)

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        f = [[0.0] * (query_row + 1) for _ in range(query_row + 1)]
        f[0][0] = poured
        for i in range(query_row):
            for j in range(i + 1):
                if f[i][j] <= 1:
                    continue
                f[i + 1][j] += (f[i][j] - 1) / 2.0
                f[i + 1][j + 1] += (f[i][j] - 1) / 2.0
        return min(1.0, f[query_row][query_glass])
