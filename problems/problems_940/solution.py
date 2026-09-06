import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.distinctSubseqII(test_input)

    def distinctSubseqII(self, s: str) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * 26  # dp[c]: 以字符 c 结尾的不同子序列个数
        for ch in s:
            dp[ord(ch) - 97] = (sum(dp) + 1) % mod  # 接在所有子序列后面 + 单独一个 ch
        return sum(dp) % mod

