import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countMonobit(test_input)

    def countMonobit(self, n: int) -> int:
        return COUNTS[n]

COUNTS = [0] * 1001
COUNTS[0] = 1
for i in range(1, 1001):
    COUNTS[i] = COUNTS[i - 1]
    if (i + 1) & (-i - 1) == i + 1:
        COUNTS[i] += 1