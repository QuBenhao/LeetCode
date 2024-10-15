from math import isqrt, sqrt

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxHeightOfTriangle(*test_input)

    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        # if odd lines, the first line has 1,3,5,...,2n-1; which sum is n^2
        # if even lines, the second line has 2,4,6,...,2n; which sum is n(n+1);
        def f(n, m):
            odd = isqrt(n)
            even = int((sqrt(m * 4 + 1) - 1) / 2)
            return even * 2 + 1 if odd > even else odd * 2

        return max(f(red, blue), f(blue, red))
