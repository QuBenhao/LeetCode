from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getLeastFrequentDigit(test_input)

    def getLeastFrequentDigit(self, n: int) -> int:
        counts = [0] * 10
        while n:
            counts[n % 10] += 1
            n //= 10
        ans = -1
        for i in range(10):
            if counts[i] == 0:
                continue
            if ans == -1 or counts[i] < counts[ans]:
                ans = i
        return ans

