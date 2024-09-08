from collections import deque

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numSubarrayProductLessThanK(*test_input)

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        left = right = 0
        cur = 1
        while right < len(nums):
            cur *= nums[right]
            while cur >= k and left <= right:
                cur //= nums[left]
                left += 1
            ans += right - left + 1
            right += 1
        return ans
