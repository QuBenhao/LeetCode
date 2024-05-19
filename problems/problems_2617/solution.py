import solution
from typing import *
import heapq
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumVisitedCells(test_input)

    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n, cost = len(grid), len(grid[0]), inf
        col_hs = [[] for _ in range(n)]
        for i, row in enumerate(grid):
            row_h = []
            for j, v in enumerate(row):
                while row_h and row_h[0][1] < j:
                    heapq.heappop(row_h)
                while col_hs[j] and col_hs[j][0][1] < i:
                    heapq.heappop(col_hs[j])
                cost = inf if i > 0 or j > 0 else 1
                if row_h:
                    cost = min(cost, row_h[0][0] + 1)
                if col_hs[j]:
                    cost = min(cost, col_hs[j][0][0] + 1)
                if v and cost != inf:
                    heapq.heappush(row_h, (cost, j + v))
                    heapq.heappush(col_hs[j], (cost, i + v))
        return cost if cost != inf else -1
