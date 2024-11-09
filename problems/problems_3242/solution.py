import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = NeighborSum(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.idx_map = {}
        n = len(grid)
        for i in range(n):
            for j in range(n):
                self.idx_map[grid[i][j]] = (i, j)

    def adjacentSum(self, value: int) -> int:
        x, y = self.idx_map[value]
        n = len(self.grid)
        ans = 0
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                ans += self.grid[nx][ny]
        return ans

    def diagonalSum(self, value: int) -> int:
        x, y = self.idx_map[value]
        n = len(self.grid)
        ans = 0
        for dx, dy in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                ans += self.grid[nx][ny]
        return ans

