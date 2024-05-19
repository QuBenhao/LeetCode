import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCost(*test_input)

    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
                pass