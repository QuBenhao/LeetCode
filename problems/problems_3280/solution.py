import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.convertDateToBinary(test_input)

    def convertDateToBinary(self, date: str) -> str:
        return "-".join(bin(int(s))[2:] for s in date.split("-"))

