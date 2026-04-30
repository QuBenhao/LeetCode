import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxRotateFunction(test_input)

    def maxRotateFunction(self, nums: List[int]) -> int:
        # F(0) = 0 * nums[0] + 1 * nums[1] + 2 * nums[2] + ... (n - 1) * nums[n - 1]
        # F(1) = F(0) - s + n * nums[0]
        s = f0 = 0
        for i, num in enumerate(nums):
            s += num
            f0 += i * num
        ans, n = f0, len(nums)
        for i in range(1, n):
            f0 += n * nums[i - 1]  - s
            ans = max(ans, f0)
        return ans
