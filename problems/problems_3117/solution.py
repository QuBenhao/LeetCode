import solution
from typing import *
from functools import lru_cache
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumValueSum(*test_input)

    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        m, n = len(nums), len(andValues)
        @lru_cache(None)
        def dfs(i, j, av):
            if m - i < n - j:
                return inf
            if j == n:
                return 0 if i == m else inf
            av &= nums[i]
            res = dfs(i + 1, j, av)
            if av == andValues[j]:
                res = min(res, dfs(i + 1, j + 1, -1) + nums[i])
            return res

        ans = dfs(0, 0, -1)
        return -1 if ans == inf else ans
