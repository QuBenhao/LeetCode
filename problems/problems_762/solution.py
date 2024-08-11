import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countPrimeSetBits(*test_input)

    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(i.bit_count() in primes for i in range(left, right + 1))
