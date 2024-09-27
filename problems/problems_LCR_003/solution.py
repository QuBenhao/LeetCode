import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countBits(test_input)

    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n + 1):
            ans.append(ans[i >> 1] + (i & 1))
        return ans
