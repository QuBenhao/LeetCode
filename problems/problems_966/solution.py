import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.spellchecker(*test_input)

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        pass

