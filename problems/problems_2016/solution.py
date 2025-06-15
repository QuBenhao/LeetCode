from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumDifference(test_input)

    def maximumDifference(self, nums: List[int]) -> int:
        mn = inf
        ans = -inf
        for num in nums:
            if num > mn:
                ans = max(ans, num - mn)
            mn = min(mn, num)
        return ans if ans != -inf else -1
