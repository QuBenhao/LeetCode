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
        def dfs(l: int, r: int, remain: int) -> float:
            if remain == 1:
                return (prefix_sum[r] - prefix_sum[l - 1]) / (r - l + 1)
            ans = -inf
            for i in range(l, r + 2 - remain): # r - (i + 1) + 1 >= remain - 1  ==> i <= r + 1 - remain
                ans = max(ans, (prefix_sum[i] - prefix_sum[l - 1]) / (i - l + 1) + dfs(i + 1, r, remain - 1))
            return ans
        return dfs(1, len(nums), k)
