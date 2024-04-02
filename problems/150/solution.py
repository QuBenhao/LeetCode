import solution
from typing import *
import operator


op_dict = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.evalRPN(test_input)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s in op_dict:
                b, a = stack.pop(), stack.pop()
                stack.append(int(op_dict[s](a, b)))
            else:
                stack.append(int(s))
        return stack[-1]
