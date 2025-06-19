from math import inf
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isIdealPermutation(test_input)

    def isIdealPermutation(self, nums: List[int]) -> bool:
        # nums是0到n-1的排列
        # 如果存在nums[i] > nums[j] 且 i < j + 2
        # i的位置最多放 [i-1, i, i+1] 中的一个数
        for i, num in enumerate(nums):
            if abs(num - i) > 1:
                return False
        return True
