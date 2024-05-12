import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minDays(test_input)

    @lru_cache(None)
    def minDays(self, n: int) -> int:
        if n <= 1:
            return 1
        return min(self.minDays(n // 2) + n % 2, self.minDays(n // 3) + n % 3) + 1
