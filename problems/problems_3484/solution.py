from collections import defaultdict

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
        self.map = [defaultdict(int) for _ in range(26)]

    def setCell(self, cell: str, value: int) -> None:
        self.map[ord(cell[0]) - ord('A')][cell] = value

    def resetCell(self, cell: str) -> None:
        self.map[ord(cell[0]) - ord('A')][cell] = 0

    def getValue(self, formula: str) -> int:
        def get_val(cell: str) -> int:
            return self.map[ord(cell[0]) - ord('A')][cell]

        formula = formula.split("=")[1]
        x1, x2 = formula.split("+")
        if x1[0].isalpha():
            v1 = get_val(x1)
        else:
            v1 = int(x1)
        if x2[0].isalpha():
            v2 = get_val(x2)
        else:
            v2 = int(x2)
        return v1 + v2
