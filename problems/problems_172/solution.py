import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.trailingZeroes(test_input)

    def trailingZeroes(self, n: int) -> int:
        ans = 0
        while n:
            n //= 5
            ans += n
        return ans
