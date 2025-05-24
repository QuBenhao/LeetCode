from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.combinationSum4(*test_input)

    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(t):
            if t == 0:
                return 1
            return sum(dfs(t-i) for i in nums if i <= t)
        return dfs(target)
