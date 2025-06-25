import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestSubsequence(*test_input)

    def longestSubsequence(self, s: str, k: int) -> int:
        ans = s.count('0')
        cur = 0
        for i in range(min(len(s), 31)):
            if s[-i-1] == '1' and cur | (1 << i) <= k:
                ans += 1
                cur |= 1 << i
        return ans
