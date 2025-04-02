import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumTripletValue(test_input)

    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [nums[-1]] * n
        ans = 0
        for i in range(n - 2, 0, -1):
            right_max[i] = max(right_max[i + 1], nums[i])
        pre_max = nums[0]
        for j in range(1, n - 1):
            ans = max(ans, (pre_max - nums[j]) * right_max[j + 1])
            pre_max = max(pre_max, nums[j])
        return ans
