import solution
from typing import *
from python.object_libs import call_method
from itertools import accumulate
from random import randint
from bisect import bisect_left
from python.object_libs import call_method

class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = S(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class S:
    def __init__(self, w):
        """
        :type w: List[int]
        """
        # 计算前缀和，这样可以生成一个随机数，根据数的大小对应分布的坐标
        self.presum = list(accumulate(w))

    def pickIndex(self):
        """
        :rtype: int
        """
        return bisect_left(self.presum, randint(1, self.presum[-1]))
