import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimizedStringLength(test_input)

    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
