from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minDifference(*test_input)

    def minDifference(self, n: int, k: int) -> List[int]:
        factors = []
        num = n
        for f in PRIME_FACTORS[n]:
            while num % f == 0:
                num //= f
                factors.append(f)

        ans = inf
        result = None
        buckets = [1] * k
        lowest = {p: 0 for p in PRIME_FACTORS[n]}
        def dfs(idx):
            if idx == len(factors):
                nonlocal ans, result
                if (m := max(buckets) - min(buckets)) < ans:
                    ans, result = m, list(buckets)
                return
            for i in range(lowest[factors[idx]], k):
                buckets[i] *= factors[idx]
                tmp = lowest[factors[idx]]
                lowest[factors[idx]] = i
                dfs(idx + 1)
                buckets[i] //= factors[idx]
                lowest[factors[idx]] = tmp
            return

        dfs(0)
        return result


# Precompute the prime factor list for each number
mx = 100001
PRIME_FACTORS = [[] for _ in range(mx)]
for i in range(2, mx):
    if not PRIME_FACTORS[i]:  # i is prime
        for j in range(i, mx, i):  # Multiples of i have prime factor i
            PRIME_FACTORS[j].append(i)
