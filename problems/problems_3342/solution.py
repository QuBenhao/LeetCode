import heapq
from math import inf
from typing import *

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minTimeToReach(test_input)

    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pq = [(0, 0, 0)] # (time, x, y)
        m, n = len(moveTime), len(moveTime[0])
        explored = [[inf] * n for _ in range(m)]
        explored[0][0] = 0
        while pq:
            time, x, y = heapq.heappop(pq)
            if x == m - 1 and y == n - 1:
                return time
            if time > explored[x][y]:
                continue
            for dx, dy in directions:
                if 0 <= (nx := x + dx) < m and 0 <= (ny := y + dy) < n:
                    nt = max(time, moveTime[nx][ny]) + (x+y)%2 + 1
                    if explored[nx][ny] > nt:
                        explored[nx][ny] = nt
                        heapq.heappush(pq, (nt, nx, ny))
        return -1
