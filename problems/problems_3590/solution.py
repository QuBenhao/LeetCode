from collections import defaultdict

from sortedcontainers import SortedSet
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.kthSmallest(*test_input)

    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        n = len(par)
        tree: List[List[int]] = [[] for _ in range(n)]
        for i, p in enumerate(par):
            if p != -1:
                tree[p].append(i)

        ans = [-1] * len(queries)
        query = defaultdict(list)
        for i, (u, k) in enumerate(queries):
            query[u].append((k, i))

        xors = [0] * n
        xors[0] = vals[0]
        def dfs(node):
            su = SortedSet()
            su.add(xors[node])
            for child in tree[node]:
                xors[child] = xors[node] ^ vals[child]
                sv = dfs(child)
                if len(sv) > len(su):
                    su, sv = sv, su
                su.update(sv)
            for _k, idx in query[node]:
                if len(su) >= _k:
                    ans[idx] = su[_k - 1]
            return su

        dfs(0)
        return ans
