from itertools import accumulate, pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minTime(*test_input)

    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        s = list(accumulate(skill, initial=0))  # skill 的前缀和
        start = 0
        for pre, cur in pairwise(mana):
            start += max(pre * s[i + 1] - cur * s[i] for i in range(n))
        return start + mana[-1] * s[-1]
