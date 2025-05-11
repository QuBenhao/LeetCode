import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.threeConsecutiveOdds(test_input)

    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cur = 0
        for i, num in enumerate(arr):
            if num % 2 == 1:
                cur += 1
            else:
                cur = 0
            if i > 2 and cur == 3:
                return True
        return False
