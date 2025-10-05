from collections import deque

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.pacificAtlantic(test_input)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        mark = [[0] * n for _ in range(m)]
        pacific_queue = deque()
        atlantic_queue = deque()
        for i in range(m):
            mark[i][0] |= 1
            pacific_queue.append((i, 0))
            mark[i][n - 1] |= 2
            atlantic_queue.append((i, n - 1))
        for j in range(n):
            mark[0][j] |= 1
            pacific_queue.append((0, j))
            mark[m - 1][j] |= 2
            atlantic_queue.append((m - 1, j))
        while pacific_queue:
            i, j = pacific_queue.popleft()
            for dx, dy in DIRS:
                if (0 <= (nx := i + dx) < m and 0 <= (ny := j + dy) < n and
                        heights[nx][ny] >= heights[i][j] and (mark[nx][ny] & 1 == 0)):
                    mark[nx][ny] |= 1
                    pacific_queue.append((nx, ny))
        while atlantic_queue:
            i, j = atlantic_queue.popleft()
            for dx, dy in DIRS:
                if (0 <= (nx := i + dx) < m and 0 <= (ny := j + dy) < n and
                        heights[nx][ny] >= heights[i][j] and (mark[nx][ny] & 2 == 0)):
                    mark[nx][ny] |= 2
                    atlantic_queue.append((nx, ny))
        ans = []
        for i in range(m):
            for j in range(n):
                if mark[i][j] & 3 == 3:
                    ans.append([i, j])
        return ans


DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
