import solution
from typing import *
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.waysToReachStair(test_input)

    def waysToReachStair(self, k: int) -> int:
        @lru_cache(None)
        def dfs(cur: int, jump: int) -> int:
            ans = 0
            if abs(cur) == k:
                ans += 1
            elif cur > k + 1 or cur < -k:
                return 0
            if cur > 0:
                ans += dfs(-cur + 1, jump)
            ans += dfs(abs(cur) + (1 << jump), jump + 1)
            return ans

        return dfs(1, 0)
