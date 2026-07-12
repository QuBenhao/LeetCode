import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sequentialDigits(*test_input)

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        pass

