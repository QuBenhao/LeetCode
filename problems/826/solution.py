import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxProfitAssignment(*test_input)

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
                pass