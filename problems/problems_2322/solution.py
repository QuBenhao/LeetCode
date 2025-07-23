from itertools import combinations
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumScore(*test_input)

    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = [[] for _ in range(n)]
        node_in = [0] * n
        node_out = [0] * n
        xors = [0] * n
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        t = 0
        def dfs(pa, node):
            nonlocal t
            xors[node] = nums[node]
            node_in[node] = t
            t += 1
            for nei in graph[node]:
                if nei != pa:
                    xors[node] ^= dfs(node, nei)
            node_out[node] = t
            t += 1
            return xors[node]

        dfs(-1, 0)
        ans = inf
        for x, y in combinations(range(n-1), 2):
            # delete edge (x + 1, parent[x + 1]), (y + 1, parent[y + 1])
            x += 1
            y += 1
            if node_in[x] < node_in[y] <= node_out[x] or node_in[y] < node_in[x] <= node_out[y]:
                if node_in[x] < node_in[y] <= node_out[x]:
                    a, b, c = xors[y], xors[x] ^ xors[y], xors[0] ^ xors[x]
                else:
                    a, b, c = xors[x], xors[x] ^ xors[y], xors[0] ^ xors[y]
            else:
                a, b, c = xors[x], xors[y], xors[0] ^ xors[x] ^ xors[y]
            ans = min(ans, max(a, b, c) - min(a, b, c))
        return ans
