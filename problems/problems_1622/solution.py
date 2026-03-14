import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Fancy()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class Fancy:
    def __init__(self):
        self.mul = 1
        self.add = 0
        self.arr = []

    def append(self, val: int) -> None:
        self.arr.append((val - self.add) * pow(self.mul, -1, MOD) % MOD)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % MOD
        self.add = (self.add * m) % MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        return (self.mul * self.arr[idx] % MOD + self.add) % MOD

MOD = 10 ** 9 + 7
