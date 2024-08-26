import solution
from typing import *
from python.object_libs import call_method
from collections import deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = RecentCounter()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        self.queue.append(t)
        return len(self.queue)
