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
        queries = sorted((w, p, q, i) for i, (p, q, w) in enumerate(queries))
        edgeList = sorted((w, u, v) for u, v, w in edgeList)

        uf = UnionFind(n)

        ans = [None] * len(queries)
        ii = 0
        for w, p, q, i in queries:
            while ii < len(edgeList) and edgeList[ii][0] < w:
                _, u, v = edgeList[ii]
                uf.union(u, v)
                ii += 1
            ans[i] = uf.find(p) == uf.find(q)
        return ans


class UnionFind:
    def __init__(self, N: int):
        self.parent = list(range(N))
        self.rank = [1] * N

    def find(self, p: int, halving: bool = True) -> int:
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p: int, q: int, ranking: bool = True) -> bool:
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False
        if ranking and self.rank[prt] > self.rank[qrt]:
            prt, qrt = qrt, prt
        self.parent[prt] = qrt
        self.rank[qrt] += self.rank[prt]
        return True
