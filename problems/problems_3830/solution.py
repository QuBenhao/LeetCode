from itertools import pairwise
from linecache import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestAlternating(test_input)

    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        up, down = [1] * n, [1] * n
        ans = 1
        for i, (a, b) in enumerate(pairwise(nums), start=1):
            if a == b:
                continue
            if a > b:
                down[i] = up[i - 1] + 1
            else:
                up[i] = down[i - 1] + 1
            ans = max(ans, up[i], down[i])
        up_rev, down_rev = [1] * n, [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] == nums[i + 1]:
                continue
            if nums[i] > nums[i + 1]:
                down_rev[i] = up_rev[i + 1] + 1
            else:
                up_rev[i] = down_rev[i + 1] + 1
        for i in range(1, n - 1):
            if nums[i - 1] == nums[i + 1]:
                continue
            if nums[i - 1] < nums[i + 1]:
                ans = max(ans, down[i - 1] + down_rev[i + 1])
            else:
                ans = max(ans, up[i - 1] + up_rev[i + 1])
        return ans
