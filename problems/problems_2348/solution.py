import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.zeroFilledSubarray(test_input)

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        left = right = 0
        n = len(nums)
        while right < n:
            while left < n and nums[left] != 0:
                left += 1
            right = left
            while right < n and nums[right] == 0:
                right += 1
            ans += (right - left) * (right - left + 1) // 2
            left = right
        return ans
