import heapq
from collections import defaultdict, deque

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.avoidFlood(test_input)

    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        next_idxes = defaultdict(deque)
        to_be_cleared = set()
        for i, r in enumerate(rains):
            if r != 0:
                next_idxes[r].append(i)
        pq = []
        for i, r in enumerate(rains):
            if r == 0:
                if not pq:
                    ans[i] = 1
                else:
                    idx = heapq.heappop(pq)
                    ans[i] = rains[idx]
                    to_be_cleared.remove(rains[idx])
                continue
            if r in to_be_cleared:
                return []
            to_be_cleared.add(r)
            if next_idxes[r]:
                next_idx = next_idxes[r].popleft()
                if next_idx <= i and next_idxes[r]:
                    next_idx = next_idxes[r].popleft()
                if next_idx > i:
                    heapq.heappush(pq, next_idx)
        return ans
