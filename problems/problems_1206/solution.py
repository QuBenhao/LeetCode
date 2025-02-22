import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Skiplist()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class Skiplist:
    def __init__(self):
        pass

    def search(self, target: int) -> bool:
        pass

    def add(self, num: int) -> None:
        pass

    def erase(self, num: int) -> bool:
        pass

