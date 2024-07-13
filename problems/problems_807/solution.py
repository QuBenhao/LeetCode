import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxIncreaseKeepingSkyline(test_input)

    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max, col_max = [max(row) for row in grid], [max(col) for col in zip(*grid)]
        return sum(min(row_max[i], col_max[j]) - grid[i][j] for i in range(len(grid)) for j in range(len(grid[0])))
