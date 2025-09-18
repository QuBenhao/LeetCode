import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Spreadsheet(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class Spreadsheet:
    def __init__(self, rows: int):
        pass

    def setCell(self, cell: str, value: int) -> None:
        pass

    def resetCell(self, cell: str) -> None:
        pass

    def getValue(self, formula: str) -> int:
        pass

