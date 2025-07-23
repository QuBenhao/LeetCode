import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.solveEquation(test_input)

    def solveEquation(self, equation: str) -> str:
        k, d = 0, 0
        cur = 0
        sign = 1
        last = '1'
        for c in equation:
            if c.isdigit():
                cur = cur * 10 + int(c)
            else:
                if c == 'x':
                    if last != '0' and cur == 0:
                        cur = 1
                    k += sign * cur
                else:
                    d += sign * cur
                    match c:
                        case '=':
                            d *= -1
                            k *= -1
                            sign = 1
                        case '+':
                            sign = 1
                        case '-':
                            sign = -1
                cur = 0
            last = c
        d += sign * cur
        if k == 0:
            return "Infinite solutions" if d == 0 else "No solution"
        return f"x={-d // k}"
