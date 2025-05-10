from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(test_input)

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        left_idx = [-1] * n
        right_idx = [n] * n
        min_stack = []
        for i, num in enumerate(nums):
            while min_stack and num < nums[min_stack[-1]]:
                idx = min_stack.pop()
                right_idx[idx] = i
            if num == 0:
                left_idx[i] = inf
            min_stack.append(i)
        min_stack = []
        for i in range(n-1, -1, -1):
            num = nums[i]
            while min_stack and num < nums[min_stack[-1]]:
                idx = min_stack.pop()
                left_idx[idx] = i
            min_stack.append(i)
        return len(set((l, r) for l, r in zip(left_idx, right_idx) if l != inf))
