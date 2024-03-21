import solution
from typing import *
from object_libs import call_method
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = FrequencyTracker()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class FrequencyTracker:

    def __init__(self):
        self.counter = Counter()
        self.freq = Counter()

    def add(self, number: int) -> None:
        self.freq[self.counter[number]] -= 1
        self.counter[number] += 1
        self.freq[self.counter[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.counter:
            self.freq[self.counter[number]] -= 1
            self.counter[number] -= 1
            self.freq[self.counter[number]] += 1
            if not self.counter[number]:
                self.counter.pop(number)

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
