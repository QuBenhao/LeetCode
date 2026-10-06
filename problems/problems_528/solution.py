import solution
from itertools import accumulate
from random import randint
from bisect import bisect_left
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = RandomPick(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class RandomPick:
    def __init__(self, w):
        """
        :type w: List[int]
        """
        # Compute prefix sums to map a random number to the index of its weighted interval
        self.presum = list(accumulate(w))

    def pickIndex(self):
        """
        :rtype: int
        """
        return bisect_left(self.presum, randint(1, self.presum[-1]))
