import solution
from functools import lru_cache
import numpy as np


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.tribonacci(test_input)

    @lru_cache(None)
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        if n <= 2:
            return 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

    # def tribonacci(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if not n:
    #         return 0
    #     if n <= 2:
    #         return 1
    #     ans = np.eye(3)
    #     a = np.array([[1, 1, 1],  [1, 0, 0], [0, 1, 0]])
    #     k = n - 2
    #     while k != 0:
    #         if (k & 1) != 0:
    #             ans = np.dot(ans, a)
    #         a = np.dot(a, a)
    #         k >>= 1
    #     return int(ans[0][0]) + int(ans[0][1])
