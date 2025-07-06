import string
from collections import deque

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.concatHex36(test_input)

    def concatHex36(self, n: int) -> str:
        x, y = n ** 2, n ** 3
        ans = deque()
        while y:
            ans.appendleft(S[y % 36])
            y //= 36
        while x:
            ans.appendleft(S[x % 16])
            x //= 16
        return ''.join(ans)

S = string.digits + string.ascii_uppercase