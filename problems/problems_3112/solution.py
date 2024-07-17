import solution
from typing import *
from collections import defaultdict
from heapq import heappush, heappop


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumTime(*test_input)

    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dis = [-1] * n
        dis[0] = 0
        pq = [(0, 0)]
        while pq:
            d, u = heappop(pq)
            if dis[u] < d:
                continue
            for v, w in graph[u]:
                new_d = d + w
                if new_d < disappear[v] and (dis[v] == -1 or new_d < dis[v]):
                    dis[v] = new_d
                    heappush(pq, (new_d, v))
        return dis
