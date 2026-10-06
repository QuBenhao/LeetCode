import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minFlipsMonoIncr(test_input)

    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        ans = n
        one = 0
        for i in range(n):
            # With k ones in total, there are n-i-k+one zeros on the right; factor out n and k and add them at the end
            ans = min(ans, one * 2 - i)
            one += s[i] == '1'
        return min(ans + n - one, one)
