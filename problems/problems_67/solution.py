from itertools import zip_longest

import solution
from typing import *
from collections import deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.addBinary(*test_input)

    def addBinary(self, a: str, b: str) -> str:
        add = 0
        ans = []
        for x, y in zip_longest(reversed(a), reversed(b)):
            cur = int(x if x else 0) + int(y if y else 0) + add
            cur, add = cur % 2, 1 if cur > 1 else 0
            ans.append(str(cur))
        if add:
            ans.append(str(add))
        return ''.join(reversed(ans))
