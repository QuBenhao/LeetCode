import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.lexicographicallySmallestString(test_input)

    def lexicographicallySmallestString(self, s: str) -> str:
        n = len(s)
        can_be_empty = [[False] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            can_be_empty[i + 1][i] = True  # 空串
            for j in range(i + 1, n):
                # 性质 2
                if is_consecutive(s[i], s[j]) and can_be_empty[i + 1][j - 1]:
                    can_be_empty[i][j] = True
                    continue
                # 性质 3
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

