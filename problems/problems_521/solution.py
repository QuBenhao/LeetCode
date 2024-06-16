import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findLUSlength(*test_input)

    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))
