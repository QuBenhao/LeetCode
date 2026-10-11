from math import isqrt

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sumOfSquares(test_input)

    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)

        def all_divisors(num):
            if num < 1:
                raise ValueError("请输入正整数")

            for d in range(1, isqrt(num) + 1):
                if num % d == 0:
                    yield d

                    other = num // d
                    if other != d:  # 平方根只记录一次
                        yield other

        return sum(nums[i - 1] ** 2 for i in all_divisors(n))
