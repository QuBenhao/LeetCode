import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.partitionArray(*test_input)

    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        cur = nums[0]
        for num in nums:
            if num - cur > k:
                ans += 1
                cur = num
        return ans