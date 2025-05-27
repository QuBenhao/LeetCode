from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxTargetNodes(*test_input)

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n, m = len(edges1) + 1, len(edges2) + 1

        graph = [defaultdict(list), defaultdict(list)]
        for u, v in edges1:
            graph[0][u].append(v)
            graph[0][v].append(u)
        for u, v in edges2:
            graph[1][u].append(v)
            graph[1][v].append(u)

        def dfs(_i, node, pa, _k):
            if _k < 0:
                return 0
            if _k == 0:
                return 1
            res = 1
            for nei in graph[_i][node]:
                if nei != pa:
                    res += dfs(_i, nei, node, _k - 1)
            return res

        mx = 0
        for i in range(m):
            mx = max(mx, dfs(1, i, -1, k-1))
        ans = [0] * n
        for i in range(n):
            ans[i] = dfs(0, i, -1, k) + mx
        return ans
