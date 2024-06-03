import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.lemonadeChange(test_input)

    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                tens += 1
                fives -= 1
            elif tens:
                tens -= 1
                fives -= 1
            else:
                fives -= 3
            if fives < 0:
                return False
        return True
