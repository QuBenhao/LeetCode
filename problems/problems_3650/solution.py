from collections import defaultdict
from heapq import heappop, heappush
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCost(*test_input)

    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(lambda: defaultdict(lambda: inf))
        for u, v, w in edges:
            graph[u][v] = min(graph[u][v], w)
            graph[v][u] = min(graph[v][u], w * 2)
        dist = [inf] * n
        dist[0] = 0
        pq = [(0, 0)]
        while pq:
            d, u = heappop(pq)
            if u == n - 1:
                return d
            if d > dist[u]:
                continue
            for v, w in graph[u].items():
                if (nd := d + w) < dist[v]:
                    dist[v] = nd
                    heappush(pq, (nd, v))
        return -1
