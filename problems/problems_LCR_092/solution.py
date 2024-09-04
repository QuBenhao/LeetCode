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
            # 一共有k个1，右边就有n-i-k+one个0，提取n和k在最后加
            ans = min(ans, one * 2 - i)
            one += s[i] == '1'
        return min(ans + n - one, one)
