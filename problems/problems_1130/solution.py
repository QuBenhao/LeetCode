from functools import cache
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.mctFromLeafValues(test_input)

    def mctFromLeafValues(self, arr: List[int]) -> int:
        # @cache
        # def range_max(i, j):
        #     if i == j:
        #         return arr[i]
        #     return max(arr[i], range_max(i + 1, j))
        #
        # @cache
        # def dfs(i, j):
        #     if j - i == 1:
        #         return arr[i] * arr[j], range_max(i, j)
        #     if j == i:
        #         return 0, arr[i]
        #     res = inf
        #     for k in range(i, j):
        #         left_cost, left_max = dfs(i, k)
        #         right_cost, right_max = dfs(k+1, j)
        #         res = min(res, left_cost + right_cost + left_max * right_max)
        #     return res, range_max(i, j)
        #
        # return dfs(0, len(arr) - 1)[0]

        # 贪心依次合并相邻中更小的组合
        ans = 0
        st = []
        for right in arr:
            while st and st[-1] <= right:
                mid = st.pop()
                if not st or st[-1] > right:
                    ans += mid * right
                else:
                    ans += mid * st[-1]
            st.append(right)
        while len(st) > 1:
            ans += st.pop() * st[-1]
        return ans
