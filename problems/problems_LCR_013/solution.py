import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = NumMatrix(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        pass

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pass

