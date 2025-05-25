import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxProfit(*test_input)

    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        g = [[] for _ in range(n)]
        for a, b in hierarchy:
            g[a - 1].append(b - 1)
        inf = 10 ** 9

        def merge(f1, f2):
            f = collections.defaultdict(lambda: -inf)
            for b1 in f1:
                for b2 in f2:
                    if b1 + b2 <= budget and f[b1 + b2] < f1[b1] + f2[b2]:
                        f[b1 + b2] = f1[b1] + f2[b2]
            return f

        @functools.lru_cache(None)
        def dfs(u, ok):
            if ok:
                cost_u = present[u] // 2
            else:
                cost_u = present[u]

            f1 = collections.defaultdict(lambda: -inf, {0: 0})
            for v in g[u]:
                f1 = merge(f1, dfs(v, 0))

            if cost_u <= budget:
                p = future[u] - cost_u
                f2 = collections.defaultdict(lambda: -inf, {cost_u: p})
                for v in g[u]:
                    f2 = merge(f2, dfs(v, 1))
                
                for b in f2:
                    if f1[b] < f2[b]:
                        f1[b] = f2[b]
            return f1

        return max(dfs(0, 0).values())
