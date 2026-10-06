import solution
from functools import lru_cache
from collections import Counter
import math


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.waysToFillArray([x[:] for x in test_input])

    def waysToFillArray(self, queries):
        """
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        # target is at most 10000, so the largest prime factor to try is 97
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        # Prime factorization
        @lru_cache(None)
        def div(num):
            c = Counter()
            for i in primes:
                while num % i == 0:
                    c[i] += 1
                    num //= i
            if num > 1:
                c[num] += 1
            return c

        ans = []
        for l,t in queries:
            count = div(t)
            cur = 1
            # For each prime factor, count ways to distribute v copies among l boxes
            # Identical balls, distinct boxes, empty boxes allowed: C(N+M-1, M-1)
            for v in count.values():
                cur *= math.comb(l+v-1,v)
            ans.append(cur % (10 ** 9 + 7))
        return ans
