import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.wordsTyping(*test_input)

    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
                pass