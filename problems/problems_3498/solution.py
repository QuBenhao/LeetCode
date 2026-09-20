import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.reverseDegree(test_input)

    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, c in enumerate(s, start=1):
            ans += i * (ord('z') - ord(c) + 1)
        return ans
