import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rob(test_input)

    def rob(self, nums: List[int]) -> int:
        dp_nr, dp_r = 0, 0
        for num in nums:
            dp_nr, dp_r = max(dp_nr, dp_r), dp_nr + num
        return max(dp_nr, dp_r)
