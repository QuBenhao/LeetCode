import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallestRepunitDivByK(test_input)

    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        ans, cur = 1, 1
        while cur % k != 0:
            cur = ((10 % k) * cur + 1) % k
            ans += 1
        return ans
