import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.accountBalanceAfterPurchase(test_input)

    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - (purchaseAmount + 5) // 10 * 10
