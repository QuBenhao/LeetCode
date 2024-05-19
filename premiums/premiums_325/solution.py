import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxSubArrayLen(*test_input)

    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
            pass