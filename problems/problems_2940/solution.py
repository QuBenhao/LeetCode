import solution
from typing import *
from heapq import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.leftmostBuildingQueries(*test_input)

    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        qs: List[List[Tuple[int, int]]] = [[] for _ in heights]
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                ans[i] = b
            else:
                qs[b].append((heights[a], i))

        h = []
        for i, x in enumerate(heights):
            while h and h[0][0] < x:
                ans[heappop(h)[1]] = i
            for q in qs[i]:
                heappush(h, q)
        return ans
