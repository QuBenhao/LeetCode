import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.merge(test_input)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for a, b in intervals:
            if a <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], b)
            else:
                ans.append([a, b])
        return ans
