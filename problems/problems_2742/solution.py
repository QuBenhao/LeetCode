import solution
from typing import *
from functools import lru_cache
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.paintWalls(*test_input)

    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if j > i:
                return 0
            if i < 0:
                return inf
            return min(dfs(i - 1, j + time[i]) + cost[i], dfs(i - 1, j - 1))

        return dfs(len(cost) - 1, 0)
