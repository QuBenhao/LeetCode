import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximalRectangle(test_input)

    def maximalRectangle(self, matrix: List[str]) -> int:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        # 二维压缩到一维后，就和最大矩形面积一样了
        heights = [0] * (n+1)
        heights[-1] = -1
        max_area = 0
        for i in range(m):
            stack = []
            for j in range(n+1):
                if j < n:
                    if matrix[i][j] == '1':
                        heights[j] += 1
                    else:
                        heights[j] = 0
                while stack and heights[j] < heights[stack[-1]]:
                    height = heights[stack.pop()]
                    width = j if not stack else j - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(j)
        return max_area
