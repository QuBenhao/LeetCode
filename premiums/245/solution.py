import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.shortestWordDistance(*test_input)

    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
                pass