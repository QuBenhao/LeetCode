import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.spiralOrder(test_input)

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        ans = []
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                ans.append(matrix[top][col])
            for row in range(top + 1, bottom + 1):
                ans.append(matrix[row][right])
            if left < right and top < bottom:
                for col in range(right - 1, left - 1, -1):
                    ans.append(matrix[bottom][col])
                for row in range(bottom - 1, top, -1):
                    ans.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return ans
