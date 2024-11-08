import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = NeighborSum(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class NeighborSum:
    def __init__(self, grid: List[List[int]]):
        pass

    def adjacentSum(self, value: int) -> int:
        pass

    def diagonalSum(self, value: int) -> int:
        pass

