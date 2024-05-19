import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMaximalUncoveredRanges(*test_input)

    def findMaximalUncoveredRanges(self, n: int, ranges: List[List[int]]) -> List[List[int]]:
            pass