import solution
from typing import *
from collections import defaultdict
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxPointsInsideSquare(*test_input)

    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        max_d = inf
        explore = defaultdict(lambda: (inf, inf))
        for (x, y), c in zip(points, s):
            cur = max(abs(x), abs(y))
            if c in explore:
                v = sorted([cur, explore[c][0], explore[c][1]])
                explore[c] = (v[0], v[1])
                max_d = min(max_d, v[1] - 1)
            else:
                explore[c] = (cur, inf)
        if max_d == inf:
            return len(s)
        return sum(1 for x, y in points if abs(x) <= max_d and abs(y) <= max_d)
