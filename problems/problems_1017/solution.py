import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.baseNeg2(test_input)

    def baseNeg2(self, n: int) -> str:
        val = 0x55555555 ^ (0x55555555 - n)
        if val == 0:
            return "0"
        res = []
        while val:
            res.append(str(val & 1))
            val >>= 1
        return ''.join(res[::-1])
