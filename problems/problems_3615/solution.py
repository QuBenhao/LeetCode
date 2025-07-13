from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxLen(*test_input)

    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        graph: List[List[int]] = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        @cache
        def dfs(i: int, j: int, explored: int) -> int:
            ans = 0
            for nxt in graph[i]:
                if (explored >> nxt) & 1:
                    continue
                for nxt_j in graph[j]:
                    if nxt_j == nxt or label[nxt] != label[nxt_j] or (explored >> nxt_j) & 1:
                        continue
                    if nxt > nxt_j:
                        nxt, nxt_j = nxt_j, nxt
                    ans = max(ans, dfs(nxt, nxt_j, explored | 1 << nxt | 1 << nxt_j) + 2)
            return ans

        ans = 1
        for i in range(n):
            ans = max(ans, dfs(i, i, 1 << i) + 1)
            for j in graph[i]:
                if label[i] != label[j] or i > j:
                    continue
                ans = max(ans, dfs(i, j, 1 << i | 1 << j) + 2)
        return ans

