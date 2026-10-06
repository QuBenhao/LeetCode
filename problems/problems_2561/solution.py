from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCost(*test_input)

    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        # The baskets must match exactly, not just in sum, so each value must occur an even number of times; matching occurrences in both baskets can be ignored
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
        return sum(min(x, mn * 2) for x in nums[:len(nums) // 2])  # Swap the two values directly, or use the minimum value for two swaps; take the smaller cost
