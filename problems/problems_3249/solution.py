from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countGoodNodes(test_input)

    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ans = 0

        def dfs(x: int, fa: int) -> int:
            size, sz0, ok = 1, 0, True
            for y in g[x]:
                if y == fa:
                    continue  # 不能递归到父节点
                sz = dfs(y, x)
                if sz0 == 0:
                    sz0 = sz  # 记录第一个儿子子树的大小
                elif sz != sz0:  # 存在大小不一样的儿子子树
                    ok = False  # 注意不能 break，其他子树 y 仍然要递归
                size += sz
            nonlocal ans
            ans += ok
            return size

        dfs(0, -1)
        return ans
