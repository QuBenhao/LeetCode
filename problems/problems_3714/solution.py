from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestBalanced(test_input)

    def longestBalanced(self, s: str) -> int:
        n = len(s)

        # One distinct letter
        ans = i = 0
        while i < n:
            start = i
            i += 1
            while i < n and s[i] == s[i - 1]:
                i += 1
            ans = max(ans, i - start)

        # Two distinct letters
        def f(x: str, y: str) -> None:
            nonlocal ans
            i = 0
            while i < n:
                pos = {0: i - 1}  # The first entry of the prefix sum array is 0, corresponding to position i-1
                d = 0  # Count of x minus count of y
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

        # Three distinct letters
        # The first entry of the prefix sum array is 0, corresponding to position -1
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
