import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minElement(test_input)

    def minElement(self, nums: List[int]) -> int:
        ans = 100000
        for num in nums:
            ans = min(ans, sum(map(int, str(num))))
        return ans
