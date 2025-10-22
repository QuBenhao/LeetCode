import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.hasSameDigits(test_input)

    def hasSameDigits(self, s: str) -> bool:
        nums = list(map(int, s))
        while len(nums) > 2:
            for i in range(len(nums) - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            nums.pop()
        return nums[0] == nums[1]
