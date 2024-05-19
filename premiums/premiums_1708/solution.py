import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestSubarray(*test_input)

    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
            pass