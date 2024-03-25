import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.wordBreak(*test_input)

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
            pass