import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.splitArray(test_input)

    def splitArray(self, nums: List[int]) -> int:
        ans = 0
        for i, num in enumerate(nums):
            ans += num if PRIMES[i] else -num
        return abs(ans)

def primes(n):
    n = int(n)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0和1不是质数
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime

PRIMES = primes(1e5)
