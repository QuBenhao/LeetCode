from functools import lru_cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.diagonalPrime(test_input)

    def diagonalPrime(self, nums: List[List[int]]) -> int:
        @lru_cache(None)
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        ans, n = 0, len(nums)
        for i in range(n):
            if is_prime(nums[i][i]):
                ans = max(ans, nums[i][i])
            if is_prime(nums[i][n - 1 - i]):
                ans = max(ans, nums[i][n - 1 - i])
        return ans
