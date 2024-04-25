import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.distanceTraveled(*test_input)

    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        return (mainTank + min((mainTank - 1) // 4, additionalTank)) * 10
