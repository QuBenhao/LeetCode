import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.majorityElement(test_input)

    def majorityElement(self, nums: List[int]) -> int:
        ans = cnt = 0
        for num in nums:
            if cnt == 0:
                ans = num
                cnt = 1
            elif num == ans:
                cnt += 1
            else:
                cnt -= 1
        return ans
