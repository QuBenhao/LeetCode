from collections import deque

import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = MovingAverage(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.s = 0
        self.size = size
        self.window = deque(maxlen=size)

    def next(self, val: int) -> float:
        if len(self.window) == self.size:
            self.s -= self.window.popleft()
        self.s += val
        self.window.append(val)
        return self.s / len(self.window)
