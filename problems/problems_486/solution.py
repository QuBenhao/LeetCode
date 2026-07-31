from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.predictTheWinner(test_input)

    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def minmax(l, r):
            sig = -1 if (r - l + 1) & 1 != n & 1 else 1
            if l == r:
                return nums[l] * sig
            ans = minmax(l + 1, r) + sig * nums[l]
            if sig < 0:
                sig = min(ans, minmax(l, r - 1) + sig * nums[r])
            else:
                sig = max(ans, minmax(l, r - 1) + sig * nums[r])
            return sig

        return minmax(0, n - 1) >= 0
