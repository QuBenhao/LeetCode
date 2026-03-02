from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findKthBit(*test_input)

    @cache
    def findKthBit(self, n: int, k: int, invert:bool=False) -> str:
        # f(n) = 2^n - 1
        if n == 1:
            return "1" if invert else "0"
        length = (1 << n) - 1
        half = length >> 1
        if k <= half:
            return self.findKthBit(n - 1, k, invert)
        if k == half + 1:
            return "0" if invert else "1"
        return self.findKthBit(n - 1, length + 1 - k, True if not invert else False)
