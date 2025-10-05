import heapq

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.swimInWater(test_input)

    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 0
        pq = [(grid[0][0], 0, 0)]
        explored = [[False] * n for _ in range(n)]
        explored[0][0] = True
        while pq:
            t, x, y = heapq.heappop(pq)
            if x == n - 1 and y == n - 1:
                return t
            for dx, dy in DIRS:
                if 0 <= (nx := x + dx) < n and 0 <= (ny := y + dy) < n and not explored[nx][ny]:
                    heapq.heappush(pq, (max(grid[nx][ny], t), nx, ny))
                    explored[nx][ny] = True

        return max(grid[x][y] for x in range(n) for y in range(n))

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
