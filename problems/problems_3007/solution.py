import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMaximumNumber(*test_input)

    def findMaximumNumber(self, k: int, x: int) -> int:
        num = pre_one = 0
        for i in range(((k + 1) << x).bit_length() - 1, -1, -1):
            # 当前i位为1的话，会增加:
            # 左边 2^i * pre_one 个价值
            # 右边 1到2^i-1里出现多少个x倍数位为1 的价值 (即 i//x * 2^(i-1)个1)
            # pre_one的价值会在遇到x倍数时增加
            cur = (pre_one << i) + (i // x << i >> 1)
            if cur <= k:
                k -= cur
                num |= 1 << i
                pre_one += (i + 1) % x == 0
        return num - 1
