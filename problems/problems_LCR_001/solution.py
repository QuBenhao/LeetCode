import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.divide(*test_input)

    def divide(self, a: int, b: int) -> int:
        if a == -1 << 31 and b == -1:
            return (1 << 31) - 1
        dividend, divisor, res = abs(a), abs(b), 0
        for i in range(31, -1, -1):
            if dividend >= divisor << i:
                res += 1 << i
                dividend -= divisor << i
        return res if (a > 0) == (b > 0) else -res
