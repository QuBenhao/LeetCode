from math import gcd

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(test_input)

    def minOperations(self, nums: List[int]) -> int:
        if gcd(*nums) > 1:
            return -1
        n = len(nums)
        cnt1 = sum(x == 1 for x in nums)
        if cnt1:
            return n - cnt1

        min_size = n
        a = []  # [GCD, right endpoint of the inclusive interval sharing this GCD]
        for i, x in enumerate(nums):
            a.append([x, i])

            # Deduplicate in place, since equal GCD values are adjacent
            j = 0
            for p in a:
                p[0] = gcd(p[0], x)
                if a[j][0] != p[0]:
                    j += 1
                    a[j] = p
                else:
                    a[j][1] = p[1]
            del a[j + 1:]

            if a[0][0] == 1:
                # This was i-a[0][1]+1; move the +1 into the return expression
                min_size = min(min_size, i - a[0][1])
        return min_size + n - 1
