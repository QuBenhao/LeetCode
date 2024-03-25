import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.kthSmallestSubarraySum(*test_input)

    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
            pass