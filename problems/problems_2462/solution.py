import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.totalCost(*test_input)

    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
                pass