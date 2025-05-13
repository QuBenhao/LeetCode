from itertools import pairwise
from typing import *

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMinDifference(test_input)

    def findMinDifference(self, timePoints: List[str]) -> int:
        times = sorted(list(map(lambda x: int(x[:2]) * 60 + int(x[3:]), timePoints)))
        ans = times[0] + 1440 - times[-1]
        for a, b in pairwise(times):
            ans = min(ans, b - a)
        return ans
