import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isAnagram(*test_input)

    def isAnagram(self, s: str, t: str) -> bool:
        return s != t and sorted(s) == sorted(t)
