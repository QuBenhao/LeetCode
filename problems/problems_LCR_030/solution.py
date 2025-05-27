import random

import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = RandomizedSet()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val_to_index:
            return False
        index = self.val_to_index[val]
        n = len(self.arr) - 1
        self.arr[index], self.arr[n] = self.arr[n], self.arr[index]
        self.val_to_index[self.arr[index]] = index
        self.arr.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randint(0, len(self.arr) - 1)
        return self.arr[idx]
