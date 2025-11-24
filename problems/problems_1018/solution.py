import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.prefixesDivBy5(test_input)

    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        ans = [False] * n
        cur = 0
        for i in range(n):
            cur = (cur * 2 + nums[i]) % 5
            ans[i] = cur == 0
        return ans
