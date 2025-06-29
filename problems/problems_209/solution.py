from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSubArrayLen(*test_input)

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 和862的区别在于没有负数，所以可以使用双指针来解决问题。
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
