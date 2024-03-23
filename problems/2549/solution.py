import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.distinctIntegers(test_input)

    def distinctIntegers(self, n: int) -> int:
        return n - 1 if n > 1 else 1
