import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countOperations(*test_input)

    def countOperations(self, num1: int, num2: int) -> int:
        if num1 == 0 or num2 == 0:
            return 0
        if num1 < num2:
            num1, num2 = num2, num1
        return num1 // num2 + self.countOperations(num2, num1 % num2)
