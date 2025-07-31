from bisect import bisect_left

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findRightInterval(test_input)

    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        d = {l: i for i, (l, _) in enumerate(intervals)}
        intervals.sort()
        n = len(intervals)
        ans = [-1] * n
        for l, r in intervals:
            idx = bisect_left(intervals, r, key=lambda x: x[0])
            if idx < n:
                ans[d[l]] = d[intervals[idx][0]]
        return ans
