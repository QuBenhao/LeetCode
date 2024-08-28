import solution
from typing import *
from itertools import pairwise


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.satisfiesConditions(test_input)

    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        return all(a != b for a, b in pairwise(grid[0])) and all(row == grid[0] for row in grid)
