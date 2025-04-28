import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countSubarrays(*test_input)

    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        n = len(nums)
        ans = left = cur = 0
        for right, num in enumerate(nums):
            cur += num == mx
            while cur >= k:
                ans += n - right
                cur -= nums[left] == mx
                left += 1
        return ans
