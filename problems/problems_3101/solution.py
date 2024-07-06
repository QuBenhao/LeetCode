import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countAlternatingSubarrays(test_input)

    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        ans = cnt = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                cnt += 1
            else:
                cnt = 1
            ans += cnt
        return ans
