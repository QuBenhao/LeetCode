import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.removeCoveredIntervals(test_input)

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        right = ans = 0
        for _, r in intervals:
            if r > right:
                ans += 1
                right = r
        return ans

