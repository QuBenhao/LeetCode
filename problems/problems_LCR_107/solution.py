import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.updateMatrix(test_input)

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[0x3f3f3f3f] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                if i > 0:
                    ans[i][j] = min(ans[i][j], ans[i-1][j] + 1)
                if j > 0:
                    ans[i][j] = min(ans[i][j], ans[i][j-1] + 1)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i < m-1:
                    ans[i][j] = min(ans[i][j], ans[i+1][j] + 1)
                if j < n-1:
                    ans[i][j] = min(ans[i][j], ans[i][j+1] + 1)
        return ans
