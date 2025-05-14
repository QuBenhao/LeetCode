import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getLongestSubsequence(*test_input)

    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        dp0, dp1 = [], []
        for c, w in zip(groups, words):
            if len(dp0) % 2 == c ^ 1:
                dp0.append(w)
            if len(dp1) % 2 == c:
                dp1.append(w)
        return dp0 if len(dp0) > len(dp1) else dp1
