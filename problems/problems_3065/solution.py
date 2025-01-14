import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(*test_input)

    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(num < k for num in nums)
