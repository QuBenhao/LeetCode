import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(*test_input)

    def minOperations(self, nums: List[int], target: List[int]) -> int:
        s = set()
        for num, t in zip(nums, target):
            if num != t:
                s.add(num)
        return len(s)
