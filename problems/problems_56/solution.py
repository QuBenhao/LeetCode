import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.merge(test_input)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        for left, right in intervals:
            if ans and ans[-1][1] >= left:
                ans[-1][1] = max(ans[-1][1], right)
            else:
                ans.append([left, right])
        return ans
