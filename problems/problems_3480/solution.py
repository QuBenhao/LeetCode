import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxSubarrays(*test_input)

    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        pass

