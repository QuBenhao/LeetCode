from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxScore(*test_input)

    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        @cache
        def dfs(city, day):
            if day == k:
                return 0
            max_score = 0
            for nc in range(n):
                if nc == city:
                    max_score = max(max_score, dfs(nc, day + 1) + stayScore[day][city])
                else:
                    max_score = max(max_score, dfs(nc, day + 1) + travelScore[city][nc])
            return max_score

        return max(dfs(i, 0) for i in range(n))
