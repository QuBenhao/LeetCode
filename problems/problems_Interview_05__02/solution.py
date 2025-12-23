import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.printBin(test_input)

    def printBin(self, num: float) -> str:
        s = ["0."]
        for _ in range(6):  # 至多循环 6 次
            num *= 2
            if num < 1:
                s.append('0')
            else:
                s.append('1')
                num -= 1
                if num == 0:
                    return ''.join(s)
        return "ERROR"
