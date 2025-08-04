import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Robot(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

DIRS_STR = ["East", "North", "West", "South"]
class Robot:
    __slots__ = ["m", "n", "total", "loc", "moved"]
    def __init__(self, width: int, height: int):
        self.m = width
        self.n = height
        self.total = (width - 1) * 2 + (height - 1) * 2
        self.loc = 0
        self.moved = False

    def step(self, num: int) -> None:
        num %= self.total
        self.loc = (self.loc + num) % self.total
        self.moved = True

    def getPos(self) -> List[int]:
        x, y, _ = self.__move()
        return [x, y]

    def getDir(self) -> str:
        _, _, d = self.__move()
        return DIRS_STR[d]

    def __move(self) -> Tuple[int, int, int]:
        if not self.moved:
            return 0, 0, 0
        if self.loc < self.m:
            return self.loc, 0, 0 if self.loc else 3
        if self.loc < self.m + self.n - 1:
            return self.m - 1, self.loc - (self.m - 1), 1
        if self.loc < self.m * 2 + self.n - 2:
            return (self.m - 1 - (self.loc - self.m - self.n + 2)), self.n - 1, 2
        return 0, self.total - self.loc, 3
