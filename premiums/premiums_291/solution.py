import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.wordPatternMatch(*test_input)

    def wordPatternMatch(self, pattern: str, s: str) -> bool:
            pass