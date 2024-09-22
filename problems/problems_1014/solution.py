import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxScoreSightseeingPair(test_input)

    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = left = 0
        for i, val in enumerate(values):
            ans = max(ans, left + val - i)
            left = max(left, val + i)
        return ans
