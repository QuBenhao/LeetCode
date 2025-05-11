import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.partition(test_input)

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        is_palindrome = [[False] * n for _ in range(n)]
        for i in range(n):
            is_palindrome[i][i] = True
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                is_palindrome[i][j] = s[i] == s[j] and (j - i < 3 or is_palindrome[i + 1][j - 1])

        ans = []
        path = []

        def backtrack(idx: int):
            if idx == n:
                ans.append(path[:])
                return
            for j in range(n-1, idx - 1, -1):
                if is_palindrome[idx][j]:
                    path.append(s[idx:j + 1])
                    backtrack(j+1)
                    path.pop()

        backtrack(0)
        return ans
