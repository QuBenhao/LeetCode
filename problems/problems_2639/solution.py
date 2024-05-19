import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findColumnWidth(test_input)

    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [len(str(max(max(col), -10 * min(col)))) for col in zip(*grid)]
