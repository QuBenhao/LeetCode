from bisect import bisect_left, bisect_right

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countFairPairs(*test_input)

    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        # # bisect
        # ans, n = 0, len(nums)
        # for i, num in enumerate(nums):
        #     l = bisect_left(nums, lower - num, i + 1, n)
        #     r = bisect_right(nums, upper - num, i + 1, n)
        #     ans += r - l
        # return ans

        # # two pointers
        ans = 0
        left = right = len(nums) - 1
        for i, num in enumerate(nums):
            left_bound, right_bound = lower - num, upper - num
            while right > i and nums[right] > right_bound:
                right -= 1
            while left > i and nums[left] >= left_bound:
                left -= 1
            ans += max(right, i) - max(left, i)
        return ans
