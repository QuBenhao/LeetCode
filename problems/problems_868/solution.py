import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.binaryGap(test_input)

    def binaryGap(self, n: int) -> int:
        last = -1
        ans = 0
        while n:
            low_bit = n & -n
            cur = low_bit.bit_length()
            if last != -1:
                ans = max(ans, cur - last)
            last = cur
            n ^= low_bit
        return ans
