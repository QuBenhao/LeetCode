import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.twoSum(*test_input)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp = dict()
        for i, num in enumerate(nums):
            if (t := target - num) in mp:
                return [mp[t], i]
            mp[num] = i
