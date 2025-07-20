import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkDivisibility(test_input)

    def checkDivisibility(self, n: int) -> bool:
        s, m = 0, 1
        num = n
        while num:
            d = num % 10
            s += d
            m *= d
            num //= 10
        return n % (s + m) == 0

