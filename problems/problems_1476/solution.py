import solution
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = SubrectangleQueries(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class SubrectangleQueries:

    def __init__(self, rectangle):
        self.sub_rectangle = rectangle
        self.history = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.history.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        for i in range(len(self.history) - 1, -1, -1):
            r1, c1, r2, c2, new_value = self.history[i]
            if r1 <= row <= r2 and c1 <= col <= c2:
                return new_value
        return self.sub_rectangle[row][col]
