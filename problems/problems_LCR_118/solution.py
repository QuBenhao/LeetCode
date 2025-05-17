from collections import defaultdict, deque

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findRedundantConnection(test_input)

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = defaultdict(int)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        s = set()
        queue = deque([u for u in degree if degree[u] == 1])
        while queue:
            u = queue.popleft()
            for v in graph[u]:
                degree[v] -= 1
                if degree[v] == 1:
                    queue.append(v)
                s.add((u, v))
                s.add((v, u))
        for u, v in edges[::-1]:
            if (u, v) not in s:
                return [u, v]
        return []
