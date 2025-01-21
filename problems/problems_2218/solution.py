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
        #         pile[i] += pile[i - 1]  # 提前计算 pile 的前缀和
        #     sum_n = min(sum_n + n, k)
        #     for j in range(sum_n, 0, -1):  # 优化：j 从前 i 个栈的大小之和开始枚举
        #         # w 从 0 开始，物品体积为 w+1
        #         f[j] = max(f[j], max(f[j - w - 1] + pile[w] for w in range(min(n, j))))
        # return f[k]
