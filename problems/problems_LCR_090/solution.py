import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rob(test_input)

    def rob(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        # rob first, not rob last; or not rob first
        dp_rob, dp_not_rob = nums[0], nums[0]
        for i in range(2, n - 1):
            dp_rob, dp_not_rob = dp_not_rob + nums[i], max(dp_rob, dp_not_rob)
        ans = max(ans, max(dp_rob, dp_not_rob))
        dp_rob, dp_not_rob = 0, 0
        for i in range(1, n):
            dp_rob, dp_not_rob = dp_not_rob + nums[i], max(dp_rob, dp_not_rob)
        ans = max(ans, max(dp_rob, dp_not_rob))
        return ans
