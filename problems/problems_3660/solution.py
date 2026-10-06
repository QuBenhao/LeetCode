import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxValue(test_input)

    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums[:]

        # Prefix maximum
        preMax = [0] * n
        preMax[0] = nums[0]
        for i in range(1, n):
            preMax[i] = max(preMax[i - 1], nums[i])

        # Traverse from right to left, maintaining the suffix minimum
        ans = [0] * n
        ans[n - 1] = preMax[n - 1]  # The last position can jump to the global maximum
        sufMin = nums[n - 1]

        for i in range(n - 2, -1, -1):
            # If preMax[i] > sufMin, a connection to i+1 is possible
            if preMax[i] > sufMin:
                ans[i] = ans[i + 1]
            else:
                ans[i] = preMax[i]
            sufMin = min(sufMin, nums[i])

        return ans
