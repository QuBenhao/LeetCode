import solution
from typing import *
from itertools import pairwise


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.temperatureTrend(*test_input)

    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        ans = cur = 0
        for (a0, b0), (a1, b1) in pairwise(zip(temperatureA, temperatureB)):
            if (a1 > a0) - (a1 < a0) == (b1 > b0) - (b1 < b0):
                cur += 1
                ans = max(ans, cur)
            else:
                cur = 0
        return ans
