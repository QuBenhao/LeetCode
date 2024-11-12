import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countKConstraintSubstrings(*test_input)

    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = left = 0
        counts = [0, 0]
        for i, c in enumerate(s):
            counts[ord(c) & 1] += 1
            while counts[0] > k and counts[1] > k:
                counts[ord(s[left]) & 1] -= 1
                left += 1
            ans += i - left + 1
        return ans
