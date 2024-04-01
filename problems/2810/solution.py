import solution
from typing import *
from collections import deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.finalString(test_input)

    def finalString(self, s: str) -> str:
        ans, tail = deque([]), True
        for c in s:
            if c == 'i':
                tail = not tail
            elif tail:
                ans.append(c)
            else:
                ans.appendleft(c)
        return "".join(ans if tail else reversed(ans))
