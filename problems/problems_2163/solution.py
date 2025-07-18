import heapq
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumDifference(test_input)

    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        suffix = [0] * (2 * n + 1)
        pq = []
        for i in range(3 * n - 1, n - 1, -1):
            heapq.heappush(pq, nums[i])
            suffix[i - n] = suffix[i - n + 1] + nums[i]
            if len(pq) > n:
                suffix[i - n] -= heapq.heappop(pq)
        ans = inf
        pq.clear()
        prefix = 0
        for i in range(2 * n):
            heapq.heappush(pq, -nums[i])
            prefix += nums[i]
            if i == n - 1:
                ans = prefix - suffix[i - n + 1]
            if i >= n:
                prefix += heapq.heappop(pq)
                ans = min(ans, prefix - suffix[i - n + 1])
        return ans
