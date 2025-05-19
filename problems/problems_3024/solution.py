import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.triangleType(test_input)

    def triangleType(self, nums: List[int]) -> str:
        if nums[0] + nums[1] <= nums[2] or nums[2] + nums[1] <= nums[0] or nums[0] + nums[2] <= nums[1]:
            return "none"
        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        if nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
            return "isosceles"
        return "scalene"
