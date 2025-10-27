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
                # 往两边出发均可
                ans += 2
            elif abs(pre * 2 - s) == 1:
                # 往多一个的方向出发
                ans += 1
        return ans
