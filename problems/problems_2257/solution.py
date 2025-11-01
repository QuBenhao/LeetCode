import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countUnguarded(*test_input)

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for x, y in guards:
            grid[x][y] = -1
        for x, y in walls:
            grid[x][y] = -1
        for x, y in guards:
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                while 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                    grid[nx][ny] = 1
                    nx, ny = nx + dx, ny + dy
        return sum(sum(g == 0 for g in row) for row in grid)

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
