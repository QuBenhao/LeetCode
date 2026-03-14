import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Fancy()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class Fancy:
    def __init__(self):
        pass

    def append(self, val: int) -> None:
        pass

    def addAll(self, inc: int) -> None:
        pass

    def multAll(self, m: int) -> None:
        pass

    def getIndex(self, idx: int) -> int:
        pass

