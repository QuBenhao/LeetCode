from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findTargetSumWays(*test_input)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i: int, cur_sum: int):
            if i == len(nums):
                return cur_sum == target
            ans = dfs(i + 1, cur_sum + nums[i])
            ans += dfs(i + 1, cur_sum - nums[i])
            return ans

        return dfs(0, 0)
