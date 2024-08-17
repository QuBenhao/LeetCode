import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.evalRPN(test_input)

    def evalRPN(self, tokens: List[str]) -> int:
        values = []
        for token in tokens:
            if token in "+-*/":
                b, a = values.pop(), values.pop()
                if token == "+":
                    values.append(a + b)
                elif token == "-":
                    values.append(a - b)
                elif token == "*":
                    values.append(a * b)
                else:
                    values.append(int(a / b))
            else:
                values.append(int(token))
        return values[0]
