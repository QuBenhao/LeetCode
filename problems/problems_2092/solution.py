import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findAllPeople(*test_input)

    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        uf = UnionFind(n)
        uf.union(0, firstPerson)
        meetings.sort(key=lambda x: x[2])
        m = len(meetings)
        i = 0
        while i < m:
            start = i
            time = meetings[i][2]
            while i < m and meetings[i][2] == time:
                x, y, _ = meetings[i]
                uf.union(x, y)
                i += 1
            # 撤销合并
            # 1. 都不知道秘密, 这个会开了等于没开。
            # 实际上这有这一轮刚建连的, 才有可能没和0连接, 因为之前留下的都是和0连通的, 所以这样撤销是没问题的。
            for x, y, _ in meetings[start: i]:
                if not uf.is_connected(x, 0):
                    uf.parent[x] = x
                    uf.parent[y] = y
        return [i for i in range(n) if uf.is_connected(i, 0)]


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # 路径压缩
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # 已经在同一集合
        self.parent[root_x] = root_y
        return True

    def is_connected(self, x:int, y:int) -> bool:
        return self.find(x) == self.find(y)
