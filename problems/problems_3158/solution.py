import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.duplicateNumbersXOR(test_input)

    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        ans, s = 0, set()
        for num in nums:
            if num in s:
                ans ^= num
            else:
                s.add(num)
        return ans
