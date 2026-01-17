from itertools import combinations

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestSquareArea(*test_input)

    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        ans = 0
        for ((x0, y0), (x1, y1)), ((x2, y2), (x3, y3)) in combinations(zip(bottomLeft, topRight), 2):
            if (a := max(x0, x2)) < (c := min(x1, x3)) and (b := max(y0, y2)) < (d := min(y1, y3)):
                ans = max(ans, min(d - b, c - a) ** 2)
        return ans
