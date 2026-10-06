from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.validSubstringCount(*test_input)

    def validSubstringCount(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0

        # Difference between letter counts in t and s
        diff = defaultdict(int)  # Counter(t) also works, but is much slower
        for c in t:
            diff[c] += 1

        # less counts the letters that occur fewer times in the window than in t
        less = len(diff)

        ans = left = 0
        for c in s:
            diff[c] -= 1
            if diff[c] == 0:
                # After c enters the window, its count matches the count in t
                less -= 1
            while less == 0:  # The window meets the requirements
                if diff[s[left]] == 0:
                    # Before removing s[left] from the window, check its count:
                    # If s[left] occurs as many times in the window as in t,
                    # removing it will leave fewer occurrences in the window than in t
                    less += 1
                diff[s[left]] += 1
                left += 1
            ans += left
        return ans


