import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.calcEquation(*test_input)

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for i, (a, b) in enumerate(equations):
            if a not in graph:
                graph[a] = {}
            if b not in graph:
                graph[b] = {}
            graph[a][b] = values[i]
            graph[b][a] = 1 / values[i]

        def dfs(a, b, visited):
            if a not in graph or b not in graph:
                return -1.0
            if a == b:
                return 1.0
            visited.add(a)
            for c in graph[a]:
                if c in visited:
                    continue
                visited.add(c)
                res = dfs(c, b, visited)
                if res != -1.0:
                    return graph[a][c] * res
            return -1.0

        ans = []
        for a, b in queries:
            ans.append(dfs(a, b, set()))
        return ans

