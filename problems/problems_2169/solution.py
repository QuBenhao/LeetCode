import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countOperations(*test_input)

    def countOperations(self, num1: int, num2: int) -> int:
        x, y = max(num1, num2), min(num1, num2)
        ans = 0
        while y > 0:
            d, r = divmod(x, y)
            ans += d
            x, y = y, r
        return ans
