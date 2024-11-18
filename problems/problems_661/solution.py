import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.imageSmoother(test_input)

    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                count = 0
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < m and 0 <= y < n:
                            ans[i][j] += img[x][y]
                            count += 1
                ans[i][j] //= count
        return ans
