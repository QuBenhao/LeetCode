import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countValidSelections(test_input)

    def countValidSelections(self, nums: List[int]) -> int:
        s = sum(nums)
        ans = pre = 0
        for num in nums:
            if num:
                pre += num
            elif pre * 2 == s:
                # Either starting direction works
                ans += 2
            elif abs(pre * 2 - s) == 1:
                # Start toward the side whose total is larger by one
                ans += 1
        return ans
