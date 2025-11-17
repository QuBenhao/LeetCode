import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isOneBitCharacter(test_input)

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        idx = 0
        while idx < n - 1:
            if bits[idx] == 0:
                idx += 1
            else:
                idx += 2
        return idx == n - 1
