from bisect import bisect_left

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxCapacity(*test_input)

    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        arr = [(cost, cap) for cost, cap in zip(costs, capacity) if cost < budget]
        arr.sort()
        pre_max = [0] * (len(arr) + 1)
        ans = 0
        for i, (cost, cap) in enumerate(arr):
            # i作为第二台的最优取值
            j = bisect_left(range(i), budget - cost, key=lambda x: arr[x][0])
            ans = max(ans, pre_max[j] + cap) # 前缀j这里相当于取arr中上式j的前一个
            pre_max[i + 1] = max(pre_max[i], cap)
        return ans
