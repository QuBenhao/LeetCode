import solution
from typing import *
from python.object_libs import call_method
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = RecentCounter()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class RecentCounter:
    def __init__(self):
        self.pq = []

    def ping(self, t: int) -> int:
        heapq.heappush(self.pq, t)
        while self.pq[0] < t - 3000:
            heapq.heappop(self.pq)
        return len(self.pq)
