import heapq

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxRemoval(*test_input)

    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)
        queries.sort() # Sort by left endpoint in ascending order
        h = []
        diff = [0] * (n + 1)
        cur = j = 0
        for i, num in enumerate(nums):
            cur += diff[i]
            # Add all intervals whose left endpoint is at or before i to the heap
            while j < m and queries[j][0] <= i:
                heapq.heappush(h, -queries[j][1])
                j += 1
            # Among intervals whose right endpoint is at or after i, greedily choose the one that extends farthest
            while cur < num and h and -h[0] >= i:
                cur += 1
                diff[-heapq.heappop(h)+1] -= 1
            if cur < num:
                return -1
        return len(h)
