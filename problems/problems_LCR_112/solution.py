from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestIncreasingPath(test_input)

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(matrix), len(matrix[0])
        max_length = [[0] * n for _ in range(m)]
        idx_map = defaultdict(list)
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                idx_map[val].append((i, j))
        ans = 0
        for val in sorted(idx_map.keys()):
            for i, j in idx_map[val]:
                for d in dirs:
                    if 0 <= (ni := i + d[0]) < m and 0 <= (nj := j + d[1]) < n and matrix[ni][nj] < matrix[i][j]:
                        max_length[i][j] = max(max_length[i][j], max_length[ni][nj])
                max_length[i][j] += 1
                ans = max(ans, max_length[i][j])
        return ans
