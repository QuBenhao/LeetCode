import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMaximumNumber(*test_input)

    def findMaximumNumber(self, k: int, x: int) -> int:
        num = pre_one = 0
        for i in range(((k + 1) << x).bit_length() - 1, -1, -1):
            # If the current bit i is 1, the added price is:
            # From the left: 2^i * pre_one
            # From the right: the count of 1 bits at positions divisible by x in 1 through 2^i-1 (i.e. i//x * 2^(i-1) ones)
            # pre_one increases when a position divisible by x is encountered
            cur = (pre_one << i) + (i // x << i >> 1)
            if cur <= k:
                k -= cur
                num |= 1 << i
                pre_one += (i + 1) % x == 0
        return num - 1
