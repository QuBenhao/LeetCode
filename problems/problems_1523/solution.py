import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countOdds(*test_input)

    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + (low % 2 == 1 or high % 2 == 1)
