import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxPrice(*test_input)

    def maxPrice(self, items: List[List[int]], capacity: int) -> float:
            pass