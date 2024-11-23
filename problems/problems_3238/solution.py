from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.winningPlayerCount(*test_input)

    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        counter = [defaultdict(int) for _ in range(n)]
        for i, pk in pick:
            counter[i][pk] += 1
        return sum(any(v > i for v in counter[i].values()) for i in range(n))
