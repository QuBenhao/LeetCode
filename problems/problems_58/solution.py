import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.lengthOfLastWord(test_input)

    def lengthOfLastWord(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if ans:
                    break
                continue
            ans += 1
        return ans
