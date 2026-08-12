import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestRepeating(*test_input)

    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        pass

