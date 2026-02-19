import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countBinarySubstrings(test_input)

    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        cur = pre = 0
        for i in range(n):
            cur += 1
            if i == n - 1 or s[i] != s[i + 1]:
                # 拐点 / 当前组的结束
                ans += min(cur, pre)
                pre = cur
                cur = 0
        return ans
