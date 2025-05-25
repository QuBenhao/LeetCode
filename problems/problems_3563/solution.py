import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.lexicographicallySmallestString(test_input)

    def lexicographicallySmallestString(self, s: str) -> str:
        def is_consecutive(x: str, y: str) -> bool:
            d = abs(ord(x) - ord(y))
            return d == 1 or d == 25

        """
        消除相邻的字符后, 原来两侧的变成相邻。类似回文串
        """

        n = len(s)
        can_be_empty = [[False] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            can_be_empty[i + 1][i] = True  # 空串
            for j in range(i + 1, n):
                # 性质 2: 相邻字符消除后，原本不相邻的字符会变成相邻，可以继续消除。[类似回文串]
                if is_consecutive(s[i], s[j]) and can_be_empty[i + 1][j - 1]:
                    can_be_empty[i][j] = True
                    continue
                # 性质 3: 设子串 A=B+C，如果子串 B 和 C 可以完全消除，那么子串 A 可以完全消除。
                for k in range(i + 1, j - 1):
                    if can_be_empty[i][k] and can_be_empty[k + 1][j]:
                        can_be_empty[i][j] = True
                        break

        f = [''] * (n + 1)
        for i in range(n - 1, -1, -1):
            res = s[i] + f[i + 1]
            for j in range(i + 1, n):
                if can_be_empty[i][j]:
                    res = min(res, f[j + 1])
            f[i] = res
        return f[0]

