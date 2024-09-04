import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minFlipsMonoIncr(test_input)

    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        ans = n
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + int(s[i] == '1')
        cur = 0
        for i in range(n - 1, -1, -1):
            ans = min(ans, cur + pre_sum[i])
            cur += int(s[i] == '0')
        return ans
