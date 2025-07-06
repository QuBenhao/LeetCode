from math import gcd

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minStable(*test_input)

    def minStable(self, nums: List[int], maxC: int) -> int:
        n = len(nums)

        gs = []
        for i, num in enumerate(nums):
            gs.append([[v, j] for v, j in gs[i-1]] if i > 0 else [])
            g = gs[i]
            g.append([num, i])
            j = 0
            for p in g:
                p[0] = gcd(p[0], num)
                if g[j][0] != p[0]:
                    j += 1
                    g[j] = p
            del g[j+1:]

        def check(k) -> bool:
            if k == 0:
                return sum(num != 1 for num in nums) <= maxC
            change = 0
            i = n - 1
            while i >= 0:
                for v, j in gs[i][::-1]:
                    if v != 1 and i - j + 1 > k:
                        change += 1
                        if change > maxC:
                            return False
                        i = max(i - k - 1, j - 1)
                        break
                else:
                    i -= 1
            return True

        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
