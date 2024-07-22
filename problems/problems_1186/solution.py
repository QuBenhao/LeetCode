import solution
from typing import *
from math import inf

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumSum(test_input)

    def maximumSum(self, arr: List[int]) -> int:
        ans = dp1 = dp2 = -inf
        for num in arr:
            dp2 = max(dp1, dp2 + num)
            dp1 = max(dp1 + num, num)
            ans = max(ans, dp1, dp2)
        return ans
