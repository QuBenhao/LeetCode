import solution
from typing import *
from math import gcd
from itertools import accumulate


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.gcdSum(test_input)

    def gcdSum(self, nums: list[int]) -> int:
        pg = sorted(gcd(x, mx) for x, mx in zip(nums, accumulate(nums, max)))
        i, j = 0, len(pg) - 1
        ans = 0
        while i < j:
            ans += gcd(pg[i], pg[j])
            i += 1
            j -= 1
        return ans

