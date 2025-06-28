import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxSubsequence(*test_input)

    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(range(len(nums)), key=lambda x: -nums[x])[:k]
        return [nums[i] for i in sorted(sorted_nums)]
