import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.confusingNumber(test_input)

    def confusingNumber(self, n: int) -> bool:
        trans = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        revert, num = 0, n
        while num:
            cur = num % 10
            if cur not in trans:
                return False
            revert = 10 * revert + trans[cur]
            num //= 10
        return revert != n
