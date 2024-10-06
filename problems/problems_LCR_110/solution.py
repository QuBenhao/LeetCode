import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.allPathsSourceTarget(test_input)

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node):
            if node == len(graph) - 1:
                return [[node]]
            ans = []
            for nxt in graph[node]:
                for path in dfs(nxt):
                    ans.append([node] + path)
            return ans

        return dfs(0)
