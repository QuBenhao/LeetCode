import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestLine(*test_input)

    def longestLine(self, mat: List[List[int]]) -> int:
            pass