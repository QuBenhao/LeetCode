import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxAreaOfIsland(test_input)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(x, y):
            if not (0 <= x < m and 0 <= y < n) or grid[x][y] == 0:
                return 0
            grid[x][y] = 0
            return sum(dfs(x + dx, y + dy) for dx, dy in directions) + 1

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans
