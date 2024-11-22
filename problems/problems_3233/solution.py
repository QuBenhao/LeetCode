import solution
from typing import *
import math


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.nonSpecialCount(*test_input)

    def nonSpecialCount(self, l: int, r: int) -> int:
        n = int(math.sqrt(r))
        v = [0] * (n + 1)
        res = r - l + 1
        for i in range(2, n + 1):
            if v[i] == 0:
                if l <= i * i <= r:
                    res -= 1
                for j in range(i * 2, n + 1, i):
                    v[j] = 1
        return res

