import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numWaterBottles(*test_input)

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles - 1) // (numExchange - 1)
