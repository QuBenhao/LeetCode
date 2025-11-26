from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxSubarraySum(*test_input)

    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        min_s = [inf] * k
        min_s[-1] = s = 0
        ans = -inf
        for j, num in enumerate(nums):
            s += num
            i = j % k
            ans = max(ans, s - min_s[i])
            min_s[i] = min(min_s[i], s)
        return ans
