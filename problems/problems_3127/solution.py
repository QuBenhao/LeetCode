import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canMakeSquare(test_input)

    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        for i in range(1, m):
            for j in range(1, n):
                count = 0
                for x in range(i - 1, i + 1):
                    for y in range(j - 1, j + 1):
                        if grid[x][y] == 'B':
                            count += 1
                if count != 2:
                    return True
        return False
