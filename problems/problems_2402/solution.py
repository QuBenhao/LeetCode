import heapq

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.mostBooked(*test_input)

    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        counts = [0] * n
        rooms = [i for i in range(n)]
        heapq.heapify(rooms)
        next_release = []
        for start, end in meetings:
            while next_release and next_release[0][0] <= start:
                _, idx = heapq.heappop(next_release)
                heapq.heappush(rooms, idx)
            if rooms:
                idx = heapq.heappop(rooms)
                counts[idx] += 1
                heapq.heappush(next_release, (end, idx))
            else:
                t, idx = heapq.heappop(next_release)
                counts[idx] += 1
                heapq.heappush(next_release, (t + end - start, idx))
        ans, ans_c = 0, 0
        for i, c in enumerate(counts):
            if c > ans_c:
                ans, ans_c = i, c
        return ans
