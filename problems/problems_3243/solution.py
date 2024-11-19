from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.shortestDistanceAfterQueries(*test_input)

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        frm = [[] for _ in range(n)]
        f = list(range(n))
        ans = []
        for l, r in queries:
            frm[r].append(l)
            if f[l] + 1 < f[r]:
                f[r] = f[l] + 1
                for i in range(r + 1, n):
                    f[i] = min(f[i], f[i - 1] + 1, min((f[j] for j in frm[i]), default=inf) + 1)
            ans.append(f[-1])
        return ans
