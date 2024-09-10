import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.addBinary(*test_input)

    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            a, b = b, a
        ans = []
        add = 0
        d = len(b) - len(a)
        for i in range(len(b) - 1, -1, -1):
            s = int(b[i]) + add + (int(a[i - d]) if i >= d else 0)
            add = s // 2
            ans.append(str(s % 2))
        if add:
            ans.append('1')
        return "".join(ans[::-1])
