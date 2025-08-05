import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countNumbersWithUniqueDigits(test_input)

    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 10
        last = 9
        for i in range(2, n + 1):
            cur = last * (11 - i)
            ans += cur
            last = cur
        return ans
