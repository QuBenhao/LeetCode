import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isPowerOfThree(test_input)

    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while not n % 3:
            n //= 3
        return n == 1
