import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.heightChecker(test_input)

    def heightChecker(self, heights: List[int]) -> int:
        return sum(a != b for a, b in zip(heights, sorted(heights)))
