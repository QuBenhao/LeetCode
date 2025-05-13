import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.lengthAfterTransformations(*test_input)

    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10 ** 9 + 7

        # [f(0), f(1), f(2), ..., f(25)]
        # [f(25), f(0)+f(25), f(1), f(2), ..., f(24)]
        # 转移矩阵
        # [[0, 1, 0, 0, ..., 0],
        #  [0, 0, 1, 0, ..., 0],
        #  [0, 0, 0, 1, ..., 0],
        #  [0, 0, 0, 0, ..., 1],
        #  [1, 1, 0, 0, ..., 0],

        counts = [0] * 26
        remain = t % 26
        for c in s:
            cur = ord(c) - ord('a')
            if cur + remain >= 26:
                counts[cur + remain - 26] = (counts[cur + remain - 26] + 1) % mod
                counts[cur + remain - 25] = (counts[cur + remain - 25] + 1) % mod
            else:
                counts[cur + remain] = (counts[cur + remain] + 1) % mod
        t -= remain
        while t > 0:
            nxt = list(counts)
            for i in range(26):
                if i < 25:
                    nxt[i + 1] = (nxt[i + 1] + counts[i]) % mod
                elif i == 25:
                    nxt[0] = (nxt[0] + counts[i]) % mod
                    nxt[1] = (nxt[1] + counts[i]) % mod
            counts = nxt
            t -= 26
        return sum(counts) % mod
