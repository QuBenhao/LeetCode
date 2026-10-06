import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestAwesome(test_input)

    def longestAwesome(self, s: str) -> int:
        D = 10  # Number of possible distinct characters in s
        n = len(s)
        pos = [n] * (1 << D)  # n means this prefix XOR has not been found
        pos[0] = -1  # pre[-1] = 0
        ans = pre = 0
        for i, x in enumerate(map(int, s)):
            pre ^= 1 << x
            ans = max(ans, i - pos[pre],  # Even count
                      max(i - pos[pre ^ (1 << d)] for d in range(D)))  # Odd count
            if pos[pre] == n:  # Record index i on the first occurrence of prefix XOR pre
                pos[pre] = i
        return ans

