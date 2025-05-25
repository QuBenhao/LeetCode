from collections import defaultdict
from functools import cache

from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxProfit(*test_input)

    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        graph = defaultdict(list)
        for _u, _v in hierarchy:
            graph[_u-1].append(_v-1)

        def merge(f1, f2):
            f = defaultdict(lambda: -inf)
            for b1 in f1:
                for b2 in f2:
                    if b1 + b2 <= budget and f[b1+b2] < f1[b1] + f2[b2]:
                        f[b1 + b2] = f1[b1] + f2[b2]
            return f

        @cache
        def dfs(u: int, pb: int):
            cost = present[u] // (pb + 1)
            f = defaultdict(lambda: -inf)
            f[0] = 0
            # 不买当前的最大收益
            for child in graph[u]:
                f = merge(f, dfs(child, 0))
            if cost <= budget:
                dp = defaultdict(lambda: -inf)
                dp[cost] = future[u] - cost
                # 买当前的最大收益
                for child in graph[u]:
                    dp = merge(dp, dfs(child, 1))
                for b in dp:
                    if f[b] < dp[b]:
                        f[b] = dp[b]
            return f

        return max(dfs(0, 0).values())
