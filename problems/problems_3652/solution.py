from itertools import accumulate

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxProfit(*test_input)

    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        origin_pre_sum = [0] *(n + 1)
        pre_sum = [0] * (n + 1)
        for i, (p, s) in enumerate(zip(prices, strategy)):
            pre_sum[i + 1] = pre_sum[i] + p * s
            origin_pre_sum[i + 1] = origin_pre_sum[i] + p
        ans = pre_sum[-1]
        for i in range(n - k + 1):
            cur = pre_sum[i] + pre_sum[-1] - pre_sum[i + k]
            cur += origin_pre_sum[i + k] - origin_pre_sum[i + k // 2]
            ans = max(ans, cur)
        return ans
