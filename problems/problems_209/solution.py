from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSubArrayLen(*test_input)

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Unlike problem 862, there are no negative numbers, so two pointers can solve this problem.
        left = 0
        ans = inf
        prefix_sum = 0
        for right, num in enumerate(nums):
            prefix_sum += num
            while prefix_sum >= target:
                ans = min(ans, right - left + 1)
                prefix_sum -= nums[left]
                left += 1
        return ans if ans != inf else 0
