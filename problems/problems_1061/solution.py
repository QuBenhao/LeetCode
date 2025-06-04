import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallestEquivalentString(*test_input)

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
                self.sz = [1] * size
                self.cc = size

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.parent[self.parent[x]]
                return self.parent[x]

            def union(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)

                if root_x == root_y:
                    return False  # 已经在同一集合

                fa = min(root_x, root_y)
                child = max(root_x, root_y)
                self.parent[child] = fa
                self.sz[fa] += self.sz[child]
                self.cc -= 1

                return True

            def is_connected(self, x, y):
                return self.find(x) == self.find(y)

        uf = UnionFind(26)
        for a, b in zip(s1, s2):
            uf.union(ord(a) - ord('a'), ord(b) - ord('a'))
        return ''.join(chr(uf.find(ord(c) - ord('a')) + ord('a')) for c in baseStr)
