import heapq
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMaxPathScore(*test_input)

    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        graph = [[] for _ in range(n)]
        right = 0
        for u, v, c in edges:
            if online[u] and online[v]:
                graph[u].append((v, c))
                right = max(right, c)
        for i in range(n):
            graph[i].sort(key=lambda x: x[1], reverse=True)

        def helper(min_cost) -> bool:
            distance = [inf] * n
            pq = [(0, 0)]
            distance[0] = 0
            while pq:
                cost, node = heapq.heappop(pq)
                if node == n - 1:
                    return True
                if cost > distance[node]:
                    continue
                for neigh, ct in graph[node]:
                    if ct < min_cost:
                        break
                    new_cost = cost + ct
                    if new_cost > k or distance[neigh] < new_cost:
                        continue
                    distance[neigh] = new_cost
                    heapq.heappush(pq, (new_cost, neigh))
            return False

        left = -1
        while left < right:
            mid = (left + right + 1) // 2
            if helper(mid):
                left = mid
            else:
                right = mid - 1
        return left
