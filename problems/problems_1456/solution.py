import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxVowels(*test_input)

    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        window = sum(c in vowels for c in s[:k])
        ans = window
        for i in range(k, len(s)):
            window += int(s[i] in vowels) - int(s[i - k] in vowels)
            ans = max(ans, window)
        return ans
