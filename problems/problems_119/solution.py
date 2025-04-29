from functools import cache
from typing import *

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getRow(test_input)

    @cache
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        last_row = list(self.getRow(rowIndex - 1))
        for i in range(rowIndex // 2, 0, -1):
            last_row[i] += last_row[i - 1]
        for i in range((rowIndex // 2) + 1, rowIndex):
            last_row[i] = last_row[rowIndex - i]
        last_row.append(1)
        return last_row
