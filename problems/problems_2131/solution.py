from collections import Counter
from typing import *

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestPalindrome(test_input)

    def longestPalindrome(self, words: List[str]) -> int:
        s = Counter(words)
        ans = 0
        has_extra = False
        for word, c in s.items():
            if word[0] == word[1]:
                ans += (c // 2) * 4
                has_extra |= c % 2 == 1
            elif word[::-1] in s and word[0] < word[1]:
                ans += min(c, s[word[::-1]]) * 4
        return ans + (2 if has_extra else 0)
