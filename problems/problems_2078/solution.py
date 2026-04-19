import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxDistance(test_input)

    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        # 首尾颜色不同，直接返回最大距离
        if colors[0] != colors[-1]:
            return n - 1

        # 从右往左找第一个与首颜色不同的位置
        right = n - 1
        while right > 0 and colors[right] == colors[0]:
            right -= 1

        # 从左往右找第一个与尾颜色不同的位置
        left = 0
        while left < n - 1 and colors[left] == colors[-1]:
            left += 1

        return max(right, n - 1 - left)
