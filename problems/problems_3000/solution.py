import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.areaOfMaxDiagonal(test_input)

    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_length, max_area = 0, 0
        for a, b in dimensions:
            if (length := a * a + b * b) > max_length:
                max_length = length
                max_area = a * b
            elif length == max_length:
                max_area = max(max_area, a * b)
        return max_area
