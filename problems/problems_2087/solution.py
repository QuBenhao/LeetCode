import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCost(*test_input)

    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        x0, y0 = startPos
        x1, y1 = homePos
        if x0 > x1:
            x0, x1 = x1 - 1, x0 - 1
        if y0 > y1:
            y0, y1 = y1 - 1, y0 - 1
        return sum(rowCosts[x0+1:x1+1]) + sum(colCosts[y0+1:y1+1])
