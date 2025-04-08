import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumOperations(test_input)

    def minimumOperations(self, nums: List[int]) -> int:
        s = set()
        n = len(nums)
        for i in range(n - 1, -1, -1):
            if nums[i] in s:
                return i // 3 + 1
            s.add(nums[i])
        return 0
