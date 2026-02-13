from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestBalanced(test_input)

    def longestBalanced(self, s: str) -> int:
        n = len(s)

        # 一种字母
        ans = i = 0
        while i < n:
            start = i
            i += 1
            while i < n and s[i] == s[i - 1]:
                i += 1
            ans = max(ans, i - start)

        # 两种字母
        def f(x: str, y: str) -> None:
            nonlocal ans
            i = 0
            while i < n:
                pos = {0: i - 1}  # 前缀和数组的首项是 0，位置相当于在 i-1
                d = 0  # x 的个数减去 y 的个数
                while i < n and (s[i] == x or s[i] == y):
                    d += 1 if s[i] == x else -1
                    if d in pos:
                        ans = max(ans, i - pos[d])
                    else:
                        pos[d] = i
                    i += 1
                i += 1

        f('a', 'b')
        f('a', 'c')
        f('b', 'c')

        # 三种字母
        # 前缀和数组的首项是 0，位置相当于在 -1
        pos = {(0, 0): -1}
        cnt = defaultdict(int)
        for i, b in enumerate(s):
            cnt[b] += 1
            p = (cnt['a'] - cnt['b'], cnt['b'] - cnt['c'])
            if p in pos:
                ans = max(ans, i - pos[p])
            else:
                pos[p] = i
        return ans
