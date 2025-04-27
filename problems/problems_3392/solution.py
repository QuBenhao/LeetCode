from collections import defaultdict
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countSubarrays(test_input)

    def countSubarrays(self, nums: List[int]) -> int:
        return sum(nums[i + 1] % 2 == 0 and nums[i + 1] == (nums[i] + nums[i+2]) * 2 for i in range(len(nums) - 2))
