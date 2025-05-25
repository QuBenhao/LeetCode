from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.assignEdgeWeights(test_input)

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        def fast_pow(base, exp, _mod):
            result = 1
            base %= _mod
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % _mod
                base = (base * base) % _mod
                exp //= 2
            return result

        mod = 10**9 + 7
        n = len(edges) + 1
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        depth = [0] * (n + 1)
        def dfs(node, parent, d):
            depth[node] = d
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node, d + 1)
        dfs(1, -1, 0)
        max_depth = max(depth)
        return fast_pow(2, max_depth-1, mod)

