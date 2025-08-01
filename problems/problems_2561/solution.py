from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCost(*test_input)

    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # 要求完全相同，不只是和相等，所以每个数要出现偶数次，两个里面已经相同的可以直接忽略
        count = defaultdict(int)
        for a, b in zip(basket1, basket2):
            count[a] += 1
            count[b] -= 1

        nums = []
        for x, c in count.items():
            if c % 2 != 0:
                return -1
            nums.extend([x] * (abs(c) // 2))

        nums.sort()
        mn = min(count)
        return sum(min(x, mn * 2) for x in nums[:len(nums) // 2])  # 两个数可以交换，或者用最小的数替换两个数，所以取最小的
