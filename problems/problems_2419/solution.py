from typing import *

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestSubarray(test_input)

    def longestSubarray(self, nums: List[int]) -> int:
        ans, mx, cur = 0, 0, 0
        for num in nums:
            if num > mx:
                ans, mx, cur = 1, num, 1
            elif num == mx:
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 0
        return ans
