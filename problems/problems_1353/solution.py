import heapq

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxEvents(test_input)

    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        cur_day = events[0][0]
        ans = 0
        idx = 0
        pq = []
        n = len(events)
        while idx < n or pq:
            while idx < n and events[idx][0] <= cur_day:
                heapq.heappush(pq, events[idx][1])
                idx += 1
            if pq:
                heapq.heappop(pq)
                ans += 1
                cur_day += 1
                while pq and pq[0] < cur_day:
                    heapq.heappop(pq)
            elif idx < n:
                cur_day = max(cur_day, events[idx][0])
        return ans
