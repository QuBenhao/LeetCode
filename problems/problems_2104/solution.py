import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.subArrayRanges(test_input)

    def subArrayRanges(self, nums: List[int]) -> int:
        def pop_stack(stack, i):
            idx = stack.pop()
            left = stack[-1] if stack else -1
            return (i - idx) * (idx - left) * nums[idx]

        ans = 0
        max_stack = []
        min_stack = []
        for i, num in enumerate(nums):
            while max_stack and num > nums[max_stack[-1]]:
                ans += pop_stack(max_stack, i)
            max_stack.append(i)
            while min_stack and num < nums[min_stack[-1]]:
                ans -= pop_stack(min_stack, i)
            min_stack.append(i)
        while max_stack:
            ans += pop_stack(max_stack, len(nums))
        while min_stack:
            ans -= pop_stack(min_stack, len(nums))
        return ans
