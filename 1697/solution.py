import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        n, edgeList, queries = test_input
        return self.distanceLimitedPathsExist(n, [l[:] for l in edgeList], [l[:] for l in queries])

    def distanceLimitedPathsExist(self, n, edgeList, queries):
        """
        :type n: int
        :type edgeList: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """

        def root(x):
            while x != parent[x]:
                x = parent[x]
                parent[x] = parent[parent[x]]
            return x

        def union(x, y):
            rx = root(x)
            ry = root(y)
            if rx != ry:
                if size[rx] < size[ry]:
                    rx, ry = ry, rx
                size[rx] += size[ry]
                parent[ry] = rx

        parent = [i for i in range(n)]
        size = [1] * n
        ans = [False] * len(queries)
        edges = sorted(edgeList, key=lambda x: x[2])
        queries = sorted(enumerate(queries), key=lambda x: x[1][2])
        start = 0
        for idx, (x, y, weight) in queries:
            while start < len(edges) and edges[start][2] < weight:
                union(edges[start][0], edges[start][1])
                start += 1
            ans[idx] = root(x) == root(y)
        return ans
#         queries = sorted((w, p, q, i) for i, (p, q, w) in enumerate(queries))
#         edgeList = sorted((w, u, v) for u, v, w in edgeList)
#
#         uf = UnionFind(n)
#
#         ans = [None] * len(queries)
#         ii = 0
#         for w, p, q, i in queries:
#             while ii < len(edgeList) and edgeList[ii][0] < w:
#                 _, u, v = edgeList[ii]
#                 uf.union(u, v)
#                 ii += 1
#             ans[i] = uf.find(p) == uf.find(q)
#         return ans
#
#
# class UnionFind:
#     def __init__(self, N: int):
#         self.parent = list(range(N))
#         self.rank = [1] * N
#
#     def find(self, p: int, halving: bool = True) -> int:
#         if p != self.parent[p]:
#             self.parent[p] = self.find(self.parent[p])
#         return self.parent[p]
#
#     def union(self, p: int, q: int, ranking: bool = True) -> bool:
#         prt, qrt = self.find(p), self.find(q)
#         if prt == qrt: return False
#         if ranking and self.rank[prt] > self.rank[qrt]:
#             prt, qrt = qrt, prt
#         self.parent[prt] = qrt
#         self.rank[qrt] += self.rank[prt]
#         return True
