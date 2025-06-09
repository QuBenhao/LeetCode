from functools import cache
from math import inf
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumTotalCost(test_input)

    def maximumTotalCost(self, nums: List[int]) -> int:
        n = len(nums)
        # 长度超过2的子数组, 不分割和分割后成本之和一致 (对应元素的正负号一致)
        f0, f1 = nums[0], nums[0] # f0代表上次取了负, f1代表上次取了正
        for i in range(1, n):
            f0, f1 = f1 - nums[i], max(f0, f1) + nums[i]
        return max(f0, f1)
