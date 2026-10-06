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
                    continue  # Do not recurse into the parent
                sz = dfs(y, x)
                if sz0 == 0:
                    sz0 = sz  # Record the size of the first child's subtree
                elif sz != sz0:  # A child's subtree has a different size
                    ok = False  # Do not break; the other subtrees y must still be traversed recursively
                size += sz
            nonlocal ans
            ans += ok
            return size

        dfs(0, -1)
        return ans
