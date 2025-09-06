import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sumZero(test_input)

    def sumZero(self, n: int) -> List[int]:
        ans = [0] * n
        for i in range(n // 2):
            ans[i * 2] = -(i + 1)
            ans[i * 2 + 1] = i + 1
        return ans
