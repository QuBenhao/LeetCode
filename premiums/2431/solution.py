import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxTastiness(*test_input)

    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
                pass