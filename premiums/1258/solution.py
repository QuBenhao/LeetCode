import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.generateSentences(*test_input)

    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
            pass