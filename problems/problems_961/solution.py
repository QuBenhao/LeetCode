import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.repeatedNTimes(test_input)

    def repeatedNTimes(self, nums: List[int]) -> int:
        # if nums[0] == nums[3]:
        #     return nums[0]
        # for i, num in enumerate(nums):
        #     if nums[i + 1] == num or nums[i + 2] == num:
        #         return num
        # return -1

        # 摩尔投票
        ans, ans_count = 0, 0
        for num in nums[1:]:
            if num == nums[0]:
                return num
            if ans_count == 0:
                ans, ans_count = num, 1
            elif num == ans:
                return num
            else:
                ans_count -= 1
        return ans
