from typing import *

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countSubarrays(*test_input)

    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = cur = left = 0
        for right, num in enumerate(nums):
            cur += num
            while cur * (right - left + 1) >= k:
                cur -= nums[left]
                left += 1
            ans += right - left + 1
        return ans
