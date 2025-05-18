from collections import defaultdict
from heapq import heappush, heappop
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minMoves(test_input)

    def minMoves(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0])
        if matrix[m - 1][n - 1] == '#':
            return -1
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = [(0, 0, 0)]  # move, -x, -y
        distance = defaultdict(lambda: inf)
        portals = defaultdict(list)
        distance[(0, 0)] = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != '.' and matrix[i][j] != '#':
                    portals[matrix[i][j]].append((i, j))
        while q:
            move, x, y = heappop(q)
            x, y = -x, -y
            if (x, y) == (m - 1, n - 1):
                return move
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != '#':
                    if (nx, ny) not in distance or distance[(nx, ny)] > move + 1:
                        distance[(nx, ny)] = move + 1
                        heappush(q, (move + 1, -nx, -ny))
            if matrix[x][y] == '.' or matrix[x][y] == '#':
                continue
            if matrix[x][y] not in portals:
                continue
            for other in portals[matrix[x][y]]:
                nx, ny = other
                if distance[(0, nx, ny)] <= move:
                    continue
                if (nx, ny) not in distance or distance[(nx, ny)] > move:
                    distance[(nx, ny)] = move
                    heappush(q, (move, -nx, -ny))
            del portals[matrix[x][y]]
        return -1
