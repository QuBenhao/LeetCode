import solution
from typing import *
from functools import lru_cache
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.mincostTickets(*test_input)

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        @lru_cache(None)
        def dfs(i):
            if i >= n:
                return 0
            ans = inf
            ans = min(ans, dfs(i+1) + costs[0])
            j = i
            while j < len(days) and days[j] < days[i] + 7:
                j += 1
            ans = min(ans, dfs(j) + costs[1])
            while j < len(days) and days[j] < days[i] + 30:
                j += 1
            ans = min(ans, dfs(j) + costs[2])
            return ans

        return dfs(0)
