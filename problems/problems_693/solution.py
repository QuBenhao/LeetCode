import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.hasAlternatingBits(test_input)

    def hasAlternatingBits(self, n: int) -> bool:
        # l = n.bit_length()
        # for i in range(l):
        #     if ((i & 1) != (l & 1)) != ((n >> i & 1) == 1):
        #         return False
        # return True

        # 交替特性 10101 1010
        # 异或得 11111
        return (x := n ^ (n >> 1)) & (x + 1) == 0
