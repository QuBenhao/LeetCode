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

        # Alternating patterns: 10101 and 1010
        # XOR gives 11111
        return (x := n ^ (n >> 1)) & (x + 1) == 0
