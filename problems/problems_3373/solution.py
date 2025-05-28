from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxTargetNodes(*test_input)

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)
        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)
        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        def dfs(node, pa, d, graph):
            res = int(d == 0)
            for neigh in graph[node]:
                if neigh != pa:
                    res += dfs(neigh, node, d^1, graph)
            return res

        mx = 0
        m, n = len(graph1), len(graph2)
        a = dfs(0, -1, 1, graph2)
        mx = max(mx, a, n - a)
        ans = [0] * m
        ans[0] = dfs(0, -1, 0, graph1)

        def dfs2(node, pa, graph):
            for neigh in graph[node]:
                if neigh != pa:
                    ans[neigh] = m - ans[node]
                    dfs2(neigh, node, graph)
        dfs2(0, -1, graph1)
        return [i+mx for i in ans]
