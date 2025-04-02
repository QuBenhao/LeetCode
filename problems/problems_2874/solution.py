import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumTripletValue(test_input)

    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        suffix_max = [nums[-1]] * n
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], nums[i])
        ans = 0
        pre_max = nums[0]
        for j in range(1, n - 1):
            pre_max = max(pre_max, nums[j - 1])
            ans = max(ans, (pre_max - nums[j]) * suffix_max[j + 1])
        return ans
