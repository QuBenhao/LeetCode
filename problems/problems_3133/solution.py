import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minEnd(*test_input)

    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        # Bit i of x and bit j of n
        i = j = 0
        # Traverse the binary representation of n from right to left
        while n >> j:
            # If bit i of x is 0, assign bit j of n to it (bits set to 1 in x must remain 1 in the result)
            if not x >> i & 1:
                # Assign bit j of n to bit i of x
                x |= (n >> j & 1) << i
                j += 1
            i += 1
        return x
