import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestAwesome(test_input)

    def longestAwesome(self, s: str) -> int:
        D = 10  # s 中的字符种类数
        n = len(s)
        pos = [n] * (1 << D)  # n 表示没有找到异或前缀和
        pos[0] = -1  # pre[-1] = 0
        ans = pre = 0
        for i, x in enumerate(map(int, s)):
            pre ^= 1 << x
            ans = max(ans, i - pos[pre],  # 偶数
                      max(i - pos[pre ^ (1 << d)] for d in range(D)))  # 奇数
            if pos[pre] == n:  # 首次遇到值为 pre 的前缀异或和，记录其下标 i
                pos[pre] = i
        return ans

