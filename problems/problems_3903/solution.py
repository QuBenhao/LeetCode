import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.firstStableIndex(*test_input)

    def firstStableIndex(self, nums: list[int], k: int) -> int:
        pass

