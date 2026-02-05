from bisect import bisect_right
from collections import deque

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minRemoval(*test_input)

    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        window = deque()
        for num in nums:
            while window and window[0] * k < num:
                window.popleft()
            window.append(num)
            ans = max(ans, len(window))
        return len(nums) - ans

        # nums.sort()
        # n = len(nums)
        # ans = n - 1
        # r = 0
        # for i, num in enumerate(nums):
        #     r = bisect_right(nums, num * k, lo=r)
        #     ans = min(ans, n - (r - i))
        # return ans
