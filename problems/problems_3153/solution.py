import solution
from typing import *
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sumDigitDifferences(test_input)

    def sumDigitDifferences(self, nums: List[int]) -> int:
        counter = defaultdict(lambda: defaultdict(int))
        ans = 0
        for i, num in enumerate(nums):
            j = 0
            while num:
                num, m = divmod(num, 10)
                ans += i - counter[j][m]
                counter[j][m] += 1
                j += 1
        return ans
