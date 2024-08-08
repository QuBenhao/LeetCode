import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.separateDigits(test_input)

    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            cur = []
            while num:
                cur.append(num % 10)
                num //= 10
            ans.extend(cur[::-1])
        return ans
