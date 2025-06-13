import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minMaxDifference(test_input)

    def minMaxDifference(self, num: int) -> int:
        mx = num
        s = str(num)
        for c in s:
            if c != '9':
                mx = int(s.replace(c, '9'))
                break
        return mx - int(s.replace(s[0], '0'))
