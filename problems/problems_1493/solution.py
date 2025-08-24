import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestSubarray(test_input)

    def longestSubarray(self, nums: List[int]) -> int:
        if all(num == 1 for num in nums):
            return len(nums) - 1
        ans = last = cur = 0
        for num in nums + [0]:
            if num == 1:
                cur += 1
            else:
                ans = max(ans, last + cur)
                last, cur = cur, 0
        return ans
