import solution
import math
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rearrangeSticks(test_input[0], test_input[1])

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
                # 第一种理解是：
                # 把最小的木棍填在第一个位置，必定会被看到，故木棍数-1且看到的数-1
                # 把最小的那根木棍填在除第一个位置外的任意一个位置(有i-1个)，都不会被看到，故 木棍数-1且看到的数不变

                # 第二种理解是:
                # 最后一根木棍能被看到，那它只能是最大的那根木棍，故 木棍数-1且看到的数-1
                # 最后一根木棍不能被看到，那它可以是1到(i-1)中的任意一个木棍(有i-1个)，都不会被看到，故 木棍数-1且看到的数不变
                g[j] = (f[j] * (i - 1) + f[j - 1]) % mod
            f = g

        return f[k]
