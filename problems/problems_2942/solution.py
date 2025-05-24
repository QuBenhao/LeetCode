import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findWordsContaining(*test_input)

    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if x in word]
