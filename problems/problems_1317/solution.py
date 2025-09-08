import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getNoZeroIntegers(test_input)

    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = 0
        base = 1
        x = n
        while x > 1:
            x, d = divmod(x, 10)
            if d <= 1:
                d += 10
                x -= 1
            a += d // 2 * base
            base *= 10
        return [a, n - a]
