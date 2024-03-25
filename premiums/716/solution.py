import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = MaxStack()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class MaxStack:

    def __init__(self):
        pass


    def push(self, x: int) -> None:
            pass


    def pop(self) -> int:
        pass


    def top(self) -> int:
        pass


    def peekMax(self) -> int:
        pass


    def popMax(self) -> int:
        pass



# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()