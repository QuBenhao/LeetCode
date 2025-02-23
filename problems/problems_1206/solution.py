import random

import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Skiplist()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


MAX_LEVEL = 32
P = 0.25


def random_level() -> int:
    level = 1
    while level < MAX_LEVEL and random.random() < P:
        level += 1
    return level


class SkipNode:

    def __init__(self, value, level=MAX_LEVEL) -> None:
        self.value = value
        self.forward = [None] * level


class Skiplist:

    def __init__(self):
        self.headNode = SkipNode(-1)
        self.level = 0

    def search(self, target: int) -> bool:
        return (node := self.getNode(target).forward[0]) is not None and node.value == target

    def add(self, num: int) -> None:
        update = [self.headNode] * MAX_LEVEL
        self.getNode(num, update)
        level = random_level()
        if level > self.level:
            for i in range(self.level, level):
                update[i] = self.headNode
            self.level = level
        x = SkipNode(num, level)
        for i in range(level):
            x.forward[i] = update[i].forward[i]
            update[i].forward[i] = x

    def erase(self, num: int) -> bool:
        update = [self.headNode] * MAX_LEVEL
        node = self.getNode(num, update).forward[0]
        if node and node.value == num:
            for i in range(self.level):
                if update[i].forward[i] != node:
                    break
                update[i].forward[i] = node.forward[i]
            del node
            while self.level > 0 and not self.headNode.forward[self.level - 1]:
                self.level -= 1
            return True
        return False

    def getNode(self, val: int, update=[]) -> SkipNode:
        node = self.headNode
        for i in range(self.level - 1, -1, -1):
            while node.forward[i] and node.forward[i].value < val:
                node = node.forward[i]
            if update:
                update[i] = node
        return node
