import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sumOfTheDigitsOfHarshadNumber(test_input)

    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        num, s = x, 0
        while num:
            num, mod = divmod(num, 10)
            s += mod
        return  s if x % s == 0 else -1
