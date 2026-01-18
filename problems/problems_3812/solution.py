from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumFlips(*test_input)

    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, i))
            graph[v].append((u, i))

        ans = []
        def dfs(node, pa):
            cur = 0
            for child, idx in graph[node]:
                if child != pa:
                    rev = dfs(child, node)
                    if rev:
                        ans.append(idx)
                    cur ^= rev
            if start[node] != target[node]:
                cur ^= 1
            return cur

        if dfs(0, -1):
            return [-1]
        ans.sort()
        return ans
