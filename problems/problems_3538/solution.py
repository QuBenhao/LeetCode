from functools import cache
from itertools import accumulate
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minTravelTime(*test_input)

    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        time_prefix_sum = list(accumulate(time, initial=0))

        @cache
        def dfs(_k: int, i: int, pre: int) -> int:
            if i == n - 1:
                return inf if _k else 0
            t = time_prefix_sum[i+1] - time_prefix_sum[pre]
            # i到nxt合并以后，计算的时间是time[i]，time[i]由上一次割点的产生决定(即pre)，从pre到i的前缀和是s[i+1]-s[pre]
            return min(dfs(_k- (nxt-i-1), nxt, i + 1) + t * (position[nxt] - position[i]) for nxt in range(i + 1, min(n, i + _k + 2)))

        dfs.cache_clear()
        return dfs(k, 0, 0)
