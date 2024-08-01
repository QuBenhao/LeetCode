import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfRightTriangles(test_input)

    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_counts, col_counts = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    row_counts[i] += 1
                    col_counts[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans += (row_counts[i] - 1) * (col_counts[j] - 1)
        return ans
