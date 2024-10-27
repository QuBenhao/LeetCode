import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findRedundantConnection(test_input)

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for x, y in edges:
            if find(x) == find(y):
                return [x, y]
            union(x, y)
        return []
