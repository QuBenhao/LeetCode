import solution
from collections import Counter
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkStrings(*test_input)

    def checkStrings(self, s1: str, s2: str) -> bool:
        return Counter(s1[::2]) == Counter(s2[::2]) and Counter(s1[1::2]) == Counter(s2[1::2])
