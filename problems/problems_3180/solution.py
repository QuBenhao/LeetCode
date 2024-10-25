import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxTotalReward(test_input)

    def maxTotalReward(self, rewardValues: List[int]) -> int:
        f = 1
        for v in sorted(set(rewardValues)):
            f |= (f & ((1 << v) - 1)) << v
        return f.bit_length() - 1
