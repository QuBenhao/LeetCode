import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxChunksToSorted(test_input)

    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for num in arr:
            if stack and num < stack[-1]:
                mx = stack.pop()
                while stack and num < stack[-1]:
                    stack.pop()
                stack.append(mx)
            else:
                stack.append(num)
        return len(stack)
