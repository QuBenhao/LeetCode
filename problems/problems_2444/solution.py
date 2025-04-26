import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countSubarrays(*test_input)

    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # 每个区间内找到最两侧的左右界，区间由非法数字分割
        ans = 0
        min_left, max_left = -1, -1
        invalid = -1
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                invalid = i
            if num == minK:
                min_left = i
            if num == maxK:
                max_left = i
            # 右端点为i，左端点最右需包含minK和maxK，最左需从invalid右边开始
            ans += max(0, min(min_left, max_left) - invalid)
        return ans
