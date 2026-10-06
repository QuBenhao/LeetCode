import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.makeLargestSpecial(test_input)

    def makeLargestSpecial(self, s: str) -> str:
        # cur: prefix sum; last: the end of the previous special sequence
        cur = last = 0
        # All available special subsequences
        candidates = []
        for i, c in enumerate(s):
            cur += 1 if c == '1' else -1
            # A special sequence must start with 1 and end with 0
            if not cur:
                # Maximize the current special sequence first; its fixed endpoints remain 1 and 0, so recurse on the interior
                candidates.append('1' + self.makeLargestSpecial(s[last + 1:i]) + '0')
                last = i + 1
        # Special subsequences can be swapped any number of times, so sort them in descending order and concatenate
        return "".join(sorted(candidates, reverse=True))
