from collections import defaultdict
from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxWeight(*test_input)

    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        ans = -1

        graph = defaultdict(list)
        for a, b, v in edges:
            graph[a].append((b, v))

        @cache
        def dfs(i, l, s):
            if l == k:
                if s < t:
                    nonlocal ans
                    ans = max(ans, s)
                return
            for neigh, v in graph[i]:
                s += v
                dfs(neigh, l + 1, s)
                s -= v

        for i in range(n):
            dfs(i, 0, 0)
        return ans
