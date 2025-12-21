import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.mirrorDistance(test_input)

    def mirrorDistance(self, n: int) -> int:
        a, b = n, 0
        while a:
            b = 10 * b + a % 10
            a //= 10
        return abs(n - b)
