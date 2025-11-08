import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumOneBitOperations(test_input)

    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        k = n.bit_length()
        return (1 << k) - 1 - self.minimumOneBitOperations(n - (1 << (k - 1)))
