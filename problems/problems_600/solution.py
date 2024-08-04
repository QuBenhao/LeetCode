import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findIntegers(test_input)

    def findIntegers(self, n: int) -> int:
        # dp[i]表示长度为i的二进制数中不包含相邻两个1的个数
        dp = [0] * 31
        dp[0], dp[1] = 1, 2
        for i in range(2, 31):
            dp[i] = dp[i - 1] + dp[i - 2]
        n += 1
        pre = 0
        res = 0
        for i in range(29, -1, -1):
            if (n >> i) & 1:
                res += dp[i]
                if pre:
                    return res
                pre = 1
            else:
                pre = 0
        return res
