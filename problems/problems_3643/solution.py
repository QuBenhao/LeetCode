import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.reverseSubmatrix(*test_input)

    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k // 2):
            grid[x + i][y:y + k], grid[x + k - 1 - i][y: y + k] = grid[x + k - 1 - i][y: y + k], grid[x + i][y:y + k]
        return grid
