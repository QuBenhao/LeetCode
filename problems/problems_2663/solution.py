import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallestBeautifulString(*test_input)

    def smallestBeautifulString(self, s: str, k: int) -> str:
        a = ord('a')
        k += a
        s = list(map(ord, s))
        n = len(s)
        i = n - 1  # Start with the last letter
        s[i] += 1  # Increment first
        while i < n:
            if s[i] == k:  # A carry is needed
                if i == 0:  # Cannot carry
                    return ""
                # Carry
                s[i] = a
                i -= 1
                s[i] += 1
            elif i and s[i] == s[i - 1] or i > 1 and s[i] == s[i - 2]:
                s[i] += 1  # If s[i] forms a palindrome with characters to its left, keep incrementing s[i]
            else:
                i += 1  # Move forward to check for palindromes in the suffix
        return ''.join(map(chr, s))
