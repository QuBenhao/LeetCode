import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findDifferentBinaryString(test_input)

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        ans = [''] * n
        for i, num in enumerate(nums):
            ans[i] = '1' if num[i] == '0' else '0'
        return ''.join(ans)
