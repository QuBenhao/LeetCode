import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countPairs(*test_input)

    def countPairs(self, nums: List[int], k: int) -> int:
        return sum(nums[i] == nums[j] and (i * j) % k == 0 for i in range(len(nums)) for j in range(i + 1, len(nums)))
