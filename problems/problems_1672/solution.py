import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumWealth(test_input)

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(a) for a in accounts)
