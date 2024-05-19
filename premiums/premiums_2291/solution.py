import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumProfit(*test_input)

    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
                pass