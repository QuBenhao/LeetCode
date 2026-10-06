import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sumFourDivisors(test_input)

    def sumFourDivisors(self, nums: List[int]) -> int:
        return sum(FACTORS_SUM[num] for num in nums if FACTORS_COUNT[num] == 4)

# Precompute the list of prime factors for each number
mx = 100001
FACTORS_COUNT = [0] * mx
FACTORS_SUM = [0] * mx
for i in range(1, mx):
    for j in range(i, mx, i):  # i is a divisor
        FACTORS_COUNT[j] += 1
        FACTORS_SUM[j] += i
