import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findKthLargest(*test_input)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]
