import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumCost(*test_input)

    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        ans = need1 * cost1 + need2 * cost2
        ans = min(ans, min(need1, need2) * costBoth + (need1 - min(need1, need2)) * cost1 + (need2 - min(need1, need2)) * cost2)
        ans = min(ans, max(need1, need2) * costBoth)
        return ans
