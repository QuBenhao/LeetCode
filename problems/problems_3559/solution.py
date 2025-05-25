from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.assignEdgeWeights(*test_input)

    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        def fast_pow(base, exp, _mod):
            result = 1
            base %= _mod
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % _mod
                base = (base * base) % _mod
                exp //= 2
            return result

        n = len(edges) + 1
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        depth = [0] * (n + 1)
        parent = [0] * (n + 1)
        def dfs(node: int, par: int):
            for neighbor in graph[node]:
                if neighbor != par:
                    depth[neighbor] = depth[node] + 1
                    parent[neighbor] = node
                    dfs(neighbor, node)
        dfs(1, 0)
        mod = 10**9 + 7
        ans = [0] * len(queries)
        def lca(a: int, b: int, parent: List[int]) -> int:
            while a != b:
                if depth[a] > depth[b]:
                    a = parent[a]
                else:
                    b = parent[b]
            return a

        for i, (a, b) in enumerate(queries):
            d = depth[a] + depth[b] - 2 * depth[lca(a, b, parent)] - 1
            ans[i] = fast_pow(2, d, mod) if d >= 0 else 0
        return ans

