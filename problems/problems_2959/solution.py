import solution
from typing import *
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfSets(*test_input)

    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        g = [[inf] * n for _ in range(n)]
        for i in range(n):
            g[i][i] = 0
        for x, y, wt in roads:
            g[x][y] = min(g[x][y], wt)
            g[y][x] = min(g[y][x], wt)

        f = [None] * n
        def check(s: int) -> int:
            for i, row in enumerate(g):
                if s >> i & 1:
                    f[i] = row[:]

            # Floyd
            for k in range(n):
                if (s >> k & 1) == 0: continue
                for i in range(n):
                    if (s >> i & 1) == 0: continue
                    for j in range(n):
                        f[i][j] = min(f[i][j], f[i][k] + f[k][j])

            for i, di in enumerate(f):
                if (s >> i & 1) == 0: continue
                for j, dij in enumerate(di):
                    if s >> j & 1 and dij > maxDistance:
                        return 0
            return 1
        return sum(check(s) for s in range(1 << n))  # 枚举子集
