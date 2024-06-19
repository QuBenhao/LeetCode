import solution
from typing import *
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxIncreasingCells(test_input)

    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, row in enumerate(mat):
            for j, v in enumerate(row):
                graph[v].append((i, j))
        row_max = [0] * len(mat)
        col_max = [0] * len(mat[0])
        for _, pos in sorted(graph.items(), key=lambda p:p[0]):
            mx = [max(row_max[i], col_max[j]) + 1 for i, j in pos]
            for (i, j), m in zip(pos, mx):
                row_max[i] = max(row_max[i], m)
                col_max[j] = max(col_max[j], m)
        return max(row_max)
