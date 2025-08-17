from bisect import bisect_right, bisect_left

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.perfectPairs(test_input)

    def perfectPairs(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_abs = sorted(abs(num) for num in nums)
        ans = 0
        l = 0
        for r in range(1, n):
            while sorted_abs[l] * 2 < sorted_abs[r]:
                l += 1
            ans += r - l
        return ans
