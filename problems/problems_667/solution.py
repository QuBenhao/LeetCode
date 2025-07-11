import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.constructArray(*test_input)

    def constructArray(self, n: int, k: int) -> List[int]:
        ans = []
        for i in range(k + 1):
            if i % 2 == 0:
                ans.append(i // 2 + 1)
            else:
                ans.append(k - i // 2 + 1)
        for i in range(k + 2, n + 1):
            ans.append(i)
        return ans
