from collections import deque

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findSafeWalk(*test_input)

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        """
        Use BFS to find the path from (0,0) to (m-1,n-1) that consumes the least health.

        Use max_health[x][y] to record the maximum remaining health on reaching this cell.
        If the same cell is reached with more health, explore it again.
        """
        m, n = len(grid), len(grid[0])

        # Health consumed at the starting cell
        start_health = health - grid[0][0]
        if start_health <= 0:
            return False

        # max_health[x][y] = maximum remaining health on reaching (x,y)
        max_health = [[0] * n for _ in range(m)]
        max_health[0][0] = start_health

        # BFS queue: (x, y, remaining_health)
        queue = deque([(0, 0, start_health)])

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            x, y, h = queue.popleft()

            # Reached the destination
            if x == m - 1 and y == n - 1:
                return h >= 1

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    # Compute the remaining health on reaching the new cell
                    new_h = h - grid[nx][ny]
                    if new_h >= 1 and new_h > max_health[nx][ny]:
                        # Reached with more health, so it is worth exploring again
                        max_health[nx][ny] = new_h
                        queue.append((nx, ny, new_h))

        return False
