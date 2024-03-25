import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.addBoldTag(*test_input)

    def addBoldTag(self, s: str, words: List[str]) -> str:
            pass