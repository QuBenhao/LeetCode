import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countHillValley(test_input)

    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        idx = 0
        last_diff = 0
        last = nums[0]
        while idx < n:
            while idx < n - 1 and nums[idx] == nums[idx + 1]:
                idx += 1
            cur_diff = nums[idx] - last
            if last_diff * cur_diff < 0:
                ans += 1
            last = nums[idx]
            last_diff = 1 if cur_diff > 0 else -1 if cur_diff < 0 else 0
            idx += 1
        return ans
