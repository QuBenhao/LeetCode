import solution
from typing import *
from collections import deque


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(solution.Solution):
    def solve(self, test_input=None):
        res = []
        root = self.construct(test_input)
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    res.append([node.isLeaf, node.val])
                    q.append(node.topLeft)
                    q.append(node.topRight)
                    q.append(node.bottomLeft)
                    q.append(node.bottomRight)
                else:
                    res.append(None)
        while res and res[-1] is None:
            res.pop()
        return res

    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        pre_sum = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                pre_sum[i + 1][j + 1] = pre_sum[i + 1][j] + pre_sum[i][j + 1] - pre_sum[i][j] + grid[i][j]

        def dfs(x0, y0, x1, y1):
            if (diff := pre_sum[x1][y1] - pre_sum[x1][y0] - pre_sum[x0][y1] + pre_sum[x0][y0]) == 0:
                return Node(False, True, None, None, None, None)
            elif diff == (x1 - x0) * (y1 - y0):
                return Node(True, True, None, None, None, None)
            else:
                return Node(True, False,
                            dfs(x0, y0, hx := (x1 + x0) // 2, hy := (y1 + y0) // 2),
                            dfs(x0, hy, hx, y1),
                            dfs(hx, y0, x1, hy),
                            dfs(hx, hy, x1, y1))

        return dfs(0, 0, n, n)
