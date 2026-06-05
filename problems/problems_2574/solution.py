import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.leftRightDifference(test_input)

    def leftRightDifference(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        pre = 0
        ans = []
        for num in nums:
            ans.append(abs(s - 2 * pre - num))
            pre += num
        return ans
