import solution
from typing import *
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfArrays(*test_input)

    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        minimum, maximum = 0, 0
        cur = 0
        for d in differences:
            cur += d
            minimum = min(minimum, cur)
            maximum = max(maximum, cur)
        # start + minimum >= lower
        # start + maximum <= upper
        # lower - minimum <= start <= upper - maximum
        return max(0, (upper - maximum) - (lower - minimum) + 1)
