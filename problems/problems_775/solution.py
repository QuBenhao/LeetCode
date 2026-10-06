from math import inf
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isIdealPermutation(test_input)

    def isIdealPermutation(self, nums: List[int]) -> bool:
        # nums is a permutation of 0 through n-1
        # If nums[i] > nums[j] and i < j + 2
        # Position i can only contain one of [i-1, i, i+1]
        for i, num in enumerate(nums):
            if abs(num - i) > 1:
                return False
        return True
