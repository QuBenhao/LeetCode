from functools import lru_cache
from itertools import accumulate

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxValueOfCoins(*test_input)

    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if j == 0:
                return 0
            if i == len(piles):
                return 0
            ans = dfs(i + 1, j)
            for w, v in enumerate(accumulate(piles[i][:j]), 1):
                ans = max(ans, dfs(i + 1, j - w) + v)
            return ans

        return dfs(0, k)

        # f = [0] * (k + 1)
        # sum_n = 0
        # for pile in piles:
        #     n = len(pile)
        #     for i in range(1, n):
        #         pile[i] += pile[i - 1]  # Precompute the prefix sums of pile
        #     sum_n = min(sum_n + n, k)
        #     for j in range(sum_n, 0, -1):  # Optimization: start j at the total size of the first i stacks
        #         # w starts at 0, so the item weight is w+1
        #         f[j] = max(f[j], max(f[j - w - 1] + pile[w] for w in range(min(n, j))))
        # return f[k]
