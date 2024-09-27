import solution
from typing import *
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.takeCharacters(*test_input)

    def takeCharacters(self, s: str, k: int) -> int:
        counter = Counter(s)
        if any(counter[c] < k for c in "abc"):
            return -1
        mx = left = 0
        for right, c in enumerate(s):
            counter[c] -= 1
            while counter[c] < k:
                counter[s[left]] += 1
                left += 1
            mx = max(mx, right - left + 1)
        return len(s) - mx
