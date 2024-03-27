import solution
from typing import *
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isAnagram(*test_input)

    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and Counter(s) == Counter(t)
