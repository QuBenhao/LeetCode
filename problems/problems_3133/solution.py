import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minEnd(*test_input)

    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        # x的二进制第i位，n的二进制第j位
        i = j = 0
        # 二进制从右往左遍历n
        while n >> j:
            # 如果x的第i位为0，将n的第j位赋给x的第i位 (因为x为1的位我们构造也必须填1)
            if not x >> i & 1:
                # 将n的第j位赋给x的第i位
                x |= (n >> j & 1) << i
                j += 1
            i += 1
        return x
