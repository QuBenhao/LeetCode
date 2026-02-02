from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isTrionic(test_input)

    def isTrionic(self, nums: List[int]) -> bool:
        # 第一段必为增
        if nums[0] >= nums[1]:
            return False
        cur = 1
        t = 0
        for a, b in pairwise(nums):
            if a == b:
                return False
            # 非拐点
            if (a < b) == (cur == 1):
                continue
            # 拐点
            cur ^= 1
            t += 1
            # 优化提前返回
            if t > 2:
                return False
        return t == 2
