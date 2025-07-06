import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.validateCoupons(*test_input)

    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        pass

