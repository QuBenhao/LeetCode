import solution
from typing import *
from math import gcd


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.subsequencePairCount(test_input)

    def subsequencePairCount(self, nums: List[int]) -> int:
        # dp[ga * 201 + gb]: #ways with current gcd(seq1)=ga, gcd(seq2)=gb
        # ga=0 / gb=0 means the sequence is still empty
        dp = [0] * (201 * 201)
        dp[0] = 1
        for x in nums:
            ndp = dp[:]
            for ga in range(201):
                row = ga * 201
                for gb in range(201):
                    c = dp[row + gb]
                    if c == 0:
                        continue
                    # put x into seq1
                    nga = gcd(ga, x)
                    ndp[nga * 201 + gb] = (ndp[nga * 201 + gb] + c) % MOD
                    # put x into seq2
                    ngb = gcd(gb, x)
                    ndp[ga * 201 + ngb] = (ndp[ga * 201 + ngb] + c) % MOD
            dp = ndp
        ans = 0
        for g in range(1, 201):
            ans = (ans + dp[g * 201 + g]) % MOD
        return ans


MOD = 10 ** 9 + 7
