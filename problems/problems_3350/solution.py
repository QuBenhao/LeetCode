from itertools import pairwise
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxIncreasingSubarrays(test_input)

    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ans = 0
        last, cur = 0, 1
        for a, b in pairwise(nums + [-inf]):
            if b <= a:
                ans = max(ans, min(last, cur), cur // 2)
                last = cur
                cur = 1
                continue
            cur += 1
        return ans
