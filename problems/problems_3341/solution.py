import heapq
from typing import *

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minTimeToReach(test_input)

    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(moveTime), len(moveTime[0])
        explored = set()
        queue = [(0, 0, 0)]  # (time, x, y)
        while queue:
            t, x, y = heapq.heappop(queue)
            if (x, y) == (m - 1, n - 1):
                return t
            if (x, y) in explored:
                continue
            explored.add((x, y))
            for dx, dy in directions:
                if 0 <= (nx := x + dx) < m and 0 <= (ny := y + dy) < n and (nx, ny) not in explored:
                    heapq.heappush(queue, (max(t, moveTime[nx][ny]) + 1, nx, ny))
        return -1
