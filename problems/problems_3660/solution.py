import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxValue(test_input)

    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 1:
            return nums[:]

        # 前缀最大值
        preMax = [0] * n
        preMax[0] = nums[0]
        for i in range(1, n):
            preMax[i] = max(preMax[i - 1], nums[i])

        # 从右往左遍历，维护后缀最小值
        ans = [0] * n
        ans[n - 1] = preMax[n - 1]  # 最后一个位置可以跳到全局最大值
        sufMin = nums[n - 1]

        for i in range(n - 2, -1, -1):
            # 如果 preMax[i] > sufMin，可以桥接到 i+1
            if preMax[i] > sufMin:
                ans[i] = ans[i + 1]
            else:
                ans[i] = preMax[i]
            sufMin = min(sufMin, nums[i])

        return ans
