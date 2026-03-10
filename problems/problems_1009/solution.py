import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.bitwiseComplement(test_input)

    def bitwiseComplement(self, n: int) -> int:
        return n ^ ((1 << n.bit_length()) - 1) if n else 1
