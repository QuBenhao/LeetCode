import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countIslands(*test_input)

    def countIslands(self, grid: List[List[int]], k: int) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        ans = 0

        def dfs(x, y):
            cur = grid[x][y]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] != 0:
                    visited[nx][ny] = True
                    cur += dfs(nx, ny)
            return cur

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and not visited[i][j]:
                    visited[i][j] = True
                    if dfs(i, j) % k == 0:
                        ans += 1
        return ans

