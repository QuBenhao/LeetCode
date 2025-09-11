import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.doesAliceWin(test_input)

    def doesAliceWin(self, s: str) -> bool:
        return any(c in "aeiou" for c in s)
