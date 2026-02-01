from bisect import bisect_right
from math import ceil

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumK(test_input)

    def minimumK(self, nums: List[int]) -> int:
        def check(k):
            idx = 0
            count = 0
            while idx < n:
                cur = ceil(nums[idx] / k)
                nxt = bisect_right(nums, cur * k, lo=idx)
                count += cur * (nxt - idx)
                idx = nxt
            return count <= k * k

        n = len(nums)
        nums.sort()
        left, right = 1, 100000
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
