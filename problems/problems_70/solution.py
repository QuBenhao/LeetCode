import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.climbStairs(test_input)

    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b
