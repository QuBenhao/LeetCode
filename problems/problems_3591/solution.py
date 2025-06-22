import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkPrimeFrequency(test_input)

    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        return any(is_primes[v] for v in counter.values()) if (counter := Counter(nums)) else False

N = 100
is_primes = [True] * (N + 1)
is_primes[0] = is_primes[1] = False
for i in range(2, N + 1):
    if is_primes[i]:
        for j in range(i*i, N+1, i):
            is_primes[j] = False
