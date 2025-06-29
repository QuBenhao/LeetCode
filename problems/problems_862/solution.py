from collections import deque

from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.shortestSubarray(*test_input)

    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q = deque([(0, -1)])  # (prefix_sum, index)
        prefix_sum = 0
        ans = inf
        for i, num in enumerate(nums):
            prefix_sum += num
            while q and prefix_sum - q[0][0] >= k:
                ans = min(ans, i - q.popleft()[1])
            while q and prefix_sum <= q[-1][0]:
                q.pop()
            q.append((prefix_sum, i))
        return ans if ans != inf else -1
