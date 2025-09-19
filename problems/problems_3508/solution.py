import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Router(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class Router:
    def __init__(self, memoryLimit: int):
        pass

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        pass

    def forwardPacket(self) -> List[int]:
        pass

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        pass

