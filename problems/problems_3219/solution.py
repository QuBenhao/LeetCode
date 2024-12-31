import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumCost(*test_input)

    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort()
        verticalCut.sort()
        ans = i = j = 0
        for _ in range(m + n - 2):
            if j == n - 1 or i < m - 1 and horizontalCut[i] < verticalCut[j]:
                ans += horizontalCut[i] * (n - j)  # 上下连边
                i += 1
            else:
                ans += verticalCut[j] * (m - i)  # 左右连边
                j += 1
        return ans
