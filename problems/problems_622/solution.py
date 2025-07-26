import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = MyCircularQueue(inputs[0][0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class MyCircularQueue:
    def __init__(self, k: int):
        self.arr = [-1] * k
        self.idx = 0
        self.size = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.size == self.k:
            return False
        self.arr[self.idx] = value
        self.idx = (self.idx + 1) % self.k
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.arr[(self.idx - self.size + self.k) % self.k]

    def Rear(self) -> int:
        if self.size == 0:
            return -1
        return self.arr[self.idx - 1]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k

