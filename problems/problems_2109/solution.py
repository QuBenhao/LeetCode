from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.addSpaces(*test_input)

    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        spaces = [0] + spaces + [len(s)]
        for a, b in pairwise(spaces):
            ans.append(s[a:b])
        return " ".join(ans)
