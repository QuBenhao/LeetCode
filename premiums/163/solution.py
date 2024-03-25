import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMissingRanges(*test_input)

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
                pass