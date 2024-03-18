import solution
from typing import *
import itertools


class Solution(solution.Solution):
    def solve(self, test_input=None):
        _, inputs = test_input
        obj = NumArray(inputs[0][0])
        ans = [None]
        for i in inputs[1:]:
            ans.append(obj.sumRange(i[0], i[1]))
        return ans


class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sum = [0] + list(itertools.accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right + 1] - self.pre_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
