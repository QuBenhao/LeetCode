from math import ceil

import solution
from collections import Counter
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.successfulPairs(*test_input)

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        counts = Counter(potions)
        mx = max(counts.keys())
        pre_sum = [0] * (mx + 1)
        pre_sum[mx] = counts[mx]
        for i in range(mx - 1, -1, -1):
            pre_sum[i] = pre_sum[i + 1] + counts[i]
        ans = [0] * len(spells)
        for i, s in enumerate(spells):
            c = ceil(success / s)
            if c > mx:
                continue
            ans[i] = pre_sum[c]
        return ans
