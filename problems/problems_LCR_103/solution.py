import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.coinChange(*test_input)

    def coinChange(self, coins: List[int], amount: int) -> int:
        pass

