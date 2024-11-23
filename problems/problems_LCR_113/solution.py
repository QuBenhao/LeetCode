import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findOrder(*test_input)

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        graph = defaultdict(list)
        indeg = [0] * numCourses
        for p in prerequisites:
            graph[p[1]].append(p[0])
            indeg[p[0]] += 1
        stack = [i for i in range(numCourses) if not indeg[i]]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(node)
            for nei in graph[node]:
                indeg[nei] -= 1
                if not indeg[nei]:
                    stack.append(nei)
        return ans if len(ans) == numCourses else []

