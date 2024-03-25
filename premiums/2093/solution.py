import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumCost(*test_input)

    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
                pass