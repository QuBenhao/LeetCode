from itertools import accumulate

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minZeroArray(*test_input)

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # # 二分+差分
        # n, m = len(nums), len(queries)
        # def check(x):
        #     diff = [0] * (n + 1)
        #     for i in range(x):
        #         l, r, v = queries[i]
        #         diff[l] += v
        #         diff[r+1] -= v
        #     return all(d >= num for d, num in zip(accumulate(diff), nums))
        #
        # left, right = 0, m + 1
        # while left < right:
        #     mid = (left + right) // 2
        #     if check(mid):
        #         right = mid
        #     else:
        #         left = mid + 1
        # return left if left < m + 1 else -1

        # 差分+双指针
        diff = [0] * (len(nums) + 1)
        k, cur = 0, 0
        for i, (num, d) in enumerate(zip(nums, diff)):
            cur += d
            while k < len(queries) and cur < num:
                l, r, v = queries[k]
                diff[l] += v
                diff[r + 1] -= v
                if l <= i <= r:
                    cur += v
                k += 1
            if cur < num:
                return -1
        return k
