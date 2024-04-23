import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxSatisfied(*test_input)

    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total = cur = ans = 0
        for i, (c, g) in enumerate(zip(customers, grumpy)):
            if g:
                cur += c
            else:
                total += c
            if i >= minutes:
                if grumpy[i - minutes]:
                    cur -= customers[i - minutes]
                ans = max(ans, cur)
            else:
                ans = cur
        return ans + total
