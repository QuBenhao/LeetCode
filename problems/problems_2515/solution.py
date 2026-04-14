from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.closestTarget(*test_input)

    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans = inf
        for i, word in enumerate(words):
            if word == target:
                ans = min(ans, abs(i - startIndex), len(words) - abs(i - startIndex))
        return ans if ans != inf else -1
