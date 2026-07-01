from collections import deque

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findSafeWalk(*test_input)

    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        """
        BFS找从(0,0)到(m-1,n-1)消耗最少生命值的路径。

        使用 max_health[x][y] 记录到达该格子时的最大剩余生命值。
        如果以更大的生命值到达同一格子，需要重新探索。
        """
        m, n = len(grid), len(grid[0])

        # 起点消耗
        start_health = health - grid[0][0]
        if start_health <= 0:
            return False

        # max_health[x][y] = 到达(x,y)时的最大剩余生命值
        max_health = [[0] * n for _ in range(m)]
        max_health[0][0] = start_health

        # BFS队列: (x, y, remaining_health)
        queue = deque([(0, 0, start_health)])

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            x, y, h = queue.popleft()

            # 到达终点
            if x == m - 1 and y == n - 1:
                return h >= 1

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    # 计算到达新格子的剩余生命值
                    new_h = h - grid[nx][ny]
                    if new_h >= 1 and new_h > max_health[nx][ny]:
                        # 以更大的生命值到达，值得重新探索
                        max_health[nx][ny] = new_h
                        queue.append((nx, ny, new_h))

        return False
