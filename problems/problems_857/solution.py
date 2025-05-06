import heapq
from typing import *
from math import inf

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.mincostToHireWorkers(*test_input)

    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # 性价比=w/q
        ans, total, pq = inf, 0, []
        for q, w in sorted(zip(quality, wage), key=lambda x: (x[1] / x[0])):
            total += q
            heapq.heappush(pq, -q)
            if len(pq) > k:
                total += heapq.heappop(pq)
            if len(pq) == k:
                ans = min(ans, total * w / q)
        return ans
