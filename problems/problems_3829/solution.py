from collections import deque, defaultdict

import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = RideSharingSystem()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class RideSharingSystem:
    def __init__(self):
        self.r = deque()
        self.d = deque()
        self.appear = set()
        self.cancel_times = defaultdict(int)

    def addRider(self, riderId: int) -> None:
        self.r.append(riderId)
        self.appear.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.d.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        while self.r:
            if self.cancel_times[self.r[0]] > 0:
                self.cancel_times[self.r.popleft()] -= 1
            elif self.d:
                r = self.r.popleft()
                self.appear.remove(r)
                return [self.d.popleft(), r]
            else:
                break
        return [-1, -1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.appear:
            self.cancel_times[riderId] += 1
