import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallestNumber(test_input)

    def smallestNumber(self, n: int) -> int:
        return (1 << n.bit_length()) - 1 if n & (n + 1) != 0 else n
