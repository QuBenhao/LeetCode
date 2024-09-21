import solution
from typing import *
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.edgeScore(test_input)

    def edgeScore(self, edges: List[int]) -> int:
        ans, counter = -1, defaultdict(int)
        for i, edge in enumerate(edges):
            counter[edge] += i
            if counter[edge] > counter[ans]:
                ans = edge
            elif counter[edge] == counter[ans]:
                ans = min(ans, edge)
        return ans
