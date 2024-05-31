import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMissingAndRepeatedValues(test_input)

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        m = len(grid) ** 2
        d1 = sum(x for row in grid for x in row) - m * (m + 1) // 2
        d2 = sum(x * x for row in grid for x in row) - m * (m + 1) * (m * 2 + 1) // 6
        return [(d2 // d1 + d1) // 2, (d2 // d1 - d1) // 2]
