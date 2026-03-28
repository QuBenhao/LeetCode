import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canBeEqual(*test_input)

    def canBeEqual(self, s1: str, s2: str) -> bool:
        from collections import Counter
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])