import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sortMatrix(test_input)

    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(2 * n - 1):
            diagonal = []
            start = (i, 0) if i < n else (0, i - n + 1)
            row, col = start
            while row < n and col < n:
                diagonal.append(grid[row][col])
                row += 1
                col += 1
            diagonal.sort(reverse=i < n)
            row, col = start
            for val in diagonal:
                grid[row][col] = val
                row += 1
                col += 1
        return grid
