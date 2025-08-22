from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumArea(test_input)

    def minimumArea(self, grid: List[List[int]]) -> int:
        left, right, top, bottom = inf, -1, inf, -1
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v:
                    left = min(left, j)
                    right = max(right, j)
                    top = min(top, i)
                    bottom = max(bottom, i)
        return (right - left + 1) * (bottom - top + 1)
