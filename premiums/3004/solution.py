import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumSubtreeSize(*test_input)

    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
            pass