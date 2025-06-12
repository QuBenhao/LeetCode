from math import gcd, inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxGCDScore(*test_input)

    def maxGCDScore(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            # 因子中2的个数最少的及其数量
            lb_min = inf
            used = g = 0
            for j in range(i, -1, -1):
                cur = nums[j]
                lb = cur & -cur
                if lb < lb_min:
                    lb_min = lb
                    used = 1 # 每个元素最多乘2一次, 木桶效应
                elif lb == lb_min:
                    used += 1
                g = gcd(g, cur)
                new_g = g * 2 if used <= k else g
                if (t := new_g * (i - j + 1)) > ans:
                    ans = t
        return ans
