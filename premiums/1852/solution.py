import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.distinctNumbers(*test_input)

    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
            pass