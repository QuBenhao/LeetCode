from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findTargetSumWays(*test_input)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums) - abs(target)
        if s < 0 or s % 2 != 0:
            return 0

        s //= 2
        n = len(nums)

        @cache
        def dfs(i, c):
            if i == n:
                return c == 0
            if c < 0:
                return dfs(i+1, c)
            return dfs(i+1, c) + dfs(i+1, c-nums[i])

        return dfs(0, s)
