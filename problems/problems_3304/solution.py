import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.kthCharacter(test_input)

    def kthCharacter(self, k: int) -> str:
        steps = 0
        while k > 1:
            k -= 1 << ((k - 1).bit_length() - 1)
            steps += 1
        return chr(ord('a') + steps % 26)
