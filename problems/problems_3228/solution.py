import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxOperations(test_input)

    def maxOperations(self, s: str) -> int:
        ans = 0
        cur = 0
        for i in range(len(s) - 2, -1, -1):
            if s[i] == '1':
                if s[i + 1] == '0':
                    cur += 1
                ans += cur
        return ans
