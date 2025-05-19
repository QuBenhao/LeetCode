import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countSubstrings(test_input)

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        ans = 0
        for i in range(n - 1, -1, -1):
            is_palindrome[i][i] = True
            ans += 1
            for j in range(i + 1, n):
                if s[j] == s[i] and (j - i < 3 or is_palindrome[i+1][j-1]):
                    is_palindrome[i][j] = True
                    ans += 1
        return ans
