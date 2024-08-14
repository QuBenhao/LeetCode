import solution
from typing import *
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxScore(test_input)

    def maxScore(self, grid: List[List[int]]) -> int:
        # ans = (b - a) + (c - b) + (d -c) + ... = last - first
        m, n = len(grid), len(grid[0])
        ans = -inf
        cols_min = [inf] * n
        for row in grid:
            pre_min = inf
            for j, v in enumerate(row):
                ans = max(ans, v - min(pre_min, cols_min[j]))
                cols_min[j] = min(cols_min[j], v)
                pre_min = min(pre_min, cols_min[j])
        return ans
