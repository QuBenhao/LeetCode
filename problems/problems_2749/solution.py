from itertools import count

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.makeTheIntegerZero(*test_input)

    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        # num1 - x * num2 = x个可重复二的幂的和 >= x
        for x in count(1):
            num1 -= num2
            # num1 >= x, 否则返回-1
            if x > num1:
                break
            if x >= num1.bit_count():
                return x
        return -1
