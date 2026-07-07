import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sumAndMultiply(test_input)

    def sumAndMultiply(self, n: int) -> int:
        x = s = 0
        pw = 1
        while n:
            n, d = divmod(n, 10)
            if d:
                x += d * pw
                s += d
                pw *= 10
        return x * s

