import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.processStr(test_input)

    def processStr(self, s: str) -> str:
        result = []
        for c in s:
            if c.isalpha():
                result.append(c)
            elif c == '#':
                result += result
            elif c == '%':
                result = result[::-1]
            elif result:
                result.pop()
        return "".join(result)
