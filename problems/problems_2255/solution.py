import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countPrefixes(*test_input)

    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum(s.startswith(v) for v in words)

