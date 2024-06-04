import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.repeatedSubstringPattern(test_input)

    def repeatedSubstringPattern(self, s: str) -> bool:
        return (s + s).find(s, 1) != len(s)
