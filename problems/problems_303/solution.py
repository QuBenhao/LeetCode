import solution
from typing import *
import itertools
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        operations, inputs = test_input
        obj = NumArray(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(operations[1:], inputs[1:])]


class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sum = [0] + list(itertools.accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right + 1] - self.pre_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
