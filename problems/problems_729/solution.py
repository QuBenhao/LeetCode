import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = MyCalendar()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class MyCalendar:
    def __init__(self):
        self.intervals = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.intervals:
            if start < endTime and startTime < end:
                return False
        self.intervals.append((startTime, endTime))
        return True
