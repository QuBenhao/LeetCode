import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minInsertions(test_input)

    def minInsertions(self, s: str) -> int:
        ans, left = 0, 0
        i, n = 0, len(s)
        while i < n:
            if s[i] == ')':
                if i < n - 1 and s[i + 1] == ')':
                    if left:
                        left -= 1
                    else:
                        ans += 1
                    i = i + 2
                else:
                    ans += 1
                    if left:
                        left -= 1
                    else:
                        ans += 1
                    i += 1
            else:
                left += 1
                i += 1
        ans += left * 2
        return ans
