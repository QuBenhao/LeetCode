import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.lengthOfLIS(test_input)

    def lengthOfLIS(self, nums: [int]) -> int:
        tails, res = [0] * len(nums), 0
        for num in nums:
            i, j = 0, res
            while i < j:
                m = (i + j) // 2
                if tails[m] < num: i = m + 1 # For a non-strictly increasing subsequence, change '<' to '<=' on this line.
                else: j = m
            tails[i] = num
            if j == res: res += 1
        return res
