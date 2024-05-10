import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countTestedDevices(test_input)

    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        for b in batteryPercentages:
            if b > ans:
                ans += 1
        return ans
