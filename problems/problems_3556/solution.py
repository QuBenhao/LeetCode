import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sumOfLargestPrimes(test_input)

    def sumOfLargestPrimes(self, s: str) -> int:
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        primes = set()
        n = len(s)

        for i in range(n):
            num = 0
            for j in range(i, n):
                num = num * 10 + int(s[j])
                if num > 1 and is_prime(num):
                    primes.add(num)

        largest_primes = sorted(primes, reverse=True)[:3]
        return sum(largest_primes)        
