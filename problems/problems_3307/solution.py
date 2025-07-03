import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.kthCharacter(*test_input)

    def kthCharacter(self, k: int, operations: List[int]) -> str:
        count = 0
        while k > 1:
            idx = (k - 1).bit_length() - 1
            if operations[idx]:
                count += 1
            k -= 1 << idx
        return chr(ord('a') + count % 26)
