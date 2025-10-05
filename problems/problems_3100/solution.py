import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxBottlesDrunk(*test_input)

    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        while numBottles >= numExchange:
            ans += numExchange
            numBottles -= numExchange - 1
            numExchange += 1
        return ans + numBottles
