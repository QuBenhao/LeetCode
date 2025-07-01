from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findSubtreeSizes(*test_input)

    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        graph = defaultdict(list)
        ans = [1] * n
        for i, pa in enumerate(parent):
            if pa != -1:
                graph[pa].append(i)
        idx_map = defaultdict(lambda: -1)

        def dfs(node: int):
            before = idx_map[s[node]]
            if before != -1:
                parent[node] = before
            idx_map[s[node]] = node
            for child in graph[node]:
                dfs(child)
            idx_map[s[node]] = before
            if parent[node] != -1:
                ans[parent[node]] += ans[node]
            return None

        dfs(0)
        return ans
