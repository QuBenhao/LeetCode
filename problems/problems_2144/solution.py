import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumCost(test_input)

    def minimumCost(self, cost: List[int]) -> int:
        ans = 0
        cost.sort(reverse=True)
        n = len(cost)
        for i in range(0, n, 3):
            if i + 2 < n:
                ans += cost[i] + cost[i + 1]
            else:
                ans += sum(cost[i:])
        return ans
