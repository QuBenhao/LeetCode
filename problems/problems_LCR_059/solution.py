import solution
from typing import *
from python.object_libs import call_method
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = KthLargest(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = []
        self.k = k
        heapq.heapify(self.nums)
        for num in nums:
            heapq.heappush(self.nums, num)
            if len(self.nums) > k:
                heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
