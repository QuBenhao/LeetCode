import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = BoundedBlockingQueue(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        pass
        

    def enqueue(self, element: int) -> None:
            pass
        

    def dequeue(self) -> int:
        pass
        

    def size(self) -> int:
        pass
        