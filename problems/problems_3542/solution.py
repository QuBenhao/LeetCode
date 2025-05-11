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
        strict_min_stack = []
        for i, num in enumerate(nums):
            while min_stack and num < nums[min_stack[-1]]:
                idx = min_stack.pop()
                right_idx[idx] = i
            while strict_min_stack and num <= nums[strict_min_stack[-1]]:
                strict_min_stack.pop()
            if num == 0:
                left_idx[i] = inf
            else:
                left_idx[i] = strict_min_stack[-1] if strict_min_stack else -1
            min_stack.append(i)
            strict_min_stack.append(i)
        return len(set((l, r) for l, r in zip(left_idx, right_idx) if l != inf))
