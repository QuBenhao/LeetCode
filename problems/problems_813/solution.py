from functools import cache
from itertools import accumulate
from math import inf
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestSumOfAverages(*test_input)

    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        prefix_sum = list(accumulate(nums, initial=0))

        @cache
        def dfs(r: int, remain: int) -> float:
            if remain == 1:
                return (prefix_sum[r] - prefix_sum[0]) / r
            ans = -inf
            for i in range(remain - 1, r):
                # [i, r) is the last segment
                ans = max(ans, (prefix_sum[r] - prefix_sum[i]) / (r - i) + dfs(i, remain - 1))
            return ans

        return dfs(len(nums), k)
