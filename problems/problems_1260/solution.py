import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.shiftGrid(*test_input)

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k %= m * n
        if k == 0:
            return grid
        ans = [[0] * n for _ in range(m)]
        x, y = k // n, k % n
        for i in range(m):
            for j in range(n):
                ans[x][y] = grid[i][j]
                y += 1
                if y == n:
                    y = 0
                    x += 1
                if x == m:
                    x = 0
        return ans
