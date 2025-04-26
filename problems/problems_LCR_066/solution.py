import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = MapSum()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for c in key:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c not in cur:
                return 0
            cur = cur[c]
        s = 0
        stack = [cur]
        while stack:
            cur = stack.pop()
            for c in cur:
                if c != '#':
                    stack.append(cur[c])
                else:
                    s += cur[c]
        return s
