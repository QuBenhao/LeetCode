from collections import defaultdict
from heapq import heappush, heappop
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minTime(*test_input)

    def minTime(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, s, e in edges:
            graph[u].append((v, s, e))
        pq = [(0, 0)] # (time, node)
        dist = [inf] * n
        dist[0] = 0
        while pq:
            t, node = heappop(pq)
            if node == n - 1:
                return t
            if t > dist[node]:
                continue
            for v, s, e in graph[node]:
                if t <= e:
                    nt = max(t, s) + 1
                    if nt < dist[v]:
                        dist[v] = nt
                        heappush(pq, (nt, v))
        return -1
