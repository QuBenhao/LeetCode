from itertools import accumulate
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumScore(test_input)

    def maximumScore(self, nums: List[int]) -> int:
        pre = list(accumulate(nums))
        suf = inf
        ans = -inf
        for i in range(len(nums) - 1, -1, -1):
            ans = max(ans, pre[i] - suf)
            suf = min(suf, nums[i])
        return ans
