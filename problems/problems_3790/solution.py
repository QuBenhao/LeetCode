import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minAllOneMultiple(test_input)

    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        cur = 0
        for i in range(k):
            cur = (cur * 10 + 1) % k
            if cur == 0:
                return i + 1
        return -1
