import heapq

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxRemoval(*test_input)

    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n, m = len(nums), len(queries)
        queries.sort() # 按照左端点升序排序
        h = []
        diff = [0] * (n + 1)
        cur = j = 0
        for i, num in enumerate(nums):
            cur += diff[i]
            # 将所有区间左端点在 i 之前的区间加入堆
            while j < m and queries[j][0] <= i:
                heapq.heappush(h, -queries[j][1])
                j += 1
            # 从所有区间右端点在 i 之后的区间贪心取范围最大的
            while cur < num and h and -h[0] >= i:
                cur += 1
                diff[-heapq.heappop(h)+1] -= 1
            if cur < num:
                return -1
        return len(h)
