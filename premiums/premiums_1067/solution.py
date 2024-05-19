import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.digitsCount(*test_input)

    def digitsCount(self, d: int, low: int, high: int) -> int:
                pass