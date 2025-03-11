import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sumOfBeauties(test_input)

    def sumOfBeauties(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        suf_min = [nums[-1]] * n
        for i in range(n - 2, 0, -1):
            suf_min[i] = min(nums[i], suf_min[i + 1])
        pre_max = nums[0]
        for i in range(1, n - 1):
            if pre_max < nums[i] < suf_min[i + 1]:
                ans += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                ans += 1
            pre_max = max(pre_max, nums[i])
        return ans
