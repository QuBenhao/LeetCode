import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.evenOddBit(test_input)

    def evenOddBit(self, n: int) -> List[int]:
        a, b, length = 0, 0, 0
        while n:
            if n & 1:
                if length & 1:
                    b += 1
                else:
                    a += 1
            length += 1
            n >>= 1
        return [a,b]
