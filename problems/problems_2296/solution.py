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
        self.left = []  # Characters to the left of the cursor
        self.right = []  # Characters to the right of the cursor

    def addText(self, text: str) -> None:
        self.left.extend(text)  # Push onto the stack

    def deleteText(self, k: int) -> int:
        pre = len(self.left)  # Stack size before deletion
        del self.left[-k:]  # Pop from the stack
        return pre - len(self.left)  # Subtract the stack size after deletion

    def text(self) -> str:
        return ''.join(self.left[-10:])  # At most 10 characters to the left of the cursor

    def cursorLeft(self, k: int) -> str:
        while k and self.left:
            self.right.append(self.left.pop())  # Move from the left stack to the right stack
            k -= 1
        return self.text()

    def cursorRight(self, k: int) -> str:
        while k and self.right:
            self.left.append(self.right.pop())  # Move from the right stack to the left stack
            k -= 1
        return self.text()
