import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxDiff(test_input)

    def maxDiff(self, num: int) -> int:
        s = str(num)
        idx = 0
        while idx < len(s) and s[idx] == '9':
            idx += 1
        if idx == len(s):
            mx = num
        else:
            mx = int(s.replace(s[idx], '9'))
        if s[0] == '1':
            idx = 1
            while idx < len(s) and (s[idx] == '0' or s[idx] == s[0]):
                idx += 1
            if idx == len(s):
                mn = num
            else:
                mn = int(s.replace(s[idx], '0'))
        else:
            mn = int(s.replace(s[0], '1'))
        return mx - mn
