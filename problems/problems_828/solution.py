from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.uniqueLetterString(test_input)

    def uniqueLetterString(self, s: str) -> int:
        grp = defaultdict(list)
        for i, c in enumerate(s):
            grp[c].append(i)
        ans = 0
        n = len(s)
        for indexes in grp.values():
            indexes = [-1] + indexes + [n]
            for i in range(1, len(indexes) - 1):
                ans += (indexes[i] - indexes[i - 1]) * (indexes[i + 1] - indexes[i])
        return ans
