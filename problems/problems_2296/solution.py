import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = TextEditor()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class TextEditor:
    def __init__(self):
        pass

    def addText(self, text: str) -> None:
        pass

    def deleteText(self, k: int) -> int:
        pass

    def cursorLeft(self, k: int) -> str:
        pass

    def cursorRight(self, k: int) -> str:
        pass

