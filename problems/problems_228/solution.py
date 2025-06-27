from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.summaryRanges(test_input)

    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        left, right = -inf, -inf
        for num in nums + [inf]:
            if num > right + 1:
                if left != -inf:
                    ans.append(f"{left}->{right}" if right != left else f"{left}")
                left = right = num
            elif num == right + 1:
                right += 1
        return ans
