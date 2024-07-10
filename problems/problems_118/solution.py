import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.generate(test_input)

    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            row = [1] * (i + 1)
            for j in range(1, i // 2 + 1):
                row[j] = row[i - j] = ans[i - 1][j - 1] + ans[i - 1][j]
            ans.append(row)
        return ans
