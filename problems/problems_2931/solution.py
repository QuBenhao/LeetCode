import solution
from typing import *
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxSpending(test_input)

    def maxSpending(self, values: List[List[int]]) -> int:
        m, n = len(values), len(values[0])
        pq = []
        for i in range(m):
            heapq.heappush(pq, (values[i][-1], i, n - 1))
        ans, d = 0, 1
        while pq:
            val, i, j = heapq.heappop(pq)
            ans += d * val
            d += 1
            if j == 0:
                continue
            heapq.heappush(pq, (values[i][j - 1], i, j - 1))
        return ans
