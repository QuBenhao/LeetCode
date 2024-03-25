import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxXor(*test_input)

    def maxXor(self, n: int, edges: List[List[int]], values: List[int]) -> int:
                pass