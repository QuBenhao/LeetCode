from heapq import heappop, heappush

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.shortestPath(*test_input)

    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # 状态: (节点 u, 结尾连续相同标签长度 r), 1 <= r <= k
        # 边权为正, 在扩展后的状态图上跑 Dijkstra
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))

        inf = float("inf")
        dist = [[inf] * (k + 1) for _ in range(n)]
        dist[0][1] = 0
        heap = [(0, 0, 1)]
        while heap:
            d, u, r = heappop(heap)
            if d > dist[u][r]:
                continue
            if u == n - 1:
                return d
            lu = labels[u]
            for v, w in graph[u]:
                nr = r + 1 if labels[v] == lu else 1
                if nr <= k and d + w < dist[v][nr]:
                    dist[v][nr] = d + w
                    heappush(heap, (d + w, v, nr))
        return -1
