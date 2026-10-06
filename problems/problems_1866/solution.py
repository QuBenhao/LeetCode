import solution
import math
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rearrangeSticks(*test_input)

    def rearrangeSticks(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        mod = 10 ** 9 + 7

        f = [1] + [0] * k
        for i in range(1, n + 1):
            g = [0] * (k + 1)
            for j in range(1, k + 1):
                # First interpretation:
                # Put the shortest stick first, where it is visible: decrease both the stick count and visible count by 1
                # Put the shortest stick in any of the other i-1 positions, where it is hidden: decrease the stick count by 1 and keep the visible count unchanged

                # Second interpretation:
                # If the last stick is visible, it must be the tallest: decrease both the stick count and visible count by 1
                # If the last stick is hidden, it can be any of the i-1 shorter sticks: decrease the stick count by 1 and keep the visible count unchanged
                g[j] = (f[j] * (i - 1) + f[j - 1]) % mod
            f = g

        return f[k]
