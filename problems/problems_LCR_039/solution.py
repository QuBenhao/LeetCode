import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestRectangleArea(test_input)

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        while stack:
            height = heights[stack.pop()]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)
        return max_area

