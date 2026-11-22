import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = ProductOfNumbers()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class ProductOfNumbers:
    def __init__(self):
        pass

    def add(self, num: int) -> None:
        pass

    def getProduct(self, k: int) -> int:
        pass

