import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.trailingZeroes(test_input)

    def trailingZeroes(self, n: int) -> int:
        # Count the factors of 5 in n!
        ans = 0
        cur = 5
        while cur <= n:
            ans += n // cur
            cur *= 5
        return ans
