import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMaxLength(test_input)

    def findMaxLength(self, nums: List[int]) -> int:
        count = {0: -1}
        ans = 0
        pre_sum = 0
        for i, num in enumerate(nums):
            pre_sum += 1 if num else -1
            if pre_sum in count:
                ans = max(ans, i - count[pre_sum])
            else:
                count[pre_sum] = i
        return ans

