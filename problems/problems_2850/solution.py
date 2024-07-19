import solution
from typing import *
from itertools import permutations


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumMoves(test_input)

    def minimumMoves(self, grid: List[List[int]]) -> int:
        source, target = [], []
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val > 1:
                    source.extend([(i, j)] * (val - 1))
                elif not val:
                    target.append((i, j))
        return min(
            sum(abs(x1 - x2) + abs(y1 - y2) for (x1, y1), (x2, y2) in zip(s, target))
            for s in permutations(source))
