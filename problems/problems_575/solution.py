import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.distributeCandies(test_input)

    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(set(candyType)))
