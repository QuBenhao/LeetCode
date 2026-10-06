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
        After adjacent characters are removed, the characters on either side become adjacent. This is similar to a palindrome.
        """

        n = len(s)
        can_be_empty = [[False] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            can_be_empty[i + 1][i] = True  # Empty string
            for j in range(i + 1, n):
                # Property 2: removing adjacent characters makes previously separated characters adjacent, allowing further removals. [Similar to a palindrome]
                if is_consecutive(s[i], s[j]) and can_be_empty[i + 1][j - 1]:
                    can_be_empty[i][j] = True
                    continue
                # Property 3: for substring A=B+C, if both B and C can be completely removed, then A can also be completely removed.
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

