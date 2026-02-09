import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestBalanced(test_input)

    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            odds, evens = set(), set()
            for j in range(i, n):
                if nums[j] & 1:
                    odds.add(nums[j])
                else:
                    evens.add(nums[j])
                if len(odds) == len(evens):
                    ans = max(ans, j - i + 1)
        return ans
