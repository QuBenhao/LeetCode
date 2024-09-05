import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isBipartite(test_input)

    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(node, c):
            if color[node] != -1:
                return color[node] == c
            color[node] = c
            for nei in graph[node]:
                if not dfs(nei, c ^ 1):
                    return False
            return True

        n = len(graph)
        color = [-1] * n
        return all(color[i] != -1 or dfs(i, 0) for i in range(n))
