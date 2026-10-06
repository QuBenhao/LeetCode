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
            # Undo the unions
            # 1. Neither person knows the secret, so the meeting has no effect
            # Only connections created in this round can be disconnected from 0, since all retained earlier connections reach 0; undoing them this way is safe
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
            self.parent[x] = self.parent[self.parent[x]]  # Path compression
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in the same set
        self.parent[root_x] = root_y
        return True

    def is_connected(self, x:int, y:int) -> bool:
        return self.find(x) == self.find(y)
