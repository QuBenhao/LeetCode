import solution
from typing import *
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallestPalindrome(test_input)

    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)
        mid = ""
        left = []
        for ch in sorted(cnt):
            c = cnt[ch]
            if c & 1:
                mid = ch
            left.append(ch * (c // 2))
        left = "".join(left)
        return left + mid + left[::-1]
