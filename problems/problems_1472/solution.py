import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = BrowserHistory(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class BrowserHistory:
    def __init__(self, homepage: str):
        self.b = [homepage]
        self.f = []

    def visit(self, url: str) -> None:
        self.b.append(url)
        self.f.clear()

    def back(self, steps: int) -> str:
        for _ in range(min(steps, len(self.b) - 1)):
            self.f.append(self.b.pop())
        return self.b[-1]

    def forward(self, steps: int) -> str:
        for _ in range(min(steps, len(self.f))):
            self.b.append(self.f.pop())
        return self.b[-1]
