import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.hammingWeight(test_input)

    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count

        # return bin(n).count('1')
