import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numIslands(test_input)

    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x, y):
            if not 0 <= x < m or not 0 <= y < n or grid[x][y] != '1':
                return
            grid[x][y] = '0'
            for dx, dy in directions:
                dfs(x + dx, y + dy)

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    ans += 1
        return ans
