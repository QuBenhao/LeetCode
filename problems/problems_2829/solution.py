import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumSum(*test_input)

    def minimumSum(self, n: int, k: int) -> int:
        explored = set()
        ans, cur = 0, 1
        for _ in range(n):
            while cur < k and k - cur in explored:
                cur += 1
                continue
            ans += cur
            explored.add(cur)
            cur += 1
        return ans
