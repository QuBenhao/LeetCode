import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = ZigzagIterator(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
            pass
        

    def next(self) -> int:
        pass
        

    def hasNext(self) -> bool:
        pass
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())