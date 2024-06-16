import solution
from typing import *
from collections import deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.addBinary(*test_input)

    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            a, b = b, a
        ans, cur = deque([]), 0
        for i in range(len(b) - 1, -1, -1):
            cur += int(a[i + len(a) - len(b)]) + int(b[i])
            ans.appendleft(f"{cur % 2}")
            cur //= 2
        for i in range(len(a) - len(b) - 1, -1, -1):
            cur += int(a[i])
            ans.appendleft(f"{cur % 2}")
            cur //= 2
        if cur:
            ans.appendleft(f"{cur}")
        return "".join(ans)
