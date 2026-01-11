from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minTimeToVisitAllPoints(test_input)

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def move(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return max(abs(x2 - x1), abs(y2 - y1))

        return sum(move(a, b) for a, b in pairwise(points))
