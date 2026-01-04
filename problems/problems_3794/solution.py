import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.reversePrefix(*test_input)

    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1] + s[k:]
